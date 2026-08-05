# ==========================================
# Day 1 Practice Challenge
# Student Profile Manager
# ==========================================

# 1. Store student information in a dictionary
student_info = {
    "name": "Mayur Tamanke",
    "age": 22,
    "branch": "Electronics & Telecommunication",
    "college": "Sinhgad Institute of Technology and Science"
}

# 2. Store favorite programming languages in a list
favorite_languages = [
    "Python",
    "JavaScript",
    "C++",
    "Java"
]


# 3. Function to print the student profile
def print_profile(student):
    print("\n===== Student Profile =====")
    print(f"Name    : {student['name']}")
    print(f"Age     : {student['age']}")
    print(f"Branch  : {student['branch']}")
    print(f"College : {student['college']}")


# Print profile
print_profile(student_info)


# 4. Loop through all programming languages
print("\nFavorite Programming Languages:")
for index, language in enumerate(favorite_languages, start=1):
    print(f"{index}. {language}")


# 5. Class to represent a student
class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def introduce(self):
        print("\n===== Introduction =====")
        print(f"Hi, I'm {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"I study {self.branch}.")
        print("I love programming and learning Agentic AI!")


# Create Student object
student = Student("Mayur Tamanke", 22, "Electronics & Telecommunication")

# Introduce the student
student.introduce()