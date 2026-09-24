from datetime import datetime
import random
import string

# Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# BMI Calculator
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# Age Calculator
def calculate_age(year, month, day):
    dob = datetime(year, month, day)
    today = datetime.today()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age

# KM to Miles
def km_to_miles(km):
    return round(km * 0.621371, 3)

# Password Generator
def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(length))
    return password