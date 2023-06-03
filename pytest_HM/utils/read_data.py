import json
import os
import sys
from pathlib import Path


path1 = Path(__file__)
data_path = Path(path1.parent.parent, "test_data")


def get_json_data(file_name):
	with open(Path(data_path, file_name), "r", encoding="utf-8") as f:
		data = json.loads(f.read())
		return data


if __name__ == '__main__':
	data = get_json_data("test_data.json")
	# print(data, type(data))
	print([data["expected_add_result"]["integar_inrange"]])