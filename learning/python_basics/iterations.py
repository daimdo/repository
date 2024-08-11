# Updating variables
# Common pattern in assignment statements is an assignment statement that updates a variable, where the new value of the variable depends on the old, initialized value.
x = 1
x = x + 1

# While statement
# Evaluate the condition, yielding True or False.
# If the condition is false, exit the while statement and continue execution at the next statement.
# If the condition is true, execute the body and then go back to step 1.
# The body of the loop should change the value of one or more variables so that eventually the condition becomes false and the loop terminates.
# The variable that changes each time the loop executes and controls when the loop finishes is the iteration variable.
# If there is no iteration variable, the loop will repeat forever, resulting in an infinite loop.
# Break leaves a loop, continue jumps to the next iteration.
# The while statement is an indefinite loop; it loops until some condition becomes False

i = 0
while True:
    if i == 5:
        # Break the loop if i reaches 5
        break
    elif i % 2 == 0:
        # Skip even numbers and continue to the next iteration
        i += 1
        continue
    else:
        # Print only odd numbers less than 5
        print(i)
    i += 1

# For loop
# Construct a definite loop using a for statement when there is a list of things to loop through.
# The for loop is looping through a known set of items so it runs through as many iterations as there are items in the set.

fruits = ["Apple", "Banana", "Pear"]
for fruit in fruits:
    print(f"This {fruit} is tasty!")
print("Vitamin C!")
