import json
import os
import sys
from pathlib import Path

from hogwarts.pytest_HM.conftest import global_env

path1 = Path(__file__)
data_path = Path(path1.parent.parent, "test_data")

class Utils:
	@classmethod
	def get_json_data(cls):
		current_env = global_env.get("env")
		if current_env == "dev":
			file_name = "test_data2.json"
		else:
			file_name = "test_data.json"
		with open(Path(data_path, file_name), "r", encoding="utf-8") as f:
			data = json.loads(f.read())
			return data


if __name__ == '__main__':
	data = get_json_data("test_data.json")
	print(data, type(data))
