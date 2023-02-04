# Implement a function csv2json(). The function receives a file_path of csv file and file_path of a new json file
# that will be created by a function. The function should read x§the original csv file, convert the data in it
# into json, and store the contents of the csv file as a json file that contains a list of objects. For example,
# for this csv file the result should be like this json file
import csv
import json


def csv2json(csv_path: str, json_path: str) -> None:
    with open(csv_path, "r") as f:
        csv_reader = csv.DictReader(f)
        my_list_of_dicts = list(csv_reader)
    with open(json_path, "w") as f:
        json.dump(my_list_of_dicts, f)


if __name__ == '__main__':
    my_csv_path = "data/data.csv"
    my_json_path = "data/result.json"
    csv2json(my_csv_path, my_json_path)

