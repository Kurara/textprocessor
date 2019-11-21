import csv


class TextProcessor:

    def read_csv(self, file):
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['macchina'], row['modello'])