import math
import random
import string

# =============================
# Calculator Tools
# =============================

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float):
    """Divide two numbers."""
    if b == 0:
        return "Cannot divide by zero."
    return round(a / b, 2)


def square(a: float) -> float:
    """Return the square of a number."""
    return a * a


# =============================
# Student Utilities
# =============================

def calculate_percentage(marks: float, total_marks: float) -> float:
    """Calculate percentage from obtained and total marks."""
    if total_marks == 0:
        return 0
    return round((marks / total_marks) * 100, 2)


def grade_from_percentage(percent: float) -> str:
    """Convert percentage into a letter grade."""

    if percent < 0 or percent > 100:
        return "Invalid Percentage"

    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    elif percent >= 40:
        return "E"
    else:
        return "F"


def calculate_cgpa(total_points: float) -> float:
    """Convert total grade points into CGPA."""
    return round(total_points / 10, 2)


def attendance_required(current: int, total: int):
    """
    Calculate the number of consecutive classes
    required to reach 75% attendance.
    """

    if total == 0:
        return "Total classes cannot be zero."

    target = 0.75

    if current / total >= target:
        return 0

    required = math.ceil(
        (target * total - current) / (1 - target)
    )

    return required


# =============================
# Security Utility
# =============================

def generate_password(length: int) -> str:
    """Generate a secure random password."""

    chars = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    password = "".join(
        random.choice(chars)
        for _ in range(length)
    )

    return password