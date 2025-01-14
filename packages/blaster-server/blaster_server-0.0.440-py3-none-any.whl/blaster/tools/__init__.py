'''
Created on 04-Nov-2017

@author: abhinav
'''

from gevent.threading import Thread
from gevent.queue import Queue, Empty as QueueEmptyException
import os
import sys
import weakref
import subprocess
import shlex
import collections
import random
import string
import socket
import struct
import fcntl
import heapq
from gevent import sleep
from functools import reduce as _reduce
from gevent.lock import BoundedSemaphore
from datetime import timezone
from datetime import datetime
from datetime import timedelta
import time
import hmac
import base64
import hashlib
import re
import six
import json
import traceback
import contextlib
from io import BytesIO, StringIO
import requests
from http.client import HTTPConnection  # py3

from ..websocket._core import WebSocket
from ..env import IS_DEV, DEBUG_PRINT_LEVEL
from ..utils.xss_html import XssHtml
from ..utils import events
from ..logging import LOG_APP_INFO, LOG_WARN, LOG_ERROR, LOG_DEBUG

os.environ['TZ'] = 'UTC'
time.tzset()

# some useful constants
INT64_MAX = 9223372036854775807
MILLIS_IN_HOUR = 60 * 60 * 1000
MILLIS_IN_DAY = 24 * MILLIS_IN_HOUR
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_DAY = 24 * 60 * 60

EPOCH = datetime.utcfromtimestamp(0)


_OBJ_END_ = object()
_1KB_ = 1024
_16KB_ = _1KB_ * 16


def cur_ms():
	return int(1000 * time.time())


# genetic LRU cache
class LRUCache:
	cache = None
	capacity = None

	def __init__(self, capacity, items=None):
		self.capacity = capacity
		self.cache = collections.OrderedDict(items or [])
		# in addition to recentness of use

	def exists(self, key):
		return self.cache.get(key, None)

	def get(self, key, default=None):
		try:
			# remove and reinsert into
			# ordered dict to move to recent
			value = self.cache.pop(key)
			self.cache[key] = value
			return value
		except KeyError:
			return default

	def set(self, key, value):
		removed_entries = []
		try:
			self.cache.pop(key)
		except KeyError:
			# new entry so cleanup space if it's beyond capacity
			while(len(self.cache) >= self.capacity):
				removed_entries.append(self.cache.popitem(last=False))
		self.cache[key] = value

		return removed_entries

	def __setitem__(self, key, value):
		return self.set(key, value)

	def __getitem__(self, key, default=None):
		return self.get(key, default)

	def delete(self, key):
		return self.cache.pop(key, None)

	def clear(self):
		return self.cache.clear()

	def to_son(self):
		ret = {}
		for key, val in self.cache:
			ret[key] = val.to_son() if hasattr(val, "to_son") else val
		return ret


class ExpiringCache:
	cache = None
	capacity = None
	ttl = None

	# ttl in millis, 5 minutes default
	def __init__(self, capacity, items=None, ttl=3 * 60 * 1000):
		self.capacity = capacity
		self.cache = collections.OrderedDict()
		self.ttl = ttl
		if(items):
			for k, v in items:
				self.set(k, v)

	def get(self, key, default=None):
		timestamp_and_value = self.cache.get(key, _OBJ_END_)
		if(timestamp_and_value == _OBJ_END_):
			return default
		if(timestamp_and_value[0] > cur_ms()):
			return timestamp_and_value[1]
		self.cache.pop(key, None)  # expired object
		return default

	def set(self, key, value):
		removed_entries = []
		cur_timestamp = cur_ms()
		while(len(self.cache) >= self.capacity):
			removed_entries.append(self.cache.popitem(last=False))
		keys_to_remove = []
		for _key, val in self.cache.items():
			if(val[0] < cur_timestamp):
				keys_to_remove.append(_key)

		for _key in keys_to_remove:
			removed_entries.append(self.cache.pop(_key))

		self.cache[key] = (cur_timestamp + self.ttl, value)
		return removed_entries

	def __setitem__(self, key, value):
		return self.set(key, value)

	def __getitem__(self, key, default=None):
		return self.get(key, default)

	def exists(self, key):
		return key in self.cache

	def delete(self, key):
		return self.cache.pop(key, None)

	def clear(self):
		return self.cache.clear()

	def to_son(self):
		ret = {}
		cur_timestamp = cur_ms()
		for key, _val in self.cache.items():
			expires_at, val = _val
			if(cur_timestamp < expires_at):
				ret[key] = val.to_son() if hasattr(val, "to_son") else val
		return ret


# get SON of the fields from any generic python object
def to_son(obj):
	ret = obj.__dict__
	for k in ret.keys():
		if(ret[k] == None):
			del ret[k]
	return ret


def from_kwargs(cls, **kwargs):
	ret = cls()
	for key in kwargs:
		setattr(ret, key, kwargs[key])
	return ret


def get_by_key_list(d, key_list, default=None):
	try:
		for key in key_list:
			d = d[key]
		return d
	except KeyError:
		return default
	except IndexError:
		return default


def set_by_key_list(d, key_list, value):
	if(not key_list):
		return
	for key in key_list[0:-1]:
		if(key not in d):
			d[key] = {}
		d = d[key]
	d[key_list[-1]] = value


def date2string(date):
	return date.isoformat()


def date2timestamp(dt):
	# datetime to timestamp
	if not isinstance(dt, datetime):
		return dt
	if(six.PY34):
		return dt.replace(tzinfo=timezone.utc).timestamp()
	else:
		timestamp = time.mktime(dt.timetuple()) + dt.microsecond / 1e6
		return timestamp


def timestamp2date(timestamp):
	if not isinstance(timestamp, (int, float)):
		return timestamp
	date = datetime.utcfromtimestamp(timestamp)
	return date


# 1h2m3s
def duration2string(seconds):
	remaining = seconds

	d = remaining // SECONDS_IN_DAY
	remaining = seconds - d * SECONDS_IN_DAY

	h = remaining // SECONDS_IN_HOUR
	remaining = remaining - h * SECONDS_IN_HOUR

	m = remaining // 60
	remaining = remaining - m * 60

	s = remaining

	ret = ""
	if(d):
		ret += f"{d}d"
	if(h):
		ret += f"{h}h"
	if(m):
		ret += f"{m}m"
	if(s):
		ret += f"{s}s"

	return ret


