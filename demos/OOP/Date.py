class Date:
    def __init__(self, day=0, month=0, year=0):
        self._day = day
        self._month = month
        self._year = year

    def def__str__(self):
        return "%02d/%02d/%d" % (
            self._day, self._month, self._year)

    def __add__(self, value):
        retn = Date(self._day, self._month, self._year)
        retn._day = retn._day + value
        retn._validate_date

        return retn


today = Date(9, 10, 2015)
print(today)
tomorrow = today + 1
print(tomorrow)