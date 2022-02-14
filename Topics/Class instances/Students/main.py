# create attribute:
class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = name[0] + last_name + str(birth_year)

new_student = Student(input(), input(), input())

print(new_student.student_id)

# # can create method too:
# class Student:
#
#     def __init__(self, name, last_name, birth_year):
#         self.name = name
#         self.last_name = last_name
#         self.birth_year = birth_year
#
#     def student_id(self):
#         print(self.name[0] + self.last_name + str(self.birth_year))
#
# new_student = Student(input(), input(), input())
#
# new_student.student_id()