def string2duration(duration_str):
	ret = 0
	splits = re.split(r'([a-zA-Z]+)', duration_str)
	for i in range(0, len(splits) - len(splits) % 2, 2):
		v = int(splits[i])
		c = splits[i + 1]
		if(c[0] == 'd'):
			ret += v * SECONDS_IN_DAY
		if(c[0] == 'h'):
			ret += v * SECONDS_IN_HOUR
		if(c[0] == 'm'):
			ret += v * 60
		if(c[0] == 's'):
			ret += v
	return ret


def zrfill(tup, n):
	return tup + tuple(0 for x in range(n - len(tup)))


def zlfill(tup, n):
	return tuple(0 for x in range(n - len(tup))) + tup


DATE_REGEX = re.compile(r"(\d{1,2})[\/\-\.](\d{1,2})[\/\-\.](\d{4})")
TIME_REGEX = re.compile(r"(\d{1,2}):(\d{0,2})?[:]*(\d{0,2})?(?:\s?((?:A|P).?M))?", re.IGNORECASE)
DAY_REGEX = re.compile(
	r"(mon|tues|wed(nes)?|thur(s)?|fri|sat(ur)?|sun)(day)?",
	re.IGNORECASE
)
DAYS_OF_WEEK = [
	'monday', 'tuesday', 'wednesday',
	'thursday', 'friday', 'saturday', 'sunday'
]


def _bound_time(start, end, a, b, partial, params):
	if(partial):
		if(start >= a and start <= b):
			return (start, (end if end < b else b), params)
		elif(start <= a and a <= end):
			return (a, (end if end < b else b), params)
	else:
		if(start >= a and end <= b):
			return (start, end, params)


# tz_delta = UTC - local ( to dereive UTC times in current timezone)

def iter_time_overlaps(a, b, x: str, tz_delta, partial=False):
	x, *params = x.split("|")
	if(isinstance(a, int)):
		a = timestamp2date(a)

	if(isinstance(b, int)):
		b = timestamp2date(b)
	x = x.strip()
	date_matches = DATE_REGEX.findall(x)
	time_matches = [
		[int(h or 0), int(m or 0), int(s or 0), am_pm.lower()]
		for h, m, s, am_pm in TIME_REGEX.findall(x)
	]
	day_matches = list(
		filter(
			lambda x: DAYS_OF_WEEK.index(x) >= 0,
			[x[m.start():m.end()].lower() for m in DAY_REGEX.finditer(x) or []]
		)
	)
	for time_match in time_matches:
		if(time_match[-1] and time_match[-1][0] in ("a", "p")):
			while(len(time_match) < 4):
				time_match.insert(-1, 0)
		else:
			while(len(time_match) < 4):
				time_match.append(0)

		for i in range(3):
			time_match[i] = int(time_match[i])

	# offset from start of day
	offset_check_x = timedelta()
	offset_check_y = timedelta(hours=24)
	if(time_matches):
		hours, mins, secs, am_pm = time_matches[0]
		if(am_pm):
			# convert to 24 hour format
			if(am_pm.lower()[0] == "p"):
				hours = (hours % 12) + 12
			if(am_pm.lower()[0] == "a"):
				if(hours == 12):
					hours = 0

		offset_check_x = timedelta(hours=hours, minutes=mins, seconds=secs)

		if(len(time_matches) > 1):
			hours, mins, secs, am_pm = time_matches[1]

			if(am_pm):
				# convert to 24 hour format
				if(am_pm.lower()[0] == "p"):
					hours = (hours % 12) + 12
				if(am_pm.lower()[0] == "a"):
					if(hours == 12):
						hours = 0
			offset_check_y = timedelta(hours=hours, minutes=mins, seconds=secs)
		else:
			offset_check_y = offset_check_x + timedelta(hours=1)  # default 1 hour

	if(date_matches):
		day, month, year, *_ = map(lambda x: int(x) if x else 0, date_matches[0])
		if(year < 100):
			year = 2000 + year
		time_range_start = datetime(year=year, month=month, day=day) + offset_check_x
		time_range_end = datetime(year=year, month=month, day=day) + offset_check_y
		if(len(date_matches) > 1):
			day, month, year, *_ = map(lambda x: int(x) if x else 0, date_matches[1])
			if(year < 100):
				year = 2000 + year
			time_range_end = datetime(year=year, month=month, day=day) + offset_check_y

		_ret = _bound_time(time_range_start + tz_delta, time_range_end + tz_delta, a, b, partial, params)
		if(_ret):
			yield _ret

	elif(day_matches):
		start_day = DAYS_OF_WEEK.index(day_matches[0].lower())
		if(start_day == -1):
			return []
		extra_offset_y = timedelta()
		if(len(day_matches) > 1):
			end_day = DAYS_OF_WEEK.index(day_matches[1].lower())
			if(end_day == -1):
				return []
			if(end_day != start_day):
				extra_offset_y = (
					timedelta(hours=24) - offset_check_x  # next day
					+ timedelta(
						days=(
							end_day - start_day
							+ (7 if start_day > end_day else 0)
							- (1 if offset_check_y != timedelta(0) else 0)
						)
					)
				)

		t = a
		while(t <= b):
			if(t.weekday() == start_day):
				t_start_of_day = datetime(year=t.year, month=t.month, day=t.day)
				_ret = _bound_time(
					t_start_of_day + offset_check_x + tz_delta,
					t_start_of_day + extra_offset_y + offset_check_y + tz_delta,
					a, b, partial, params
				)
				if(_ret):
					yield _ret
			t += timedelta(days=1)  # increment by 1 day and keep on checking
	elif(time_matches):  # just times were given
		if(offset_check_y < offset_check_x):
			offset_check_y += timedelta(days=1)
		t_start_of_day = datetime(a.year, a.month, a.day)
		while(t_start_of_day < b):
			_ret = _bound_time(
				t_start_of_day + offset_check_x + tz_delta,
				t_start_of_day + offset_check_y + tz_delta,
				a, b, partial, params
			)
			if(_ret):
				yield _ret
			t_start_of_day += timedelta(days=1)

	return []


