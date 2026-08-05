# def add(a,b):
#     return a + b
# result = add(23,94)
# print(result)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


student =Student("Mayur", 22)
student.greet()