"""
Python Program to Swap Two Elements in a List
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

Examples:
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""


class IntegerInputHandler:
    #   Provides functions to collect integers, print their indexes, and change the positions of elements in the list.

    def __init__(self):
        # Initiate empty list
        self.numbers = []

    def get_integers(self):
        # Prompts users for valid integers and stores them in a list and returns them.
        while True:
            user_input = input("Enter an integer (or 'q' or 'quit' to exit): ")

            # Check for quit commands (case-insensitive) before conversion
            if user_input.lower() in ("q", "quit"):
                break  # Exit the loop immediately if user enters a quit command

            try:
                # Convert to integer only if user_input is not a quit command
                user_input = int(user_input)
                self.numbers.append(user_input)
            except ValueError:
                # Handle invalid input (non-integer)
                print("Invalid input. Please enter an integer.")

        return self.numbers

    def change_positions(self, from_pos, to_pos):
        # Changes the position of an element in the list.
        if from_pos < 0 or from_pos >= len(self.numbers):
            raise IndexError("from_pos is out of range")
        if to_pos < 0 or to_pos >= len(self.numbers):
            raise IndexError("to_pos is out of range")
        if from_pos == to_pos:
            raise ValueError("from_pos and to_pos cannot be the same index")

        # Swap elements using temporary storage
        temp = self.numbers[from_pos]
        self.numbers[from_pos] = self.numbers[to_pos]
        self.numbers[to_pos] = temp

    def print_indexes(self):
        # Prints the current list and its indexes for reference.
        if not self.numbers:
            print("No elements in the list yet.")
            return
        for i, num in enumerate(self.numbers):
            print(f"Index: {i}, Value: {num}")

    def run(self):
        # Main function to initiate the interaction with the user.
        collected_numbers = self.get_integers()
        print("Original list:", collected_numbers)

        self.print_indexes()

        while True:
            try:
                from_pos = int(
                    input("Enter the index of the element to move (from): "))
                to_pos = int(
                    input("Enter the new index for the element (to): "))
                self.change_positions(from_pos, to_pos)
                print("Modified list:", self.numbers)
                break
            except (IndexError, ValueError) as e:
                print("Error:", e)


# Example usage (all functionality within the class)
integer_handler = IntegerInputHandler()
integer_handler.run()
