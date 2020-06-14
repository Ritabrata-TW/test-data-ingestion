from src.main.python.generator.Generator import Generator


class Ingestor:

    def __init__(self) -> None:
        self.columns = {}

    def add_column(self, column_name: str, column_type: str):
        self.columns[column_name] = column_type

    def get_columns(self):
        return self.columns

    def generate_data(self, row_count):
        generator = Generator(self.columns, row_count)
        data_frame = generator.generate_data()
        return data_frame
