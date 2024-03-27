import random


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
and X(xxx) which is the exit code.

The rules are as follows:
Paper Captures Rock
Rock Crushes Scissors
Scissors Slices Paper

Good Luck, Player!
    ''')


# Check that users have entered a valid option based on a list
def int_check(question):
    while True:
        error = "Please enter an integer more than 1 or with out a decimal point."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Check that users have entered a valid
# option based on a list
def rps_compare(user, comp):
    if user == comp:
        result = "tie"

    # there are 3 ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"

    # if is not tie / win then you lose.
    else:
        result = "lose"

    return result


# Main routine starts here

# Initialize game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]


print('''
o(^▽^)o🪨📄✂️ Rock🪨 Paper📄 Scissors✂️ 🪨📄✂️o(^▽^)o
''')

# ask user for instructions
want_instructions = string_checker("Do you want to read the instructions? (Y/N)= ")

# Checks users enter yes (y) and no (n)
if want_instructions == "yes" or want_instructions == "y":
    instructions()

# Ask user for number of rounds
num_rounds = int_check("How many rounds would you like? Press <enter> to play Infinite Mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds Headings
    if mode == "infinite":
        rounds_heading = f"\n🪨📄✂️ Round {rounds_played + 1} (INFINITE MODE)🪨📄✂️"
    else:
        rounds_heading = f"\n🪨📄✂️ Round {rounds_played + 1} of {num_rounds} 🪨📄✂️"

    print(rounds_heading)
    print()

    user_choice = string_checker("Choose: ", rps_list)
    print("You Chose:", user_choice)

    # if user enters exit code, game ends.
    if user_choice == "xxx":
        print("Aw Man, Fun's Over.")
        break

    # Randomly choose from the rps list excluding the exit code. We do not want the computer giving up.
    comp_choice = random.choice(rps_list[:-1])
    print("Computer Choice:", comp_choice)

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history / Statistics area
