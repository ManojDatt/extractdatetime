extractdatetime
=============

Parse human-readable date/time strings.

==========
Installing
==========

You can install extractdatetime using::

    pip install git+https://github.com/ManojDatt/extractdatetime.git

===================
Using extractdatetime
===================

An example of how to use extractdatetime:


.. code:: python

    import extractdatetime
    
    cal = extractdatetime.Calendar()
    
    cal.parse("tomorrow")

To get it to a Python ``datetime`` object:


.. code:: python

    from datetime import datetime

    time_struct, parse_status = cal.parse("tomorrow")
    
    datetime(*time_struct[:6])

Parse datetime with timezone support (using pytz package):

.. code:: python

    import extractdatetime
    from datetime import datetime
    import pytz
    from pytz import timezone

    cal = extractdatetime.Calendar()

    datetime_obj, _ = cal.parseDT(datetimeString="tomorrow", tzinfo=timezone("US/Pacific"))

.. code:: python

    text = 'We will share next update by 30/01/2020 at 7:00PM.'
    time_struct, parse_status = cal.parse(text, sourceTime=datetime.now() OR ANY OTHER)
    """
    parse_status can be integer of (0-3) as:
        0 = not parsed at all
        1 = parsed as a C{date}
        2 = parsed as a C{time}
        3 = parsed as a C{datetime}
                """
    datetime(*time_struct[:6])
    Out: datetime.datetime(2020, 10, 30, 19, 0)