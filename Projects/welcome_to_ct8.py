###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fall")
mySprite = codesters.Sprite("cardinal")
mySprite.say("Good job finding me!")



print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
print(" this is the last instruction")
mySprite2 = codesters.Sprite("baseball",-250,250)