import pytest
import allure

from hogwarts.pytest_HM.func.operation import Calculator
from hogwarts.pytest_HM.utils.read_data import get_json_data

Skip = ""
calculator = Calculator()


def read_data(filename, key_word_a, key_word_b, key_word_expected):
	data = []
	integar_a = get_json_data(filename)[key_word_a]
	integar_b = get_json_data(filename)[key_word_b]
	expected_integar = get_json_data(filename)["expected_add_result"][key_word_expected]
	for i in range(5):
		data.append([integar_a[i], integar_b[i], expected_integar[i]])
	return data



@allure.epic("测试计算器")
@allure.feature("测试计算器加法")
@pytest.mark.skipif(Skip=="Add", reason="命令行执行跳过case")
class TestAdd():
	@allure.story("整数之间的加法")
	@allure.severity(allure.severity_level.CRITICAL)
	@pytest.mark.parametrize("a,b,expected", read_data("test_data.json", "integar_inrange", "integar_inrange", "integar_inrange"))
	def test_integar_add(self, a, b, expected):
		result = calculator.add(a, b)
		assert result == expected