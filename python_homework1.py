from typing import List


class Student:
	"""
    自己根据题目要求实现
    """

	def __init__(self, student_id, student_name, student_gender):
		self.student_id = student_id
		self.student_name = student_name
		self.student_gender = student_gender


class StudentList:
	def __init__(self, student_list):
		self.s_list = student_list

	def get(self, student_id: int):
		"""
			根据 student_id 查询信息
		"""
		for student in self.s_list:
			if student_id == student.student_id:
				print("查询的学生是: ")
				print(student.__dict__)
				break
		else:
			print("查无此人")

	def delete(self, student_id: int):
		"""
			根据 student_id 删除信息
		"""
		for student in self.s_list:
			if student_id == student.student_id:
				self.s_list.remove(student)
				print("删除的学生是: ")
				print(student.__dict__)
				break
		else:
			print("查无此人")
		print("剩余学生是: ")
		for student in self.s_list:
			print(student.__dict__)


if __name__ == '__main__':
	# 入参自己定义
	s1 = Student(1, "John", "male")
	s2 = Student(2, "Sunny", "female")
	s3 = Student(3, "Jacky", "male")
	# 初始化一个成员名单
	s_list = StudentList([s1, s2, s3])
	# 实现get()方法
	s_list.get(3)
	# 实现delete
	s_list.delete(1)
