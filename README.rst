Python Pause
===============

Suspend the execution of your program for a given amount of time. This works similarly to ``time.sleep``, but uses your computers timestamp to track time, versus a counter.

For example, traditionally using ``time.sleep(3600)``, will pause the program for 60 minutes. If your computer goes into standby mode during minute one, and wakes up several hours later, your program will continue to be paused for 59 minutes.

On the other hand, with ``pause.seconds(3600)``, if your computer goes into standby mode for several hours, the program will continue immediately after the machine wakes back up since the minimum amount of time has passed since the pause was started.

How it works
------------

When you create a pause, it will determine what the end time of that pause should be. Then a loop will be started that will continually check the current time against the end time. When the current time is equal or greater than the end time, the method will allow your program can resume.

Precision
---------

The precision *should* be within 0.001 of a second, however, this will depend on how precise your system sleep is and other performance factors.

This module computes the pause duration between now and the future date, and then sleeps for half of this duration. After this time, it recomputes the new pause duration, repeating this process until the desired time is reached.

Install
-------

Download the source code and run the following command::

    sudo python ./setup.py install

Or, without downloading, install with `pip <http://www.pip-installer.org/en/latest/>`_::

     sudo pip install pause


Examples:
---------

Pause for half a second::

    import pause
    pause.milliseconds(500)

Or::

    import pause
    pause.seconds(0.5)

Pause for 1 minute::

    import pause
    pause.minutes(1)

Pause for 2 days::

    import pause
    pause.days(2)

Pause until a unix time, with millisecond precision::

    import pause
    pause.until(1370640569.7747359)

Pause using datetime::

    import pause, datetime
    dt = datetime.datetime(2013, 6, 2, 14, 36, 34, 383752)
    pause.until(dt)


Functions
---------

* days(num)
    Pause for this many days

* hours(num)
    Pause for this many hours

* milliseconds(num)
    Pause for this many milliseconds

* minutes(num)
    Pause for this many minutes

* seconds(num)
    Pause for this many seconds

* time(num)
    Same as PauseFor.seconds()

* until(time)
    Pause your program until a specific end time.
    'time' is either a unix timestamp in seconds (i.e. seconds since Unix epoch) or datetime object

* weeks(num)
    Pause for this many weeks
