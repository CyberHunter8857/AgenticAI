"""
number = int(input("Enter a Number:"))
print(100/number)
"""

try:
    number = int(input("Enter a Number:"))
    result = 100/number
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
# except Exception as e:
#     print(f"Error: {e}")
