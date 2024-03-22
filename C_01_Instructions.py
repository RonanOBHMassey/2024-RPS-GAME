# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if response is a word in the list
            if item == user_response:
                return item

            # check if user response iss the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if something is invalid
        print(error)
        print()


# display instructions to the user
def instructions():
    print('''
**** INSTRUCTIONS ****

To begin, choose a number of rounds 
                or 
press enter to choose infinite mode.

Then you play against the computer.
You need to pick between: 
R (rock), P (paper) and S (scissors)

The rules are as follows:
Paper Captures Rock
Rock Crushes Scissors
Scissors Slices Paper

Good Luck, Player!
    ''')


# Main Routine
print('''
o(^▽^)o🪨📄✂️ Rock🪨 Paper📄 Scissors✂️ 🪨📄✂️o(^▽^)o
''')


# Loop for testing purposes.


want_instructions = string_checker("Do you want to read the instructions? (Y/N)= ")

# Checks users enter yes (y) and no (n)
if want_instructions == "yes" or want_instructions == "y":
    instructions()

print("program continuing")
