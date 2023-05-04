import datetime
import time


class Coffee:
	def __init__(self, name: str, price: int, ingredient: str):
		self.name = name
		self.price = price
		self.ingredient = ingredient

	def __str__(self):
		return f"{self.name}({self.price}元): {self.ingredient}"


class Latte(Coffee):
	def __init__(self):
		super().__init__("拿铁", 20, "浓缩咖啡，牛奶，糖")


class Americano(Coffee):
	def __init__(self):
		super().__init__("美式", 15, "浓缩咖啡")


class CoffeeMachie:
	def __init__(self):
		self.products = [Latte(), Americano()]
		self.records = []
		self.money = 0

	def display(self):
		print(" 展示咖啡 ".center(20, "-"))
		for coffee in self.products:
			print(coffee)

	def select_coffee(self) -> Coffee:
		print(" 选择咖啡 ".center(20, "-"))
		while True:
			selected = input("请输入数字选择咖啡 0:拿铁，1:美式\n")
			if selected in ('0', '1'):
				return self.products[int(selected)]
			else:
				print("输入不合法，请重新选择可选的咖啡")
				continue

	def input_money(self, select_coffee: Coffee):
		while True:
			if int(self.money) < int(select_coffee.price):
				print(" 投入钱币 ".center(20, "-"))
				coffee_money = input(f"请投入{select_coffee.price}元\n")
				self.money = self.money + int(coffee_money)
				continue
			else:
				return int(self.money)

	def make_coffee(self, select_coffee: Coffee, money: int):
		print(" 制作咖啡 ".center(20, "-"))
		print("咖啡制作中，请稍后......")
		time.sleep(1)
		now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print(f"{select_coffee.name}☕制作完成! ")
		self.money = money - select_coffee.price
		record = f"{now} 订单：{select_coffee.name}, 支付{money}元, 找零{self.money}元"
		self.records.append(record)

	def print_records(self):
		print(" 打印记录 ".center(20, "-"))
		for i in self.records:
			print(i)


if __name__ == '__main__':
	machine = CoffeeMachie()
	while True:
		machine.display()
		select_coffee = machine.select_coffee()
		input_money = machine.input_money(select_coffee)
		machine.make_coffee(select_coffee, input_money)
		is_continue = input("是否继续购买？Y:是，N:否\n")
		if is_continue.upper() == "Y":
			continue
		else:
			break
	machine.print_records()