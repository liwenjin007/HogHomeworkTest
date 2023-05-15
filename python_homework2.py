from dataclasses import dataclass, field, asdict
from typing import List


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

	# def __str__(self):
	# 	return f"学生学号{self.sid},姓名是{self.name},性别是{self.gender},成绩是{self.__grade}"


class StudentList:
	def __init__(self, student_list: List[Student]):
		self.s_list = student_list

	def __str__(self):
		return f"目前学生列表为：{self.s_list}"

	def get(self, student_id: int):
		"""
        根据 student_id 查询信息
        """
		for student in self.s_list:
			if student.sid == student_id:
				# print('查询的学生是: ', asdict(student))
				print("查询：", student)
		# print(self.s_list)

	def delete(self, student_id: int):
		"""
        根据 student_id 删除信息
        """
		for student in self.s_list:
			if student.sid == student_id:
				self.s_list.remove(student)
		# print("删除后剩余的学生列表: ", self.s_list)
		print(self.s_list)

	def update(self, student: Student):
		for i in self.s_list:
			if student.sid == i.sid:
				i.name = student.name
				i.gender = student.gender
				i.grade = student.grade
		# print("更新后学生列表:", self.s_list)
		print(self.s_list)

	def save(self, student: Student):
		for i in self.s_list:
			if student.sid == i.sid:
				sid = int(student.sid) + 1
				student.sid = sid
		self.s_list.append(student)
		# print("新增的学生是: ", asdict(student))
		print("新增：",student)


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
	s_list.delete(2)
