import csv

from parser_model import PostModelFull


def extract_data_from_csv(to_type: str = 'dict'):
    with open('posts2.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                if to_type == 'dict':
                    yield PostModelFull.parse_csv_to_dict(row)
                elif to_type == 'tuple':
                    yield PostModelFull.parse_csv_to_tuple(row)
            except Exception as ex:
                pass
