import argparse
import sys

import pytest

# 初始化参数构造器
# parser = argparse.ArgumentParser()
# 在参数构造中添加添加2个命令行参数
# parser.add_argument("--calmethod", type=str, default="")
# parser.add_argument("--a", type=int, default=0)
# parser.add_argument("--b", type=int, default=0)
# 获取所有命令行参数
# args = parser.parse_args()



@pytest.fixture(scope="class", autouse=True)
def get_env():
	pass



def pytest_collection_modifyitems(items):
	for i in items:
		i.name = i.name.encode("utf-8").decode("unicode_escape")
		i._nodeid=i.nodeid.encode("utf-8").decode("unicode_escape")