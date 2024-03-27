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


# Main routine starts here

# Initialize game variables
mode = "regular"
rounds_played = 0


print('''
o(^▽^)o🪨📄✂️ Rock🪨 Paper📄 Scissors✂️ 🪨📄✂️o(^▽^)o
''')

# Instructions

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

    user_choice = input("Choose: ")

    # if user enters exit code, game ends.
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history / Statistics area
