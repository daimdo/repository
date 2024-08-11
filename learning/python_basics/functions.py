# A function is a named sequence of statements that performs a computation. When you define a function, you specify the name and the sequence of statements.
print(max("Hello"))
print(min(1, 2, 3))
print(len("Have a great day!"))
print(float("500.50"))
print(int(2.90))
print(str(200))

# Math module
# Python has a math module that provides most of the familiar mathematical functions. Before we can use the module, we have to import it:
import math

print(math)
# The module object contains the functions and variables defined in the module. To access one of the functions, you have to specify the name
# of the module and the name of the function, separated by a dot also known as a period (dot notation).
number_log = 10 * math.log10(10)
number_sin = math.sin(0.7)
number_pi = math.pi
number_sqrt = math.sqrt(2)

# Random module
# The random module provides functions that generate pseudorandom numbers. The function random returns a random float between 0.0 and 1.0
import random

for i in range(2):
    x = random.random()
    print(x)

print(random.randint(5, 10))


# Adding new functions
# A function definition specifies the name of a new function and the sequence of statements that execute when the function is called, which can be reused throughout the program.
# def is a keyword that indicates that this is a function definition. The name of the function is print_sentences.
# The parentheses after the name indicate that this function can take arguments.
def add_values(a, b):
    added = a + b
    return added


x = add_values(3, 5)
print(x)
# Within the function, the parameters a and b were arguments 3 and 5. The function computed the sum of the two numbers and placed it in the local function variable named added.
# Then it used the return statement to send the computed value back to the calling code as the function result, which was assigned to the variable x and printed out.
