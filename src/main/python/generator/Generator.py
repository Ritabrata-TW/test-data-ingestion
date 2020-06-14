import pandas as pd

from src.main.python.generator.StringGenerator import StringGenerator
from src.main.python.generator.NumberGenerator import NumberGenerator


class Generator:

    def __init__(self, columns, row_count) -> None:
        self.columns = columns
        self.row_count = row_count

    def generate_data(self) -> pd.DataFrame:

        final_data_frame = pd.DataFrame(columns=self.columns.keys())

        for column_name, column_type in self.columns.items():
            generator = None

            if column_type == 'String':
                generator = StringGenerator(column_name, self.row_count)
            elif column_type == 'Integer':
                generator = NumberGenerator(column_name, self.row_count)

            data_frame = generator.generate()
            final_data_frame[column_name] = data_frame[column_name]

        return final_data_frame
