import pandas as pd

from src.main.python.domain.DataTypesEnum import DataTypesEnum


class DateTransformer:
    def __init__(self, target_type: DataTypesEnum):
        self.target_type = target_type

    def transform(self, data_frame: pd.DataFrame):
        column_name = data_frame.columns[0]

        if self.target_type == DataTypesEnum.DateTime:
            pass
        elif self.target_type == DataTypesEnum.Date:
            data_frame[column_name] = data_frame[column_name].dt.date
        elif self.target_type == DataTypesEnum.Time:
            data_frame[column_name] = data_frame[column_name].dt.time
        elif self.target_type == DataTypesEnum.Epoch:
            data_frame[column_name] = data_frame[column_name].apply(lambda datetime: datetime.timestamp() * 1000)

        return data_frame