def get_time_overlaps(
	a, b, include: list, exclude=None,
	limit=10, partial=False, tz_delta=timedelta(), milliseconds=False
):
	if(isinstance(include, str)):
		include = include.split(",")
	if(isinstance(exclude, str)):
		exclude = exclude.split(",")

	buffer = []
	heapq.heapify(buffer)
	for x in include:
		try:
			it = iter_time_overlaps(a, b, x, tz_delta, partial=partial)
			heapq.heappush(buffer, (next(it), it))
		except StopIteration:
			pass
	ret = []
	while(len(ret) < limit and len(buffer) > 0):
		time_range, it = heapq.heappop(buffer)
		try:
			heapq.heappush(buffer, (next(it), it))
		except StopIteration:
			pass
		# check if it's excluded
		if(
			not exclude
			or not get_time_overlaps(
				time_range[0], time_range[1], exclude,
				limit=1, partial=True, tz_delta=tz_delta
			)
		):
			if(milliseconds):
				ret.append(
					(
						int(date2timestamp(time_range[0]) * 1000),
						int(date2timestamp(time_range[1]) * 1000),
						*time_range[2:]
					)
				)
			else:
				ret.append(time_range)
	return ret


def get_start_of_day(t):
	return datetime(year=t.year, month=t.month, day=t.day)


