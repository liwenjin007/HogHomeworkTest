import pytest
import allure

from hogwarts.pytest_HM.func.operation import Calculator
from hogwarts.pytest_HM.utils.read_data import Utils


def get_data(level):
	json_data = Utils.get_json_data()
	print(json_data)
	return json_data[level]

@allure.epic("测试计算器")
@allure.feature("测试计算器加法")
class TestAdd():

	def setup_class(self):
		self.calculator = Calculator()

	@allure.story("整数之间的加法")
	@allure.severity(allure.severity_level.CRITICAL)
	@pytest.mark.parametrize("a,b,expected", get_data("P0"))
	def test_integar_add(self, a, b, expected):
		result = self.calculator.add(a, b)
		assert result == expected

	@allure.story("a/b超出范围")
	@allure.severity(allure.severity_level.CRITICAL)
	@pytest.mark.parametrize("a,b,expected", get_data("P1"))
	def test_outrange_add(self, a, b, expected):
		result = self.calculator.add(a, b)
		assert result == expected

	@allure.story("非数字")
	@allure.severity(allure.severity_level.NORMAL)
	@pytest.mark.parametrize("a,b,expected", get_data("P2"))
	def test_non_number_add(self, a, b, expected):
		with pytest.raises(eval(expected)) as e:
			result = self.calculator.add(a, b)
			assert e.type == TypeError


