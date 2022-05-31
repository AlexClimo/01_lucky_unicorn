
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




if played_before == "no":
    instructions()

print("Program continues")


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
       try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if  low < response <= high:
                return response
            # output an error
            else:
                print(error)
       except ValueError:
                print(error)



# main routine goes here

how_much = num_check("Pick a number between 1-10",1,10)

print("You will be spending ${}".format(how_much))

played_before = yes_no("Have you played the "
                           "game before?")