def get_start_of_day_millis(millis):
	return (millis // MILLIS_IN_DAY) * MILLIS_IN_DAY


def find_index(a_list, value):
	try:
		return a_list.index(value)
	except ValueError:
		return -1


def find_nth(haystack, needle, n):
	''' Find position of nth occurance in a string'''
	if(not haystack):
		return -1
	start = haystack.find(needle)
	while start >= 0 and n > 1:
		start = haystack.find(needle, start + len(needle))
		n -= 1
	return start


SOME_TIME_WHEN_WE_STARTED_THIS = 1471504855
SOME_TIME_WHEN_WE_STARTED_THIS_MILLIS_WITH_10 = 16111506425808


# this function is inspired from instagram engineering
# post on generating 64bit keys with 12 bit shard_id inside it
# __thread_data = LRUCache(10000)
def generate_64bit_key(shard_id):  # shard id should be a 12 bit number
	# may be later use dattime
	millis_elapsed = int((time.time() - SOME_TIME_WHEN_WE_STARTED_THIS) * 1000)

	# 41 bits , clear 22 places for random id and shard_id
	_id = (((1 << 41) - 1) & millis_elapsed) << 23

	# 12 bit shard id, on top
	_id |= (((1 << 12) - 1) & shard_id) << 11

	# increment per thread number
	# thread_id = threading.current_thread().ident
	# thread_data = __thread_data.get(thread_id, None)
	# if(not thread_data):
	#     thread_data = [0]
	#     __thread_data.set(thread_id , thread_data)
	# thread_data[0] = (thread_data[0] + 1)%(1 << 11)
	random_11_bits = random.randrange(0, 1 << 11)
	_id |= (((1 << 11) - 1) & random_11_bits)  # clear 12 places for random

	# shard_id|timestmap|random_number

	return _id


def int_to_bytes(number: int) -> bytes:
	return number.to_bytes(
		length=(8 + (number + (number < 0)).bit_length()) // 8,
		byteorder='big',
		signed=True
	)


BASE_62_LIST = string.ascii_uppercase + string.digits + string.ascii_lowercase
BASE_62_DICT = dict((c, i) for i, c in enumerate(BASE_62_LIST))


def str_to_int(string, reverse_base=BASE_62_DICT):
	length = len(reverse_base)
	ret = 0
	for i, c in enumerate(string[::-1]):
		ret += (length ** i) * reverse_base[c]

	return ret


def int_to_str(integer, base=BASE_62_LIST):
	if integer == 0:
		return base[0]

	length = len(base)
	ret = ''
	while integer != 0:
		ret = base[integer % length] + ret
		integer //= length

	return ret


def get_int_id():
	time_elapsed \
		= time.time() * 10000 - SOME_TIME_WHEN_WE_STARTED_THIS_MILLIS_WITH_10
	return int(time_elapsed)


def get_str_id():
	return int_to_str(get_int_id())


def is_almost_equal(a, b, max_diff=0.01):
	if(a == None and b == None):
		return True
	if(a == None or b == None):
		return False
	diff = abs(a - b)
	if(diff < max_diff):
		return False
	return True


# protobuf + mysql utility functions
def list_to_protobuf(values, message):
	'''parse list to protobuf message'''
	if not values:
		return
	if isinstance(values[0], dict):  # value needs to be further parsed
		for v in values:
			cmd = message.add()
			dict_to_protobuf(v, cmd)
	else:  # value can be set
		message.extend(values)


# just like move constructor ;) , move values much faster than copies
def dict_to_protobuf(
	values, obj,
	transformations=None, excludes=None, preserve_values=True
):
	if(not preserve_values):
		if(transformations):
			for k, func in transformations.items():
				values[k] = func(values.get(k, None))

		if(excludes):
			for exclude, flag in excludes.items():
				if(hasattr(values, exclude)):
					del values[exclude]

	for k, v in values.items():
		if(preserve_values):
			if(transformations and k in transformations):
				v = transformations[k](v)

			if(excludes and k in excludes):
				continue

		if hasattr(obj, k):
			if isinstance(v, dict):  # value needs to be further parsed
				dict_to_protobuf(v, getattr(obj, k))
			elif isinstance(v, list):
				list_to_protobuf(v, getattr(obj, k))
			else:  # value can be set
				if v:  # otherwise default
					setattr(obj, k, v)


def get_mysql_rows_as_dict(res):
	rows_as_dict = []
	for row in res.rows:
		as_dict = {}
		for field, val in zip(res.fields, row):
			as_dict[field[0]] = val

		rows_as_dict.append(as_dict)

	return rows_as_dict

########################


def remove_duplicates(lst, key=None):
	exists = set()
	ret = []
	for i in lst:
		if(key):
			if((key_val := key(i)) in exists):
				continue
			exists.add(key_val)
		else:
			if(i in exists):
				continue
			exists.add(i)
		# i doesn't exist
		ret.append(i)
	return ret


def get_shard_id(_id):
	return (int(_id) & (((1 << 12) - 1) << 11)) >> 11


# can split at most at n points
# always returns n + 1 parts
def nsplit(_str, delimiter, n):
	parts = _str.split(delimiter, n)
	for i in range(n + 1 - len(parts)):
		parts.append(None)
	return parts


# move it to seperate module ?
# copied from internet sha1 token encode - decode module
if hasattr(hmac, 'compare_digest'):  # python 3.3
	hmac_compare_digest = hmac.compare_digest
else:
	def hmac_compare_digest(a, b):
		if len(a) != len(b):
			return False
		result = 0
		if isinstance(a[0], int):  # python3 byte strings
			for x, y in zip(a, b):
				result |= x ^ y
		else:  # python2
			for x, y in zip(a, b):
				result |= ord(x) ^ ord(y)
		return result == 0


def utf8(value) -> bytes:
	if(isinstance(value, bytes)):
		return value
	return value.encode("utf-8")


def create_signed_value(name, value, secret, expires_in=31 * SECONDS_IN_DAY) -> bytes:
	expires_at = utf8(str(int(time.time() + expires_in)))
	value = base64.b64encode(utf8(value))  # hide value
	# ~ to prevent changing value, timestamp but value + timestamp being same
	signature = hmac_hexdigest(secret, name, value, b"~", expires_at)
	signed_value = b"|".join([value, b"~", expires_at, signature])
	return signed_value


def decode_signed_value(name, value, secret, expiry_check=True) -> bytes:
	if not value:
		return None
	_parts = utf8(value).split(b"|")
	if len(_parts) < 3:
		return None
	_value, *parts, expires_at, _signature = _parts
	# check signature matches or not
	signature = hmac_hexdigest(secret, name, _value, *parts, expires_at)
	if not hmac_compare_digest(_signature, signature):
		return None

	if(expiry_check):
		expires_at = int(expires_at)
		if(time.time() > expires_at):
			return None
	try:
		return base64.b64decode(_value)
	except Exception:
		return None


def hmac_hexdigest(secret, *parts) -> bytes:
	hash = hmac.new(utf8(secret), digestmod=hashlib.sha256)
	for part in parts:
		hash.update(utf8(part))
	return utf8(hash.hexdigest())


"""Dependencies are expressed as a dictionary whose keys are items
	and whose values are a set of dependent items. Output is a list of
	sets in topological order. The first set consists of items with no
	dependences, each subsequent set consists of items that depend upon
	items in the preceeding sets.
"""


def toposort(data):

	# Special case empty input.
	if len(data) == 0:
		return

	# Copy the input so as to leave it unmodified.
	data = data.copy()

	# Ignore self dependencies.
	for k, v in data.items():
		v.discard(k)
	# Find all items that don't depend on anything.
	extra_items_in_deps = _reduce(set.union, data.values()) - set(data.keys())
	# Add empty dependences where needed.
	data.update({item: set() for item in extra_items_in_deps})
	while True:
		ordered = set(item for item, dep in data.items() if len(dep) == 0)
		if not ordered:
			break
		yield ordered
		data = {
			item: (dep - ordered)
			for item, dep in data.items() if item not in ordered
		}
	if len(data) != 0:
		exception_string = \
			'Circular dependencies exist among these items: {{{}}}'.format(
				', '.join([
					'{!r}:{!r}'.format(key, value) for key, value in sorted(data.items())
				])
			)
		raise Exception(exception_string)


# Console or Cloud Console.
def get_random_id(length=10, include_timestamp=True):
	'''returns a random string containing numbers lowercase upper case'''
	'''http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python'''

	key_str = ''.join(
		random.SystemRandom().choice(BASE_62_LIST) for _ in range(length)  # iter
	)
	if(include_timestamp):
		key_str = f"{int(time.time())}{key_str}"
	# key_str = hashlib.md5(key_str).hexdigest()
	return key_str


# jump consistent hash function , jump_hash("Asdasd", 100) assigns to a bucket
def jump_hash(key, num_buckets):
	b, j = -1, 0
	key = int(hashlib.md5(key).hexdigest(), 16)
	while j < num_buckets:
		b = int(j)
		key = ((key * int(2862933555777941757)) + 1) & 0xFFFFFFFFFFFFFFFF
		j = float(b + 1) * (float(1 << 31) / float((key >> 33) + 1))
	return int(b)

##############


number_regex = re.compile(r"([0-9\.]+)")
non_alpha_num_space_dot_regex = re.compile(r"[^0-9a-zA-Z \.]", re.DOTALL)  # space, . allowed
non_alpha_regex = re.compile(r"[^0-9a-zA-Z]", re.DOTALL)
non_alpha_num_underscore_regex = re.compile(r"[^0-9a-zA-Z_]", re.DOTALL)
non_alpha_groups_regex = re.compile(r"[^0-9a-zA-Z]+", re.DOTALL)  # multiple non-alpha groups


def sanitize_string(text):
	return non_alpha_num_space_dot_regex.sub("", text)


def sanitize_to_id(text):
	return non_alpha_regex.sub("", text.lower())


def sanitize_to_id_allow_case(text):
	return non_alpha_regex.sub("", text)


def sanitize_to_id2(text):
	return non_alpha_groups_regex.sub("_", text.strip().lower())


EMAIL_REGEX = re.compile(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*(\+[_a-z0-9-]+)?\@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,6})$')


def is_valid_email(email):
	return EMAIL_REGEX.match(email)


SANITIZE_EMAIL_REGEX_NO_PLUS_ALLOWED = re.compile(r"\+[^@]*")


def sanitize_email_id(email_id, plus_allowed=True):
	if(not email_id):
		return None
	email_id = email_id.strip().lower()
	if(not EMAIL_REGEX.match(email_id)):
		return None

	if(not plus_allowed):
		email_id = SANITIZE_EMAIL_REGEX_NO_PLUS_ALLOWED.sub("", email_id)

	return email_id


