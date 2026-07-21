import csv



class CSVWriter:

    @staticmethod
    def update_status(file_path,
                      employee_id,
                      status):

        rows = []

        with open(file_path,
                  "r",
                  newline="",
                  encoding="utf-8") as file:

            reader = csv.DictReader(file)

            headers = reader.fieldnames

            for row in reader:

                if row["EmployeeId"] == employee_id:

                    row["Status"] = status

                rows.append(row)

        with open(file_path,
                  "w",
                  newline="",
                  encoding="utf-8") as file:

            writer = csv.DictWriter(file,
                                    fieldnames=headers)

            writer.writeheader()

            writer.writerows(rows)