# A boolean expression is an expression that is either true or false.
print(1 == 2)
print("car" == "car")
print(type(True))
# Other comparison operators are:
# x != y        x is not equal to y
# x > y         x is greater than y
# x < y         x is less than y
# x >= y        x is greater than or equal to y
# x <= y        x is less than or equal to y
# x is y        x is the same as y
# x is not y    x is not the same as y

# If statement
# To write useful programs, the ability to check conditions and change the behavior of the program is crucial.
# Conditional statements give us this ability. The simplest form is the if statement.
x = 20
if x > 0:
    print("x is positive")

# A second form of the if statement is alternative execution, in which there are two possibilities and the condition determines which one gets executed.
# Since the condition must either be true or false, exactly one of the alternatives will be executed. The alternatives are called branches in the flow of execution.
y = 25
if y < 25:
    print("The number is smaller than 25")
else:
    print("The number is greater than 24")

# Sometimes there are more than two possibilities and more branches are needed. One way to express a computation like that is a chained conditional.
# elif is an abbreviation of “else if.” Exactly one branch will be executed.
if x < y and x < 25:
    print("x is smaller than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y are equal")

# Try / except
# Try / except conditional execution structure to handle expected and unexpected errors. Python starts by executing the sequence of statements in the try block.
# If successfully executed, it skips the except block and proceeds. If an exception occurs in the try block, Python executes the statements in the except block.
user_input = input("Insert a decimal number.\n")
try:
    number = float(user_input)
    result = (number * 2) + number
    print(result)
except:
    print("Error! Please enter a number. Thank you!")
