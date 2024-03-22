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


# Main routine goes here

yes_no = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want to see the instructions? ",
                                   yes_no)

print("You Chose:", want_instructions)

user_choice = string_checker("Choose: ", rps_list)
print("You Chose:", user_choice)
