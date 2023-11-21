import re

class MyClass:
    def __init__(self, email):
        self.email = self.validate(email)

    @staticmethod
    def validate(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        return email

# Example usage:
try:
    instance = MyClass("invalid-email")
except ValueError as e:
    print(f"Error: {e}")

try:
    instance = MyClass("valid@email.com")
    print(f"Valid email: {instance.email}")
except ValueError as e:
    print(f"Error: {e}")