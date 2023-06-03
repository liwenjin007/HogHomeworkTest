import argparse
import json
import sys
from pathlib import Path

import pytest

# 初始化参数构造器
# parser = argparse.ArgumentParser()
# 在参数构造中添加添加2个命令行参数
# parser.add_argument("--calmethod", type=str, default="")
# parser.add_argument("--a", type=int, default=0)
# parser.add_argument("--b", type=int, default=0)
# 获取所有命令行参数
# args = parser.parse_args()

def pytest_addoption(parser):
	my_group = parser.getgroup("hogwarts")
	my_group.addoption(
		"--env",
		dest="env",
		default="test",
		help="setup for env"
	)

file_path = Path(__file__)
data_path = Path(file_path.parent, "test_data")

@pytest.fixture(scope="class", autouse=True)
def cmdoption(request):
	env = request.config.getoption("--env", default="test")
	if env == "test":
		file_name = "test_data.json"
	elif env == "online":
		file_name = "test_data2.json"
	return str(file_name)
	# with open(Path(data_path, file_name), "r", encoding="utf-8") as f:
	# 	data = json.loads(f.read())
	# 	return data


def pytest_collection_modifyitems(items):
	for i in items:
		i.name = i.name.encode("utf-8").decode("unicode_escape")
		i._nodeid=i.nodeid.encode("utf-8").decode("unicode_escape")