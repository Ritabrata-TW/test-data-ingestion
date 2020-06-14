import sys

from src.main.python.api.Ingestor import Ingestor


def main():
    ingestor = Ingestor()

    ingestor.add_column("Subject", "String")
    ingestor.add_column("Marks", "Integer")

    data_frame = ingestor.generate_data(1000)
    print(data_frame.head())


if __name__ == '__main__':
    main()
