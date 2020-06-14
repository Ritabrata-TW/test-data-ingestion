import random
import string

import pandas as pd


class StringGenerator:

    def __init__(self, column_name, row_count):
        self.column_name = column_name
        self.row_count = row_count

    def generate(self) -> pd.DataFrame:
        data_frame = pd.DataFrame(columns=[self.column_name])

        for index in range(self.row_count):
            entry = self._generate_random_entry(5)
            data_frame = data_frame.append({self.column_name: entry}, ignore_index=True)

        return data_frame

    @staticmethod
    def _generate_random_entry(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
