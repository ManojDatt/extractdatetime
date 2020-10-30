extractdatetime
=============

Parse human-readable date/time strings.

==========
Installing
==========

You can install extractdatetime using::

    pip install extractdatetime

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
    import pytz
    from pytz import timezone

    cal = extractdatetime.Calendar()

    datetime_obj, _ = cal.parseDT(datetimeString="tomorrow", tzinfo=timezone("US/Pacific"))

