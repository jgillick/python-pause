#!/usr/bin/env python

"""
Suspend the execution of your program for a given amount of time.
This works similarly to ``time.sleep``, but uses your computers timestamp to track time, versus a counter.
"""

"""
The MIT License (MIT)

Copyright (c) 2013 Jeremy Gillick

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from datetime import datetime
import time as pytime
from time import sleep


def until(time):
    """
    Pause your program until a specific end time.
    'time' is either a valid datetime object or unix timestamp in seconds (i.e. seconds since Unix epoch)
    """
    end = time

    # Convert datetime to unix timestamp
    if type(time) is datetime:
        end = float(time.strftime('%s.%f'))

    # Type check
    if type(end) not in [int, float]:
        raise Exception('The time parameter is not a number or datetime object')

    # Now we wait
    while True:
        now = pytime.time()
        diff = end - now

        #
        # Time is up!
        #
        if diff <= 0:
            break

        #
        # Let's try to tune the precision, as we get closer to the end time
        #

        # Sleep by 0.001, when we're within 0.1 seconds
        if diff <= 0.1:
            sleep(0.001)

        # Sleep by 0.01, when we're within 0.5 seconds
        elif diff <= 0.5:
            sleep(0.01)

        # Sleep by 0.1, when we're within 1.5 seconds
        elif diff <= 1.5:
            sleep(0.1)

        # Otherwise sleep by 1 second
        else:
            sleep(1)


def milliseconds(num):
    """
    Pause for this many milliseconds
    """
    seconds(num / 1000.0)


def seconds(num):
    """
    Pause for this many seconds
    """
    now = pytime.time()
    end = now + num
    until(end)


def time(num):
    """
    Same as PauseFor.seconds()
    """
    seconds(num)


def minutes(num):
    """
    Pause for this many minutes
    """
    seconds(60 * num)


def hours(num):
    """
    Pause for this many hours
    """
    minutes(60 * num)


def days(num):
    """
    Pause for this many days
    """
    hours(24 * num)


def weeks(num):
    """
    Pause for this many weeks
    """
    days(7 * num)
