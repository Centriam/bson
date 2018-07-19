#!/usr/bin/env python
from datetime import datetime, timedelta, time
from unittest import TestCase

import pytz
from bson import dumps, loads


class TestDateTime(TestCase):
    def test_datetime(self):
        now = datetime.now(pytz.utc)
        obj = {"now": now}
        serialized = dumps(obj)
        obj2 = loads(serialized)

        td = obj2["now"] - now
        seconds_delta = (td.microseconds + (td.seconds + td.days * 24 * 3600) *
                         1e6) / 1e6
        self.assertTrue(abs(seconds_delta) < 0.001)


class TestTimeDelta(TestCase):
    def test_datetime(self):
        some_time = timedelta(microseconds=12, seconds=23, hours=2, days=5)
        obj = {"some_time": some_time}
        serialized = dumps(obj)
        obj2 = loads(serialized)

        interval = obj2["some_time"]
        seconds_delta = interval.total_seconds() - some_time.total_seconds()
        self.assertTrue(abs(seconds_delta) < 0.001)

class TestTime(TestCase):
    def test_datetime(self):
        some_time = time(5, 33)
        obj = {"utc_time": some_time}
        serialized = dumps(obj)
        obj2 = loads(serialized)

        interval = obj2["utc_time"]
        as_string = interval.isoformat()
        self.assertTrue(as_string == "05:33:00")