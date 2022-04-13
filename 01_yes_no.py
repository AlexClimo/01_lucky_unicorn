# function goes here
def yes_no(question):
    valid = False
    while not valid:
        # ask user if played before
        response = input(question).lower().strip()

         # if yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # if no output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter yes or no")

# main routine goes here...
show_instructions = yes_no("Have you played the games before? ")
print("You chose {}".format(show_instructions))
