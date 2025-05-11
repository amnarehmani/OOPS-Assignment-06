# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        super().__init__(message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError()
    else:
        print("Access granted.")

try:
    check_age(16)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
