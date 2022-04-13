# Ask user if played before
show_instructions = input("Have you played lucky unicorn before? ").lower()

# If yes 'program continues'
if show_instructions.lower() == "yes":
    print("Program continues")
    
elif show_instructions.lower() == "y":
    print("Program continues")
    
# If no output 'display instructions'
elif show_instructions.lower() == "no":
    print("Display instructions")
    
elif show_instructions.lower() == "n":
    print("Display instructions")
    
else:
    print("Please enter yes or no")
