import re


class Date:
    DATA = ''
    DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, string):
        Date.DATA = string

    @classmethod
    def pars_date(cls):
        RE_DAY = re.compile(r'^\d*')
        RE_MONTH = re.compile(r'-\d*-')
        RE_YEAR = re.compile(r'-\d*$')
        day = RE_DAY.search(cls.DATA)
        month = RE_MONTH.search(cls.DATA)
        year = RE_YEAR.search(cls.DATA)
        return int(day[0]), int(month[0][1:-1]), int(year[0][1:])

    @staticmethod
    def is_date():
        try:
            if (0 < Date.pars_date()[0] <= Date.DAYS_IN_MONTH[Date.pars_date()[1]]) and Date.pars_date()[2] > 0:
                print('the date is all right')
            else:
                print('there is no such day in this month')
        except TypeError:
            print('the entered string does not match the date format')
        except KeyError:
            print('there is no such month')


a = Date('03-06-45')
a.is_date()
