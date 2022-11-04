show = input("Do you watch the tv show Big Mouth?")
if show == "yes":
  print("I love that show!")
  character = input("Who is your favorite character? ")
  if character == "Connie":
      print("That's cool! I like her too.")
      line = input("What is your favorite line she says?")
      if line == "Bubble bath":
        print("Wow you really are a super fan!")
      elif line == "Rage, rage, f*cking rage!":
        print("She does not say that, Maury does. You are  not a super fan.")
      else:
        print("I do not know if she says that, but my favorite is when she says bubble bath.")
  elif character == "Mona":
    print("They are an ok character I guess.")
    accent = input("What accent does she have?")
    if accent == "British":
      print("Correct! Just testing you.")
    else:
      print("Wrong, she has a British accent.")
else:
  print("What a bummer, that is my favorite show.")
