import calendar


class Time_Mana:
    def __init__(self, year, month):
        self.year = 2019
        self.month = 11

    def print_cal(self):
        print(calendar.month(self.year, self.month))

    def print_time(self):
        print('Year = ', self.year)


