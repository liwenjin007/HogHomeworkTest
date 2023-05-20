from dataclasses import dataclass, field, asdict
from typing import List
import yaml


@dataclass
class Student:
	"""
    自己根据题目要求实现
    """
	sid: int
	name: str
	gender: str
	__grade: int = field(default=0, repr=False)

	# def __init__(self, sid, name, gender, grade):
	# 	self.sid = sid
	# 	self.name = name
	# 	self.gender = gender
	# 	self.__grade = grade

	@property
	def grade(self):
		return self.__grade

	@grade.setter
	def grade(self, score):
		if str(score).isdigit():
			self.__grade = score
		else:
			print("wrong")


class StudentList:
	def __init__(self, student_list: List[Student]):
		self.s_list = student_list

	def get(self, student_id: int):
		"""
        根据 student_id 查询信息
        """
		data = self.check_file()
		for student in data:
			if student['sid'] == student_id:
				print("查询成功")
				print(f"学生姓名{student['name']}, 性别{student['gender']}")

	def delete(self, student_id: int):
		"""
        根据 student_id 删除信息
        """
		for student in self.s_list:
			if student.sid == student_id:
				self.s_list.remove(student)
		print("删除成功")
		self.save_file()
		data = self.check_file()
		print(data)

	def update(self, student: Student):
		for i in self.s_list:
			if student.sid == i.sid:
				i.name = student.name
				i.gender = student.gender
				i.grade = student.grade
		print("更新成功")
		self.save_file()
		data = self.check_file()
		print(data)

	def save(self, student: Student):
		try:
			for i in self.s_list:
				if student.sid == i.sid:
					sid = int(student.sid) + 1
					student.sid = sid
			self.s_list.append(student)
		except Exception as e:
			print("应传student类，报错信息: ", e)
		else:
			print("保存成功")
			self.save_file()
			data = self.check_file()
			print(data)

	def save_file(self):
		student_lst = []
		for i in self.s_list:
			student_lst.append(asdict(i))
		with open("./student_info.yaml", "w", encoding="utf-8") as f:
			yaml.dump(student_lst, f, allow_unicode=True)

	def check_file(self):
		with open("./student_info.yaml", "r", encoding="utf-8") as f:
			data = yaml.safe_load(f)
		return data


if __name__ == '__main__':
	# 入参自己定义
	s1 = Student(1, "John", "male", 90)
	s2 = Student(2, "Sunny", "female", 97)
	s3 = Student(3, "Jacky", "male", 93)
	# 初始化一个成员名单
	s_list = StudentList([s1, s2, s3])
	# 实现save
	s4 = Student(4, "July", "female", 100)
	s_list.save(s4)
	# 实现update
	s4 = Student(1, "Kessy", "female", 88)
	s_list.update(s4)
	# 实现get()方法
	s_list.get(1)
	# 实现delete
	s_list.delete(1)
