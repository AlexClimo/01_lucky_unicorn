
# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()


        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please enter yes / no")


def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

# Main Routine goes here...
show_instructions = yes_no("Have you played the "
                           "game before?")
print("You chose {}".format(show_instructions))
print()
having_fun = yes_no("Are you having fun? ")
print("You said {} to having fun".format(having_fun))
