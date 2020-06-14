import pandas as pd

from src.main.python.domain.Column import Column
from src.main.python.domain.DataTypesEnum import DataTypesEnum
from src.main.python.domain.SinkTypes import SinkTypes
from src.main.python.generator.Generator import Generator
from src.main.python.writer.Writer import Writer


class Ingestor:

    def __init__(self) -> None:
        self.columns = {}
        self.data_frame = pd.DataFrame()
        self.sink_file_path = None

    def add_column(self, column: Column):
        self.columns[column.name] = column.datatype

    def get_columns(self):
        return self.columns

    def generate_data(self, row_count):
        generator = Generator(self.columns, row_count)
        self.data_frame = generator.generate_data()

    def add_sink_filepath(self, filepath: str):
        self.sink_file_path = filepath

    def write_data(self):
        writer = Writer(self.data_frame, SinkTypes.CSV, self.sink_file_path)
        writer.write()
