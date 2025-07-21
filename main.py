# assignment 4
import string_operations as so

sample_string = "National Anthem by Lana Del Ray"
print("Original:", sample_string)
print("Reversed:", so.reverse_string(sample_string))
print("Capitalized:", so.capitalize_string(sample_string))
print("Lowercase:", so.lowercase_string(sample_string))
print("Uppercase:", so.uppercase_string(sample_string))

# assignment 5
from utilities.calculator import add, subtract , multiply, divide
from utilities.string_operations import reverse_string, capitalize_string, lowercase_string, uppercase_string

print("Using calculator.py:")
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))
