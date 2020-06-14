import pandas as pd

from src.main.python.domain.SinkTypes import SinkTypes


class Writer:
    def __init__(self, data_frame: pd.DataFrame, write_format: SinkTypes.CSV, write_path: str):
        self.data_frame = data_frame
        self.write_format = write_format
        self.write_path = write_path

    def write(self):
        if self.write_format == SinkTypes.CSV:
            self.data_frame.to_csv(self.write_path, index=False)
