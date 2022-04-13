
show_instructions = ""

while show_instructions.lower() != "xxx":
    # Ask user if they hav e played before
    show_instructions = input("Have you played lucky unicorn before? ").lower()

    # if yes, output 'program continues'
    if show_instructions.lower() == "yes" or show_instructions == "y":
        print("Program continues")

    # if no output 'Display instructions'
    elif show_instructions.lower() == "no" or show_instructions == "n":
        print("Display instructions")

    else:
        print("Please enter yes or no")
