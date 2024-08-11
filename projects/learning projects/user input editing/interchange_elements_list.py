# Python program to interchange first and last elements in a list
# Given a list, write a Python program to swap first and last element of the list.

# Examples:

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

def Interchange(new_list):
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list


new_list = []
user_input = input("Enter a number (type 'done' to finish): ")

while user_input.lower() != 'done':
    new_list.append(int(user_input))
    user_input = input("Enter another number (type 'done' to finish): ")

# new_list = [12, 35, 9, 56, 24]
print(Interchange(new_list))
