txtinput = "12312"

for i, a in enumerate(txtinput):
    # Print character and index within loop
    print(f"Character: {a} , Index: {i}")

middle_index = len(txtinput) // 2  # Integer division for floor

if len(txtinput) % 2 == 0:  # Check for even-length string (no middle character)
    print("The string has an even number of characters, no middle character.")
else:
    middle_char = txtinput[middle_index]
    beginning = txtinput[:middle_index]
    ending = txtinput[middle_index + 1 :]
    if beginning == ending:
        equal = "equal"
    else:
        equal = "not equal"
    print(
        f"The middle of this string is character '{middle_char}' (index {middle_index}). The beginning of the string is : {beginning}, the ending of the string is {ending}. This makes them {equal}."
    )
