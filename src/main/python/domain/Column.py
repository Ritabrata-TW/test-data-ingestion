from src.main.python.domain.DataTypesEnum import DataTypesEnum


class Column:
    def __init__(self, name: str, datatype: DataTypesEnum):
        self.name = name
        self.datatype = datatype
