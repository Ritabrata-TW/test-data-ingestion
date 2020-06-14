import random
import pandas as pd
from random import randrange
from datetime import datetime, timedelta


class DateTimeGenerator:

    def __init__(self, column_name, row_count):
        self.column_name = column_name
        self.row_count = row_count

    def generate(self) -> pd.DataFrame:
        data_frame = pd.DataFrame(columns=[self.column_name])

        for index in range(self.row_count):
            entry = self._generate_random_entry()
            data_frame = data_frame.append({self.column_name: entry}, ignore_index=True)

        return data_frame

    def _generate_random_entry(self):
        start_datetime = datetime.strptime('14/06/2020 1:30 PM', '%d/%m/%Y %I:%M %p')
        end_datetime = datetime.strptime('14/07/2020 4:50 AM', '%d/%m/%Y %I:%M %p')
        return self.random_date(start_datetime, end_datetime)

    @staticmethod
    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)
