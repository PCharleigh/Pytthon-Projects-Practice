print("=== Affirmation Generator ===")
name = input("What is your name?")
print(f"Nice to meet you {name}")
know = input("Would you mind telling me a little more about yourself?")
if know == "no":
  print("Great! Thank you.")
  food = input("What is your favorite food?")
  print(f"{food} sounds tasty!")
  game = input("Do you like video games?")
  if game == "yes":
    print("Awesome! I like video games too.")
    favorite_game = input("What is your favorite game?")
    if favorite_game == "mario kart":
      print("That's a fun game. Very competative but full of excitement too.")
    elif favorite_game == "mario party":
      print("That's a great game for family time. Until someone steals a star from you.")
    elif favorite_game == "pokemon":
      print("That game takes a lot of time and dedication when playing. Very fun game all around.")
    elif favorite_game == "card game":
      print("Card games have great variation for big crowds and small crowds. Just be careful when if comes to uno. That game ends relationships.")
    else:
      print("I am slightly familiar with that game. Must be pretty fun though if it is your favorite.")
    
  else:
    print("Interesting.")
    fun = input("Then what do you do for fun?")
    if fun == "read":
      print("Reading is boring, but cool that you like it.")
    elif fun == "cleaning":
      print("Wow! That's a new one. Must be an alien.")
    else:
      print("That sounds cool but personally I like board games or video games.")
else:
  print("I understand. I am just a strange program afterall.")
day = input("What day of the week is it?")
if day == "Sunday":
  print("Sundays are for sundaes! Treat yourself to a delicious treat for being such a great person.")
elif day == "Monday":
  print(f"You are a very strong person {name} and can face anything that comes your way.")
elif day == "Tuesday":
  print("Don't let others get in the way of doing what is right for you.")
elif day == "Wednesday":
  print("Congrats! Half of the week is over, only downhill from here. Keep it up.")
elif day == "Thursday":
  print("Be proud for all the challenges you've overcome thus far.")
elif day == "Friday":
  print(f"Yay! Friday is finally here! Relax and take a break this weekend. You deserve it {name}.")
elif day == "Saturday":
  print("Take some time to unwind today",name, "You have too much on your plate which is stressing you out.")
else:
  print("Well even if you don't know what day of the week it is")
print("Thank you for participating! <3")