# first minus second
def list_diff(first, second):
	if(not first or not second):
		return first
	second = set(second)
	return [item for item in first if item not in second]


# what are added vs what need to be deleted from first
# no order
def list_diff2(first, second, key=None):
	if(not first and second):
		return [], list(second)
	if(second == None):
		return list(first), []
	if(key):
		second_keys = set(map(key, second))
		first_keys = set(map(key, first))
		# to add and delete
		return [item for item in first if key(item) not in second_keys],\
			[item for item in second if key(item) not in first_keys]
	else:
		second = set(second)
		first = set(first)
		# to add and delete
		return [item for item in first if item not in second],\
			[item for item in second if item not in first]


# a dummy object with given keys,values
class DummyObject:
	entries = None

	def __init__(self, entries=None, **kwargs):
		self.entries = entries or {}
		if(kwargs):
			self.entries = _entries = dict(entries)
			_entries.update(kwargs)

	def __setattr__(self, key, val):
		if(self.entries):
			self.entries[key] = val
		else:
			super().__setattr__(key, val)

	def __getattr__(self, key):
		return self.entries.get(key)

	def get(self, key, default=None):
		return self.entries.get(key, default)

	def __getitem__(self, key):
		return self.entries.get(key)

	def __setitem__(self, key, val):
		self.entries[key] = val

	def to_dict(self):
		return self.entries


# fully qualified name of the object
def object_name(o):
	# o.__module__ + "." + o.__class__.__qualname__ is an example in
	# this context of H.L. Mencken's "neat, plausible, and wrong."
	# Python makes no guarantees as to whether the __module__ special
	# attribute is defined, so we take a more circumspect approach.
	# Alas, the module name is explicitly excluded from __qualname__
	# in Python 3.

	module = o.__class__.__module__
	if module is None or module == str.__class__.__module__:
		return o.__class__.__name__  # Avoid reporting __builtin__
	else:
		return module + '.' + o.__class__.__name__


# normalize a int/str to n number of characters
def normalize(val, n=13):
	val = str(val)
	length = len(val)
	if(n >= length):
		return ("0" * (n - length)) + val

	raise Exception('cannot have greater length, ensure about this')


# normalize a int/str to n number of characters
# and clips of any characters more than n characters
def normalize_no_warn(val, n=13):
	val = str(val)
	length = len(val)
	if(n >= length):
		return ("0" * (n - length)) + val
	return val


def ltrim(_str, str_to_remove):
	if(str_to_remove and _str.startswith(str_to_remove)):
		return _str[len(str_to_remove):]
	return _str


def rtrim(_str, str_to_remove):
	if(str_to_remove and _str.endswith(str_to_remove)):
		return _str[:len(_str) - len(str_to_remove)]
	return _str


def trim(_str, str_to_remove):
	return rtrim(ltrim(_str, str_to_remove), str_to_remove)


# remove zeros in the front
# returns 0 if it's all zeroes
def de_normalize(id1):
	i = 0
	length = len(id1)
	while(i < length):
		if(id1[i] != '0'):
			break
		i = i + 1
	if(i >= length):
		return '0'
	return id1[i:]


def set_non_blocking(fd):
	"""
	Set the file description of the given file descriptor to non-blocking.
	"""
	flags = fcntl.fcntl(fd, fcntl.F_GETFL)
	flags = flags | os.O_NONBLOCK
	fcntl.fcntl(fd, fcntl.F_SETFL, flags)


# generic thread pool to submit tasks which will be
# picked up wokers and processed
class Worker(Thread):
	is_running = True

	""" Thread executing tasks from a given tasks queue """
	def __init__(self, tasks=None, name="worker thread"):
		self.tasks = tasks or Queue()
		super().__init__(name=name)

	def run(self):
		while self.is_running:
			# get a task from queue
			func, args, kargs = self.tasks.get()
			try:
				func(*args, **kargs)
			except Exception as ex:
				# An exception happened in this thread
				stacktrace_string = traceback.format_exc()
				LOG_ERROR(
					"blaster_worker_thread",
					exception_str=str(ex),
					stacktrace_string=stacktrace_string
				)
				IS_DEV and traceback.print_exc()
			finally:
				# Mark this task as done, whether an exception happened or not
				self.tasks.task_done()


class ThreadPool:
	""" Pool of threads consuming tasks from a single queue """
	# queue of tasks
	tasks = None
	worker_threads = None

	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		self.worker_threads = []
		for _ in range(num_threads):
			worker_thread = Worker(self.tasks)
			self.worker_threads.append(worker_thread)
			# start the worker thread
			worker_thread.start()

	def add_task(self, func, *args, **kargs):
		""" Add a task to the queue """
		self.tasks.put((func, args, kargs))

	def join(self):
		""" Wait for completion of all the tasks in the queue """
		self.tasks.join()
		# stop processing
		for worker_thread in self.worker_threads:
			worker_thread.is_running = False
		# join all threads
		for worker_thread in self.worker_threads:
			worker_thread.join()


def raise_exception(msg):
	raise Exception(msg)


def make_xss_safe(_html):
	if(not _html):
		return _html
	parser = XssHtml()
	parser.feed(_html)
	parser.close()
	return parser.getHtml()


# yeild batches of items from iterator
def batched_iter(iterable, n=1):
	current_batch = []
	for item in iterable:
		current_batch.append(item)
		if len(current_batch) == n:
			yield current_batch
			current_batch = []
	if current_batch:
		yield current_batch


