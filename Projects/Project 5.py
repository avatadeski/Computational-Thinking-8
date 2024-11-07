# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()


player = codesters.Sprite("dog")
player.set_size(0.09)
player.go_to(0,-200)
stage.disable_floor()


gameOver = False
lives = 5


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("kitten", x_position, 250)
        object.set_size(0.4)
        object.set_y_speed(-5)
   
stage.event_interval(falling_object, 0.5)


# Section 3 - Collision


def collision(dog, s2):
    global lives, gameOver
    if s2.get_image_name() == "kitten":
        stage.remove_sprite(s2)

        lives -=1

        if lives <=0:
           gameOver = True
        
             
player.event_collision(collision)


# Section 4 - Controls

def move_up(sprite):
	sprite.move_up(2)
   	 
def move_down(sprite):
	sprite.move_down(2)
    
def move_left(sprite):
	sprite.move_left(2)
    
def move_right(sprite):    
	sprite.move_right(2)
      
      

# Section 5: bind controls to specific keys

player.event_key("w", move_up)
player.event_key("s", move_down)
player.event_key("a", move_left)
player.event_key("d", move_right)
