import pandas as pd

from src.main.python.domain.DataTypesEnum import DataTypesEnum
from src.main.python.generator.DateTimeGenerator import DateTimeGenerator
from src.main.python.generator.NumberGenerator import NumberGenerator
from src.main.python.generator.StringGenerator import StringGenerator
from src.main.python.transformers.date.DateTransformer import DateTransformer


class Generator:

    def __init__(self, columns, row_count) -> None:
        self.columns = columns
        self.row_count = row_count

    def generate_data(self) -> pd.DataFrame:

        final_data_frame = pd.DataFrame(columns=self.columns.keys())

        for column_name, column_type in self.columns.items():
            generator = None
            transformer = None

            if column_type == DataTypesEnum.String:
                transformer = None
                generator = StringGenerator(column_name, self.row_count)
            elif column_type == DataTypesEnum.Integer:
                transformer = None
                generator = NumberGenerator(column_name, self.row_count)
            elif column_type == DataTypesEnum.DateTime:
                transformer = None
                generator = DateTimeGenerator(column_name, self.row_count)
            elif column_type == DataTypesEnum.Date:
                transformer = DateTransformer(column_type)
                generator = DateTimeGenerator(column_name, self.row_count)
            elif column_type == DataTypesEnum.Time:
                transformer = DateTransformer(column_type)
                generator = DateTimeGenerator(column_name, self.row_count)
            elif column_type == DataTypesEnum.Epoch:
                transformer = DateTransformer(column_type)
                generator = DateTimeGenerator(column_name, self.row_count)

            data_frame = generator.generate()

            if transformer is not None:
                data_frame = transformer.transform(data_frame)

            final_data_frame[column_name] = data_frame[column_name]

        return final_data_frame