# This is the most *important* socket wrapped implementation
# used by blaster server.
class BufferedSocket():

	is_eof = False
	sock = None
	store = None
	lock = None

	def __init__(self, sock):
		self.sock = sock
		self.store = bytearray()

	def close(self):
		self.sock.close()
		self.is_eof = True

	def send(self, *_data):
		total_sent = 0
		for data in _data:
			if(isinstance(data, str)):
				data = data.encode()
			n = 0
			data_len = len(data)
			data_mview = memoryview(data)
			while(n < data_len):
				sent = self.sock.send(data_mview[n:])
				if(sent < 0):
					return sent  # return failed
				n += sent
			total_sent += n
		return total_sent

	def sendl(self, *_data):
		if(not self.lock):
			self.lock = BoundedSemaphore()
		self.lock.acquire()
		ret = self.send(*_data)
		self.lock.release()
		return ret

	def recv(self, n):
		if(self.is_eof):
			return None
		if(self.store):
			ret = self.store
			self.store = bytearray()
			return ret
		return self.sock.recv(n)

	def recvn(self, n):
		if(self.is_eof):
			return None
		while(len(self.store) < n):
			data = self.sock.recv(4096)
			if(not data):
				self.is_eof = True
				break
			self.store.extend(data)

		# return n bytes for now
		ret = self.store[:n]
		# set remaining to new store
		self.store = self.store[n:]
		return ret

	# fails if it couldn't find the delimiter until max_size
	def readuntil(self, delimiter, max_size, discard_delimiter):
		if(self.is_eof):
			return None
		# check in store
		if(isinstance(delimiter, str)):
			delimiter = delimiter.encode()

		delimiter_len = len(delimiter)
		# scan the store until end, if not found extend
		# and continue until store > max_size
		to_scan_len = len(self.store)
		i = 0  # how much we scanned already

		_store = self.store  # get a reference
		while(True):
			if(i > max_size):
				self.is_eof = True
				return None
			if(i >= delimiter_len):
				j = 0
				lookup_from = i - delimiter_len
				while(j < delimiter_len and _store[lookup_from + j] == delimiter[j]):
					j += 1

				if(j == delimiter_len):
					# found
					ret = None
					if(discard_delimiter):
						ret = _store[:i - delimiter_len]
					else:
						ret = _store[:i]
					self.store = _store[i:]  # set store to unscanned/pending
					return ret
			if(i >= to_scan_len):
				# scanned all buffer
				data = self.sock.recv(4096)
				if(not data):
					self.is_eof = True
					return None

				_store.extend(data)  # fetch more data
				to_scan_len = len(_store)
			i += 1

	def __getattr__(self, key):
		ret = getattr(self.sock, key, _OBJ_END_)
		if(ret == _OBJ_END_):
			raise AttributeError()
		return ret


# this variable indicated the TCP_USER_TIMEOUT
# parameter that indicated after how long without an
# ack packet we should close
__tcp_user_timeout = 30 * 1000


def set_socket_fast_close_options(sock):
	# abruptly close the connection after 10 seconds
	# without back and forth communication about closing
	# i.e waiting in time_wait state
	sock.setsockopt(
		socket.SOL_SOCKET, socket.SO_LINGER,
		struct.pack('ii', 1, 10)
	)
	# it can wait 10 seconds,
	# if there is congestion on the network card to send data
	sock.setsockopt(
		socket.SOL_SOCKET, socket.SO_SNDTIMEO,
		struct.pack('ll', 10, 0)
	)

	# after 30 seconds if there is no ack
	# then we assume broken and close it
	TCP_USER_TIMEOUT = 18
	sock.setsockopt(socket.SOL_TCP, TCP_USER_TIMEOUT, 30 * 1000)


# wraps send method of websocket which keeps a buffer of messages
# for 20 seconds if the connection closes, you can use them to resend
class WebsocketConnection(WebSocket):
	# to keep track of how many greenlets are waiting on semaphore to send
	queue = None
	# queue for older sent messages in case of reset we try to retransmit
	msg_assumed_sent = None
	ws = None
	lock = BoundedSemaphore()
	is_stale = False
	last_msg_recv_timestamp = None
	last_msg_sent_timestamp = None

	user_id = None
	is_viewer_list = False

	def __init__(self, ws, user_id):
		self.ws = ws
		# to keep track of how many greenlets are waiting on semaphore to send
		self.queue = collections.deque()
		# queue for older sent messages in case of reset we try to retransmit
		self.msg_assumed_sent = collections.deque()
		self.user_id = user_id

		self.last_msg_recv_timestamp\
			= self.last_msg_sent_timestamp \
			= time.time() * 1000

	# msg is only string data , #ref is used
	# just in case an exception occurs , we pass that ref
	def send(self, msg, ref=None, add_to_assumend_sent=True):
		if(self.is_stale):
			raise Exception("stale connection")

		self.queue.append((ref, msg))
		if(self.lock.locked()):
			return

		self.lock.acquire()
		data_ref = None
		data = None
		try:
			while(not self.is_stale and len(self.queue) > 0):
				data_ref, data = self.queue.popleft()  # peek
				self.ws.send(data)  # msg objects only
				current_timestamp = time.time() * 1000
				self.last_msg_sent_timestamp = current_timestamp
				if(add_to_assumend_sent):
					while(
						len(self.msg_assumed_sent) > 0
						and self.msg_assumed_sent[0][0] < current_timestamp - __tcp_user_timeout
					):
						# keep inly 20 seconds of previous data
						self.msg_assumed_sent.popleft()

					self.msg_assumed_sent.append((current_timestamp, data_ref, data))
		except Exception:
			err_msg = "Exception while sending message to {}, might be closed ".format(
				self.user_id
			)
			self.is_stale = True
			raise Exception(err_msg)
		finally:
			self.lock.release()
		return


def parse_cmd_line_arguments():
	from sys import argv
	args = []
	args_map = {}
	i = 0
	num_args = len(argv)
	while(i < num_args):
		arg = argv[i]
		if(arg.startswith("-")):
			if("=" in arg):
				key, val = arg.split("=", 1)
				args_map[key.lstrip("-")] = val
			else:
				next_arg = True
				if(i + 1 < num_args and not argv[i + 1].startswith("-")):
					next_arg = argv[i + 1]
					i += 1
				args_map[arg.lstrip("-")] = next_arg
		else:
			args.append(arg)

		i += 1
	return args, args_map


# PARSE COMMAND LINE ARGUMENTS BY DEFAULT
CommandLineArgs, CommandLineNamedArgs = parse_cmd_line_arguments()


