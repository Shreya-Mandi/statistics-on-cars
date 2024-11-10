import numpy as np
import random
import pandas as pd
from random import randrange
from datetime import timedelta
from datetime import datetime

# all dates in the format %m/%d/%Y
# all car purchase lie between '1/1/2008' and today

class Dates:
    def __init__(self, num):
        np.random.seed(1)
        random.seed(1)
        self.num = num
        self.count=0
        self.day=datetime.now().strftime('%m/%d/%Y')
        self.dates=self.gen_dates()

    def random_date(self, start, end):
        if isinstance(start, str):
            start = datetime.strptime(start, '%m/%d/%Y')
        if isinstance(end, str):
            end = datetime.strptime(end, '%m/%d/%Y')

        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    def gen_start(self):
        start = datetime.strptime('1/1/2008', '%m/%d/%Y')
        self.start_date=self.random_date(start, self.day)
        return self.start_date

    def gen_end(self):
        retired = np.random.choice(["true", "false"], p=[0.1, 0.9])
        self.end_date = self.random_date(self.start_date, self.day) if retired == "true" else None
        return self.end_date

    def gen_dates(self):
        dates_start=[]
        dates_end=[]
        for i in range(self.num):

            start_date=self.gen_start()
            end_date=self.gen_end()
            dates_start.append(start_date)
            dates_end.append(end_date)

        dates = pd.DataFrame({
            'start':dates_start,
            'end':dates_end
        })
        return dates

    def gen_csv(self, filename):
        self.dates.to_csv(f"{filename}.csv", index=True)

    def __iter__(self):
        self.count=0
        return self

    def __next__(self):
        x = self.profiles.loc[self.count]

        self.count+=1
        return x

if __name__ == '__main__':
    dates=Dates(100)
    dates.gen_csv("dates")
    iter_dates = iter(dates)

    # # iteration example
    # for i in range(dates.num):
    #     print(next(iter_dates))