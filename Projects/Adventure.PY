# Intro
print ("You walk into the abandoned Sephora.")
print ("The door slams behind you.")
print("")
print("Will you be able to find the last Refy Mascara?")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
c1= input("Do you choose to go to the (back of the store) or stay at the (front of the store and explore)?")
if "front of the store and explore" in c1:
    print ("you walk to the mascara and eyelash curler wall")

    c2 = input("You see a ghost do you ask it to help you find the Refy Mascara Or Ignore It?")
    if "ask it to help you help you find the Refy Mascara" in c2:
        print("The ghost says sure thing")
    else:
        print("You ignore the ghost and start scannning the wall for the mascara.")

else:
    
    if "back of the store" in c1:
        print ("You walk to the back and open the door that writes EMPLOYES ONLY.")
        c3 = input("do you (walk left) or (walk right)?")
        if "walk left" in c3:
            print("you see back-stalk of blush, concealer and foundation.... GAME OVER")
        else:
            print("as you walk right you see mascaras, eyelash curlers, and eyeshadow... there it is you see the Refy Mascara!")

    c4 = input("The ghost says sure thing")
    if "ask it to help you help you find the Refy Mascara" in c2:
        print("you say thank you and you start to search?")
    else:
        print("")

    
        print ("You can't find it anywhere and the ghost has disappeared")
        c5 = input("do you (look around somewhere else) or (look in the cabinets under the wall)")
        if "look around somewhere else" in c3:
            print("you walk towards the lip products and setting powder")
        else:
            print("")