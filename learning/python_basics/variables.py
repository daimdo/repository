# A value is one of the basic things a program works with, like a letter or a number.
print(1)
print("Hello")

# If you are not sure what type a value has, the interpreter can tell you.
print(type(1))
print(type("Hello"))

# A variable is a name that refers to a value. An assignment statement creates new variables and gives them values:
words = "Hello, how are you?"
numbers = 12345
# A statement is a unit of code that the Python interpreter can execute. We have seen two kinds of statements: print being an expression statement and assignment.

# Python reserves 35 keywords, so these cannot be variable names:
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# Operators are special symbols that represent computations like addition and multiplication. The values the operator is applied to are called operands.
# An expression is a combination of values, variables, and operators.
print((numbers * 2) / numbers)
quotient = 7 // 3
print(quotient)
remainder = 7 % 3
print(remainder)

# In string operations, the + operator performs concatenation. The * operator multiplies the content of a string by an integer.
first_number = 10
second_number = 15
print(first_number + second_number)
first_string = "100"
second_string = "150"
print(first_string + second_string)

# Getting user input and storing it in a variable stops the program and waits for the user to type something. When the user presses Return or Enter,
# the program resumes and input returns what the user typed as a string.
# Wrap it in a try / except conditional execution structure to make it error proof. More on this in conditionals.py
user_input = int(input("Insert a number you want to multiply by 5\n"))
print(user_input * 5)
