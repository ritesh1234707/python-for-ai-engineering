# import random

# choice = random.choice(["heads", "tails"])

# print(choice)

''' Using "form" keyword'''

# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)


# ''' Use of random.randint'''

# import random 

# number = random.randint(1, 10)

# print(number)

''' Use of another random function called "sheffle".'''

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card) 