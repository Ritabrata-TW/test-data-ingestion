from src.main.python.api.Ingestor import Ingestor
from src.main.python.domain.DataTypesEnum import DataTypesEnum


def main():
    print("Start ingest flow.... Creating ingestor object....")
    ingestor = Ingestor()

    ingestor.add_column("Subject", DataTypesEnum.String)
    ingestor.add_column("Marks", DataTypesEnum.Integer)
    print("Added columns to ingestor....")

    ingestor.generate_data(1000)
    print("Generated data....")

    ingestor.add_sink_filepath("/Users/ritabrata/Projects/Open_Source/test_data_ingest/out/output_file.csv")
    ingestor.write_data()
    print("Done writing data to sink....")

    print()


if __name__ == '__main__':
    main()