def run_shell(cmd, output_parser=None, shell=False, max_buf=5000, fail=True, state=None, env=None, **kwargs):

	DEBUG_PRINT_LEVEL > 2 and print(f"#RUNNING: {cmd}")
	state = state if state != None else DummyObject()
	state.total_output = ""
	state.total_err = ""

	# keep parsing output
	def process_output(proc_out, proc_in):
		while(state.is_running):
			_out = proc_out.read(1)
			if(not _out):
				break
			_out = _out.decode('utf-8', 'ignore')
			# add to our input
			state.total_output += _out
			if(len(state.total_output) > 2 * max_buf):
				state.total_output = state.total_output[-max_buf:]

			if(output_parser):
				# parse the output and if it returns something
				# we write that to input file(generally stdin)
				_inp = output_parser(state.total_output, state.total_err)
				if(_inp):
					proc_in.write(_inp)
			else:
				print(_out, end="", flush=True)

	def process_error(proc_err, proc_in):
		while(state.is_running):
			_err = proc_err.read(1)
			if(not _err):
				break
			_err = _err.decode('utf-8', 'ignore')
			# add to our input
			state.total_err += _err
			if(len(state.total_err) > 2 * max_buf):
				state.total_err = state.total_err[-max_buf:]
			if(output_parser):
				# parse the output and if it returns something
				# we write that to input file(generally stdin)
				_inp = output_parser(state.total_output, state.total_err)
				if(_inp):
					proc_in.write(_inp)
			else:
				print(_err, end="", flush=True)

	if(isinstance(cmd, str) and not shell):
		cmd = shlex.split(cmd)

	dup_stdin = os.dup(sys.stdin.fileno()) if shell else subprocess.PIPE
	_env = os.environ.copy()
	if(env):
		_env.update(env)

	state.proc = proc = subprocess.Popen(
		cmd,
		stdin=dup_stdin,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		shell=shell,
		env=_env,
		**kwargs
	)
	state.is_running = True

	# process output reader
	output_parser_thread = Thread(
		target=process_output,
		args=(
			proc.stdout,
			proc.stdin
		)
	)
	# process err reader
	err_parser_thread = Thread(
		target=process_error,
		args=(
			proc.stderr,
			proc.stdin
		)
	)
	output_parser_thread.start()
	err_parser_thread.start()

	os.close(dup_stdin) if dup_stdin != subprocess.PIPE else None

	# just keep printing error
	# wait for process to terminate
	ret_code = proc.wait()
	state.return_code = ret_code
	state.is_running = False
	output_parser_thread.join()
	err_parser_thread.join()
	state.proc = None
	if(ret_code and fail):
		raise Exception(f"Non zero return code :{ret_code}")
	return state


# args is array of strings or array or array of words
# you can use this to return a bunch of strings to index
# in elasticsearch with key "search_words"
def condense_for_search(*args):
	global_word_map = {}
	for arg in args:
		if(not arg):
			continue
		word_map = {}
		if(isinstance(arg, str)):
			arg = arg.split()
		for word in arg:
			key = word[:5]
			existing_words_of_key = word_map.get(key)
			if(not existing_words_of_key):
				word_map[key] = existing_words_of_key = []
			existing_words_of_key.append(word)
		for _key, words in word_map.items():
			_words = global_word_map.get(_key)
			# when existing matching words list
			# has more than current arg, ignore
			if(_words and len(_words) > len(words)):
				continue
			global_word_map[_key] = words

	ret = []
	for key, vals in global_word_map.items():
		ret.extend(vals)

	return ret


# returns None when there are exceptions instead of throwing
def ignore_exceptions(*exceptions):
	def decorator(func):
		def new_func(*args, **kwargs):
			try:
				func(*args, **kwargs)
			except Exception as ex:
				for exception in exceptions:
					if(isinstance(ex, exception)):
						return None
				raise ex

		new_func._original = getattr(func, "_original", func)
		return new_func
	return decorator


# r etries all exceptions or specific given expections only
# backoff = 1 => exponential sleep
# max_time milliseconds for exception to sleep, not counts the func runtime
def retry(num_retries=2, ignore_exceptions=None, max_time=5000):
	num_retries = max(2, num_retries)
	sleep_time_on_fail = max_time / num_retries
	ignore_exceptions = ignore_exceptions or []

	def decorator(func):
		def new_func(*args, **kwargs):
			retry_count = 0
			while(retry_count < num_retries):
				try:
					return func(*args, **kwargs)
				except Exception as ex:
					ignore_exception = False
					for _ex_type in ignore_exceptions:
						if(isinstance(ex, _ex_type)):
							ignore_exception = True
							break
					if(not ignore_exception):
						raise ex
					LOG_WARN("retrying", func=func.__name__, exception=str(ex))
					sleep(sleep_time_on_fail / 1000)
				retry_count += 1
			return None

		new_func._original = getattr(func, "_original", func)
		return new_func
	return decorator


def original_function(func):
	_original = getattr(func, "_original", _OBJ_END_)
	if(_original != _OBJ_END_):
		return _original

	while(True):
		func_wrapped = getattr(func, "__wrapped__", _OBJ_END_)
		if(func_wrapped == _OBJ_END_):
			break
		func = func_wrapped

	return func


def empty_func():
	pass


# when server shutsdown
_joinables = []


# partioned queues
_partitioned_background_task_queues = None


def _process_task_queue(_queue):
	while _process_task_queue.can_process or not _queue.empty():
		posted_at = 0
		start_at = 0
		try:
			posted_at, func, args, kwargs = _queue.get(timeout=300)
			start_at = cur_ms()
			func(*args, **kwargs)
		except QueueEmptyException:
			LOG_DEBUG("background_task_queue_empty", _id=id(_queue))
			continue
		except Exception as ex:
			stacktrace_string = traceback.format_exc()
			LOG_ERROR(
				"background_task_run_error",
				func_name=func.__name__,
				exception_str=str(ex),
				stacktrace_string=stacktrace_string
			)
			IS_DEV and traceback.print_exc()

		end_at = cur_ms()
		exec_ms = end_at - start_at
		delay_ms = end_at - posted_at
		if(delay_ms > 10000):
			# background tasks should be executed fast
			# some tasks may be blocking the queue
			LOG_WARN(
				"background_task_perf",
				func_name=func.__name__,
				delay_ms=delay_ms,
				exec_ms=exec_ms
			)
		if(exec_ms > 3000):
			LOG_WARN(
				"background_task_took_long",
				func_name=func.__name__,
				delay_ms=delay_ms,
				exec_ms=exec_ms
			)


