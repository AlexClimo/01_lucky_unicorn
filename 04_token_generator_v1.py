import random

# main routine goes here
tokens =["unicorn", "horse", "zebra", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
#test loop to generate 20 tokens
for item in range(0,100) :
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5


print()
print("Starting balance: ${}".format(STARTING_BALANCE))
print("Final balance: ${}".format(balance))
