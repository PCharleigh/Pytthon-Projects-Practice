import random

guess = int(input("What is your guess?:"))

correct_number = random.randint(1,50)
guess_count = 1
  

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        print("Close! Choose a higher number.")
    else:
        print("Close! Try choosing a lower number")
    guess = int(input("What is your guess?:"))


print(f"Congrats!The right answer was {correct_number}. It took you {guess_count} guesses.")