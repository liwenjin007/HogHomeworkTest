import allure
import pytest

from hogwarts.pytest_HM.func.operation import Calculator

calculator = Calculator()

@allure.epic("测试计算器")
@allure.feature("测试计算器除法")
class TestDiv:
	@allure.story("整数之间的除法")
	@allure.severity(allure.severity_level.NORMAL)
	@pytest.mark.parametrize("a, b, expected", [[100, 80, "参数大小超出范围"]])
	@pytest.mark.xfail()
	def test_div_outrange(self, a, b, expected):
		result = calculator.add(a, b)
		assert result == expected