cat_points = 0
dog_points = 0
fish_points = 0
#begining
# question 1:
answer = input("On a weekend would you rather A) sleep all day, B) pull a all nighter, C) Watch TV all day?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_points += 1

# question 2:
answer = input("Are you A) an extrovert, or B) an introvert, C) ambivert?")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	fish_points += 1

# question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a group, C) In a bathroom stall?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_points += 1
#Middle
# question 4:
answer = input("Have a pet to run with A) Have a lazy pet, or B) , C) Have a pet that swims?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_points += 1

# question 5:
answer = input("Have a pet that lives through your child hood A) Have a pet through your lifetime, or B) , C) Have a pet that dies quick?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_points += 1

# End of quiz
if cat_points > dog_points:
   print("You are a cat person.")
elif dog_points > fish_points:
   print("You are a dog person.")
else:
   print("You are a fish person.")