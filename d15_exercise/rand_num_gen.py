from random import randrange

lower_bound = int(input("Insert the lower bound for the random number: "))
upper_bound = int(input("Insert the uper bound for the random number: "))

rand_num = randrange(lower_bound,upper_bound)

print (f"random number withn the range of {lower_bound} to {upper_bound} is: {rand_num}")
