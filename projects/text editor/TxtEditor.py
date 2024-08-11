# Module to interact with operating system (listing files in current directory)
import os
# Module for working with regular expressions (text insights like count numbers, sentences and such)
import re

# Initializing variable and entering while loop that continues until file is found and read, or created
file_found = False

while not file_found:
    user_read_create = input("Read from an existing .txt file (R) or create a new .txt file (C): ")
    # Read if there are existing files in directory
    if user_read_create.upper() == "R":
        file_list = [f for f in os.listdir(".") if f.endswith(".txt")]
        if len(file_list) == 0:
            print("There are no files found in your current directory")
            continue
        print("Available files: ")
        for i, filename in enumerate(file_list):
            print(f"{i+1}. {filename}")
        # Let user choose which file to read
        user_numb_chosen = int(input("Enter the number of the file you want to read: "))
        while user_numb_chosen <1 or user_numb_chosen > len(file_list):
            user_numb_chosen = int(input(f"Out of range. Enter a number between 1 and {len(file_list)}: "))
        filename = file_list[user_numb_chosen-1]
        with open(filename, "r") as file:
            text = file.read()
        file_found = True

    # Create new ".txt" file in user directory. Check if filename ends with .txt and existence in user directory
    elif user_read_create.upper() == "C": 
        while True:
            filename = input("Enter name of your new file and end with '.txt': ")
            if not filename.endswith(".txt"):
                print("Please type a filename that ends with '.txt' (E.g. 'example.txt')")
                continue
            if os.path.exists(filename):
                print(f"File '{filename}' already exists, use another filename.")
                file_overwrite = input("Do you want to overwrite the file? Yes (Y) or No (N)? ")
                if file_overwrite.upper() != "Y":
                    continue
            break
        # Let user input text, store in one or more lines and write to file
        text = ""
        line_num = 1
        while True:
            new_text = input(f"Type text to line {line_num} or don't and press Enter to finish: ")
            if new_text == "":
                break
            text += new_text + "\n"
            line_num += 1
        with open(filename, "w") as file:
            file.write(text)
        file_found = True
    else:
        print("Please type either letter 'R' (read file) or 'C' (create file): ")

# Print contents of file user created or read
print("File contents:\n")
print(text)
# Allow user to make changes in .txt file through enabling replacement of characters

# Track total occurrences replaced
total_occurrences_replaced = 0  

while True:
    replacement_text = input("\nEnter the word(s)/character(s) to replace (or type 'exit' to save and exit): ")
    # If user types "exit", exit the program and save modified text to the file
    if replacement_text == "exit":
        with open(filename, 'w') as file:
            file.write(text)
        print("\nText saved. Exiting program.")
        break
    # If user entered non-existing text, inform and continue prompting for existing characters to replace
    else:
        if replacement_text not in text:
            print(f"'{replacement_text}' not existing in your file.")
            continue
        # Prompt user to enter replacement text
        replace_with = input("Enter replacement text: ")

        # Count number of occurrences of replacement text
        occurrences = text.count(replacement_text)
        # If replacement text exists once, replace with replacement word and print modified text
        if occurrences == 1:
            text = text.replace(replacement_text, replace_with)
            print("\nModified text:\n")
            print(text)
            print(f"Replaced {occurrences} occurrence of '{replacement_text}'.")
            total_occurrences_replaced += occurrences
        else:
            # If more than one occurrence of word to replace, ask user if they want to replace all occurrences
            replace_all = input("Replace all occurrences? Yes (Y) or no (N): ")
            # Replace all occurrences of word and print modified text
            if replace_all.upper() == "Y":
                text = text.replace(replacement_text, replace_with)
                print("\nModified text:\n")
                print(text)
                print(f"Replaced {occurrences} occurrences of '{replacement_text}'.")
                total_occurrences_replaced += occurrences
            elif replace_all.upper() =="N":
            # else:
                # Replace a specific occurrence, ask user which line and which occurrence to replace
                line_num = int(input("Which line to replace? (1-based index): "))
                lines = text.split('\n')
                # If user entered valid line number, retrieve line and check if word exists in line
                if line_num > 0 and line_num <= len(lines):
                    line = lines[line_num-1]
                    if replacement_text not in line:
                        print(f"'{replacement_text}' is not known in line {line_num}.")
                        continue
                    # If replacement word exists in line, count number of occurrences of word to replace in line and ask user which occurrence to replace
                    occurrences = line.count(replacement_text)
                    occurrence_num = int(input(f"Which occurrence to replace? (1-based index, total {occurrences}): "))
                    # Find  start and end indices of the occurrence of word to replace and replace with replacement word
                    start = 0
                    for i in range(occurrence_num):
                        start = line.find(replacement_text, start) + 1
                    end = start + len(replacement_text)
                    new_line = line[:start-1] + replace_with + line[end-1:]
                    lines[line_num-1] = new_line
                    text = '\n'.join(lines)
                    print("\nModified text:\n")
                    print(text)                                                     
                    print(f"Replaced {occurrences} occurrences of '{replacement_text}' in line {line_num}.")
                    total_occurrences_replaced += occurrences
                else:
                    # If user entered invalid line number, inform user
                    print("Invalid line number. Please check again.")
            else:
                print("Please type either yes (Y) or no (N).")
                continue

# Print insights
num_chars = len(text)
num_sentences = len(re.findall(r'[.!?]+', text))
num_words = len(re.findall(r'\b\w+\b', text))
num_lines = len(text.split('\n'))-1
print(f"\nText file insights for {filename}:")
print(f"Number of characters: {num_chars}")
print(f"Number of sentences: {num_sentences}")
print(f"Number of words: {num_words}")
print(f"Number of lines: {num_lines}")
print(f"Total occurrences replaced: {total_occurrences_replaced}")