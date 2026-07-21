import csv


class CSVReader:

    @staticmethod
    def read_csv(file_path: str):

        rows = []

        with open(file_path,
                  mode="r",
                  newline="",
                  encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:
                rows.append(row)

        return rows