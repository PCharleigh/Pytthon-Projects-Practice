import random
import random

# print(random.randint(1,10))

# print(random.random())
# mylist = "yes", "no", "maybe"


# print(input("What is your question?"))
# print(random.choice(mylist))

lucky_number = random.randint(1,100)

Mylist = "You will get married this year!", "You're going to win the lottery.", "Someone has a crush on you.", "You will have a bad day today.", "Someone will compliment you today!"

print(f'{random.choice(Mylist)}: {lucky_number}')