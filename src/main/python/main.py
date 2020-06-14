import sys

from src.main.python.api.Ingestor import Ingestor


def main():
    ingestor = Ingestor()

    ingestor.add_column("Subject", "String")
    ingestor.add_column("Marks", "Integer")

    ingestor.generate_data(1000)

    ingestor.add_sink_filepath("/Users/ritabrata/Projects/Open_Source/test_data_ingest/out/output_file.csv")
    ingestor.write_data()


if __name__ == '__main__':
    main()
