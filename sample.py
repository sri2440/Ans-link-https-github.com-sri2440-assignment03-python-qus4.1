import re

phone_number_pattern = re.compile(r'^\+\d{1,4}-\d{1,10}$')

# Test with multiple phone numbers
valid_numbers = ['+123-4567890', '+1-1234567890', '+9999-9876543210']
invalid_numbers = ['123-4567890', '+1-12345', '+123-45678901', '+1-abc123456']

print("Valid Phone Numbers:")
for number in valid_numbers:
    if phone_number_pattern.match(number):
        print(number)

print("\nInvalid Phone Numbers:")
for number in invalid_numbers:
    if not phone_number_pattern.match(number):
        print(number)
