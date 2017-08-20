"""
numbers = [3, 1, 4, 1, 5, 9, 2]
First, write down your answers to these questions without running the code, then use Python to see if you were
correct. What values do the following expressions have?
"""
numbers = ["ten", 1, 4, 1, 5, 9, 1]
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

# TODO Get all the elements from numbers except the first two
print(numbers[2:])
# TODO Check if 9 is an element of numbers
print(9 in numbers)
