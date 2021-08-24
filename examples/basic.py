"""
Basic examples of how to use extractdatetime
"""

import extractdatetime as pdt

# create an instance of Constants class so we can override some of the defaults

c = pdt.Constants()

c.BirthdayEpoch = 80    # BirthdayEpoch controls how extractdatetime
                        # handles two digit years.  If the parsed
                        # value is less than this value then the year
                        # is set to 2000 + the value, otherwise
                        # it's set to 1900 + the value

# create an instance of the Calendar class and pass in our Constants
# object instead of letting it create a default

p = pdt.Calendar(c)

# parse "tomorrow" and return the result

result = p.parse("tomorrow")

# parseDate() is a helper function that bypasses all of the
# natural language stuff and just tries to parse basic dates
# but using the locale information

result = p.parseDate("4/4/80")

# parseDateText() is a helper function that tries to parse
# long-form dates using the locale information

result = p.parseDateText("March 5th, 1980")