_process_task_queue.can_process = True
# singleton


def start_background_task_processors(n):
	global _partitioned_background_task_queues
	if(_partitioned_background_task_queues != None):
		return
	_partitioned_background_task_queues = tuple()  # empty tuple, so we don't run this twice
	_queues = []
	for _ in range(n):
		_queues.append(_queue := Queue())
		_thread_to_start = Thread(
			target=_process_task_queue,
			args=(_queue,),
		)
		LOG_APP_INFO(
			"background_threads", msg="starting background tasks processor thread",
			func=_process_task_queue.__name__
		)
		_thread_to_start.start()
		_joinables.append(_thread_to_start)
	_partitioned_background_task_queues = tuple(_queues)


# submit a task:func to a partition
# parition is used when you want them to execute in the
# same order as submitted
def submit_background_task(partition_key, func, *args, **kwargs):
	# start processors if not started already
	now_millis = cur_ms()
	if(partition_key == None):
		partition_key = now_millis  # choose a random key

	if(not _process_task_queue.can_process):
		raise Exception("Cannot submit tasks to a queue which is not processing")

	# wait for processors to start
	while(not _partitioned_background_task_queues):
		from blaster.config import NUM_BACKGROUND_TASK_PROCESSORS
		start_background_task_processors(NUM_BACKGROUND_TASK_PROCESSORS or 4)
		LOG_APP_INFO(
			"background_threads_starting",
			msg="waiting for background tasks processors to start",
		)
		sleep(0.1)

	_queue = _partitioned_background_task_queues[hash(str(partition_key)) % len(_partitioned_background_task_queues)]
	_queue.put((now_millis, func, args, kwargs))
	try:
		_item = _queue.peek(block=False)  # this won't block or raise exception
		delay = _item[0] - now_millis
		if(delay > 15000):
			LOG_WARN("background_task_queue_long_delay", queue_id=id(_queue), delay_ms=delay)
	except QueueEmptyException:
		pass


# decorator to be used for a short io tasks to be
# run in background
def background_task(func):
	def wrapper(*args, **kwargs):
		# spawn the thread
		submit_background_task(None, func, *args, **kwargs)
		return True

	wrapper._original = getattr(func, "_original", func)
	return wrapper


# Blaster exit functions
@events.register_listener(["blaster_exit0"])
def exit_0():
	# start of exit - background threads cannot run
	# push an empty function to queues to flush them off
	if(_partitioned_background_task_queues):
		_process_task_queue.can_process = False
		for _queue in _partitioned_background_task_queues:
			_queue.put((cur_ms(), empty_func, [], {}))

# Background tasks END


@events.register_listener(["blaster_exit5"])
def exit_5():
	# reap all joinables of background threads,
	# everything should be done by this point
	for _joinable in _joinables:
		_joinable.join()
	_joinables.clear()
	LOG_DEBUG("background_threads", msg="cleanedup")


# calls a function after the function returns given by argument after
def call_after_func(func):

	if(isinstance(func, str)):
		# after_func => take from args named by func
		def decorator(func):
			def new_func(*args, **kwargs):
				after_func = kwargs.pop(func, None)
				ret = func(*args, **kwargs)
				after_func and after_func()
				return ret

			new_func._original = getattr(func, "_original", func)
			return new_func
		return decorator

	else:
		def new_func(*args, after=None, **kwargs):
			ret = func(*args, **kwargs)
			after and after()
			return ret

		new_func._original = getattr(func, "_original", func)
		return new_func


def all_subclasses(cls):
	return set(cls.__subclasses__()).union(
		[s for c in cls.__subclasses__() for s in all_subclasses(c)]
	)


# print debugging info for networks request called with requests
def debug_requests_on():
	import logging
	'''Switches on logging of the requests module.'''
	HTTPConnection.debuglevel = 3
	logging.basicConfig()
	logging.getLogger().setLevel(logging.DEBUG)
	requests_log = logging.getLogger("requests.packages.urllib3")
	requests_log.setLevel(logging.DEBUG)
	requests_log.propagate = True


def debug_requests_off():
	'''Switches off logging of the requests module, might be some side-effects'''
	import logging
	HTTPConnection.debuglevel = 0

	root_logger = logging.getLogger()
	root_logger.setLevel(logging.WARNING)
	root_logger.handlers = []
	requests_log = logging.getLogger("requests.packages.urllib3")
	requests_log.setLevel(logging.WARNING)
	requests_log.propagate = False


@contextlib.contextmanager
def debug_requests():
	'''Use with 'with'!'''
	debug_requests_on()
	yield
	debug_requests_off()


def cached_request(
	url, ignore_cache_read=False, cache_folder="/tmp/",
	as_string_buffer=False, _json=None, data=None, headers=None
):
	cache_hash = url
	if(_json):
		cache_hash += json.dumps(_json)
	elif(data):
		cache_hash += json.dumps(data)
	cache_hash = hashlib.md5(cache_hash.encode("utf-8")).hexdigest()
	cache_file_path = cache_folder + cache_hash
	if(ignore_cache_read or not os.path.isfile(cache_file_path)):
		if(_json or data):
			resp = requests.post(url, json=_json, data=data, headers=headers, stream=True)
		else:
			resp = requests.get(url, headers=headers, stream=True)
		try:
			with open(cache_file_path, "wb") as cache_file:
				for chunk in resp.iter_content():
					cache_file.write(chunk)
		except Exception:
			os.remove(cache_file_path)

	bytes_buffer = BytesIO(open(cache_file_path, "rb").read())
	if(as_string_buffer):
		return StringIO(bytes_buffer.read().decode())
	else:
		return bytes_buffer


def memoized_method(func):
	cache = {}

	def wrapper(self, *args, **kwargs):
		# need weakref otherwise cache will never be garbage collected
		key = (weakref.ref(self), args, frozenset(kwargs.items()))
		if key in cache:
			return cache[key]
		result = func(self, *args, **kwargs)
		cache[key] = result
		return result
	setattr(wrapper, "_original", func)
	wrapper.clear_cache = cache.clear
	return wrapper
