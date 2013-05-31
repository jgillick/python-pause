Python PauseFor
===============

Like using ``time.sleep``, but uses your computers current timestamp to track time.

For example, traditionally using ``time.sleep(3600)``, will pause the program for 60 minutes. If your computer goes into standby mode during minute one, and wakes up several hours later, your program will continue to sleep for 59 minutes.

With ``pause.seconds(3600)``, if your computer goes into standby (sleep) mode for several hours, the program will continue immediately after the machine wakes back up since the minimum amount of time has passed since the pause was started.

How it works
------------

When you create a pause, it will determine what the end time of that pause should be. Then a loop will be started that will continually check the current time against the end time. When the current time is equal or greater than the end time, the method will return and your program can resume.

Precision
---------

The precision **should** be within 0.001 of a second, however, this will depend on how precise your system sleep is and other performance factors.

This module checks the time at various intervals depending on how much time is left on the pause. If there is at least 1.5 seconds left, it will check every second. When the timer gets down to 0.1 seconds, the time will be checked every 0.001 second.

Seconds v.s. DateTime with ``until``
------------------------------------

If you pass ``pause.util`` a datetime object, the precision will only be within the closest 1 second.

Examples:
---------

Pause for 1 minute::

   import pause
   pause.minute(1)

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
