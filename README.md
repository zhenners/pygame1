# Learning Game Development with Pygame

Table of Contents
1. Learning how to use VSCode
2. Setting up the environment with Pygame
3. Creating the display window
4. Creating a game loop and event handling
5. Drawing on the window (The Background and The Player)
6. Setting the position of enemies
7. Creating movement of the enemy and the player
9. Collision of player and enemy
10. Bonus items! - Adding sound, text (health & score) and bullets

# 1. How to use VSCode

Here are some things you need to know to use VSCode!

1. Running your code: Just like the 'green flag' button on Scratch, we type this commmand ``` python3 main.py ``` in the ```terminal```. Or you can press the ``` up ``` button on the keyboard to avoid always typing the command.

2. Debugging: Sometimes your code will not run and we don't know why! Not to worry, the ```terminal``` lets you know where the error is in your code. 

*INSERT PIC: SCREENSHOT OF TERMINAL IN VSCODE

# 2. Setting up the environment with Pygame
Goal: 
1. Import library 
2. iInitialise Pygame

What you'll learn:
1. import ```pygame```: We need to import Pygame because it brings all the tools and functions we need to create our game. Without importing Pygame, your programme won't have access too the things that make games work!
2. ```pygame.init()```: Initialises all the Pygame modules. Think of it like flipping a switch to turn on all the different parts of the game. This function turns on all the parts of Pygame so you can start creating your game.

Step 1: Type the following code below

```python
import pygame

pygame.init()
```
# Creating the display window
Goals: 
1. Define the size of the game window
2. Create a display window where your game will be rendered
3. Name the game

What you'll learn: 
1. Setting the size: We use the measurement of width and height. This window is where all the game action will happen!
   (Ask them: why do you think it is important to set the size of the display window?)
   *INSERT PIC: include a picture of width and height
2. ```pygame.display.set_mode()```: Makes the programme create a window of your preferred size.
3. ```pygame.display.set_caption()```: Sets the text that appears on the top of the window. 

Let's try it out with the following measurements and see how your screen changes in size!

Step 1: Define the game constants. These are fixed values used throughout your game, meaning they don't change while the game is running. 

```python
# Game constants
WIDTH = 800
HEIGHT = 400
```

Step 2: Use a function to create the display window. Which should we use?

Step 3: Use a function to create the text on top of the window. Which should we use?

Your code should look something like this. Tell us what do you notice?:
[Ask them what happens after they run the code and explain why we need loops]

```python
# Game constants
WIDTH = 800
HEIGHT = 400

# Create display window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# Create text
pygame.display.set_caption("PEW PEW PEW GAME")
```
*INSERT PIC: INCLUDE A SCREENSHOT OF THE WINDOW WITH THE CAPTION

# 3. Creating the game loop and event handling
Goals:
1. Keep the game running
2. Process user inputs and system events to control the game aka event handling
3. Manage the game's frame rate per second

What you'll learn: 
1. Creating a main game loop function using ```def main():```. This serves as the core of the game. It initialises the game, contains the main game loop, updates the game state and renders the graphics.
2. ```pygame.event.get()```: retrieves the list of events
3. ```pygame.QUIT:```: quitting the game

1. Frame rate per second (FPS): refers to the number of frames (images) that are displayed on the screen every second in a video or game. It is a measure of how smooth the animation appears to the user.
[ask them what is fps, the value that defines our fps in the game and why is it important that we have fps]
2. ```pygame.time.Clock()```: creates a Clock that helps control the frame rate
3. ```clock.tick(FPS)```: makes sure that the game runs at the specified frame rates per second.

Step 1: Let's create our first function called ```main():```.

```python
# The main game loop
def main():
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
```
[assign someone to explain what this loop means & does]

Step 2: Let's set the desired FPS in our game constants

```python
# Game constants
WIDTH = 800
HEIGHT = 400
FPS = 30
```
Step 3: Use ```pygame.time.Clock()`` and ```clock.tick(FPS)``` to manage the frame rate per second in the game

```python
def main():
   clock = pygame.time.Clock()
   running = True
   while running:
      clock.tick(FPS)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            runnning = False
```
Step 4: Don't forget to let the computer to know to run the function!

```python
def main():
   clock = pygame.time.Clock()
   running = True
   while running:
      clock.tick(FPS)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            runnning = False

main()
```
# 4. Drawing on the window - The Space Background 

Goal:
1. Load the images of the game characters and display on the screen
2. Understand coordinates 


What you'll learn:
1. ```pygame.image.load():```to load images of the player's spaceship and enemy from your file directory
2. ```WIN.blit():``` to draw one image onto another surface.
3. ```pygame.display.update()``` to update the contents of the entire display screen.

TO LOAD THE IMAGES 

Step 1: Assign a variable to the function and specify the file path. 

```python
background_image = pygame.image.load("assets/background.png")
```
This means:
background_image = our variable
pygame.image.load = function
assets = folder name (file path)
background.png = name of the image

#INSERT PIC: SCREENSHOT OF GAME WINDOW WITH SPACE BACKGROUND

Step 2: Your turn to load the player and enemy image!

TO MAKE THE IMAGE APPEAR ON SCREEN

Step 1: Write a ```draw``` function that will compartmentalise all our images and display. It should be written above the ```main``` function

```python
# This where all your images/characters will come alive!
def draw():

# The main game loop
def main():
   clock = pygame.time.Clock()
   running = True
   while running:
```
Step 2: In the ```def draw():``` function, use ```.blit``` to make the image appear!

```python
def draw():
   WINDOW. blit(background_image, (0,0))
```
Let's break this down:

WINDOW = our variable that represents the window surface
background_image = our image loaded from the file
[ASSIGN SOMEONE TO EXPLAIN THAT IN GAMES, THE WINDOW BEGINS FROM THE TOP LEFT CORNER]
(0,0) = our x and y coordinates. This means that you want to draw the 'background' image starting from the top-left corner of the window.

Step 3: Let's update the contents using ```pygame.display.update()```. This will be called inside our ```main``` game loop. 

```python
def main():
   clock = pygame.time.Clock()
   running = True
   while running:
      clock.tick(FPS)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            runnning = False

      pygame.display.update()

main()
```
Step 4: The ```draw``` function will not work if we do not call it!

```python
   pygame.display.update()
   draw()

main()
```
# 5 Drawing the window - The Player 
Goals:
1. Create an invisible rectangle around the player image
[ASSIGN SOMEONE TO SHARE WHY WE NEED A RECTANGLE & WHAT ARE PIXELS]
2. Draw the player image on to the display screen

What you'll learn:
1. Using a rectangle to surround our player helps with the position, movement and collision in the game.
2. ```.get_rect():```: to create a rectangle that matches with size of the image.
3. ```.left``` and ```.centery```: to move the rectangle.
4. ```.centery```: represents the y-coordinate of its center. 

Step 1: Create the invisible rectangle based on the size of the player_image. Run your programme.

```python
player_image = pygame.image.load ("assets/player.png")
player_rect = player_image.get_rect()
```

Notice that the player is on the top left corner. Let's position it differently. 
*INSERT PIC: SCREENSHOT OF THIS PART

Step 2: Move the player to the left by 100 pixels from its current position

```python
player_image = pygame.image.load ("assets/player.png")
player_rect = player_image.get_rect()
player_rect.left = 100
```
Yay! This means that the left side of the player rectangle has moved to the left. Let's position it to the middle.
*INSERT PIC: DIAGRAM OF THE 100 pixels MOVEMENT


Step 2: Move the player to the middle from its current position

```python
player_image = pygame.image.load ("assets/player.png")
player_rect = player_image.get_rect()
player_rect.left = 100
player_rect.centery = HEIGHT//2
```
For a sure shot to place the player in the middle, we took the ```HEIGHT``` and divided it by 2. 

*INSERT PIC: DIAGRAM OF THE 100 pixels MOVEMENT

# 6 Setting the position of the enemies
Goal:
1. Create an invisible rectangle to around our enemy image
2. Draw the enemy image onto the display screen.
3. Understand factors like the number of enemies, spacing between the enemies and enemy behavior in gameplay.
   [ASSIGN SOMEONE TO EXPLAIN THE DIFFERENT MECHANICS IN GAME PLAY]
5. Utilise the ```random``` module to generate random positions of the enemies for variability and unpredictability in the game.

What you'll learn: 
1. TBC

Step 1: Create the invisible rectangle based on the size of the enemy_image. Then, blit it out onto the screen with the coordinates (0,0)
Try it out on your own! 

```python
enemy_image = pygame.image.load ("assets/enemy.png")
enemy_rect = enemy_image.get_rect()

def draw():
   WINDOW.blit (player_image, player_rect)
   WINDOW.blit (enemy_image, (0,0))
```

Your enemy has appeared! It should be at the top left position of the screen. 
*INSERT PIC: SCREENSHOT OF THIS PART

Step 2: To use the ```random``` module, we have to import it. Just like how we ```import pygame```.

```python
import pygame
import random
```

Step 3: Set the enemies' postions by setting up the parameters of our game constants.

```python
# Our game constants
WIDTH = 800
HEIGHT = 400
FPS = 30
NUM_ENEMIES = 5
BUFFER_DISTANCE = 500
```
NUM_ENEMIES = The number of enemies you want to create *each loop?
BUFFER_DISTANCE = To control where the enemies start appearing. We want some pixel distance for the enemies before they appear into the screen, so that it looks realistic! This means we're setting an extra 500 of unseen space to our window width of 400 (400 + 500).
* *INSERT PIC: SCREENSHOT OF THIS PART - draw a box of the extended 500

Step 4: We will create a `list` to hold all the enemies together.  [Ask why do we need a list to hold them?]

```python
# Our game constants
WIDTH = 800
HEIGHT = 400
FPS = 30
NUM_ENEMIES = 5
BUFFER_DISTANCE = 500
ENEMIES = []
```
Step 5: Let's create a loop for each enemy to appear by using a `for loop`

```python
for _ in range(NUM_ENEMIES):
```
Step 6: Under this loop, we are going to randomly set the positions of the enemies to be outside the screen using ```BUFFER_DISTANCE``` and the ```random.randint``` function.      

```python
for _ in range(NUM_ENEMIES):
   enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
```
Using ```enemy_rect.left``` means we are setting the left side of the enemy rectangle to a random position between the right edge of the game window (which is WIDTH = 800) and a BUFFER_DISTANCE of 500 more beyond the WIDTH (800 + 500).
The ```random.randint``` function helps us randomise the positions. 

Step 7: So we have set the enemies' position from left to right (horizontally). Let's set the up and down position (vertically) for the enemies using ```.centery```

```python
for in _ range(NUM_ENEMIES):
   enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
   enemy_rect.centery = random.randint(0, HEIGHT - 48)
```
Using ```enemy_rect.centery``` means we are setting the vertical center of the enemy rectangle at the top of the window (0) and 48 pixels less than the window HEIGHT (800 - 48). This ensures that the enemies are positioned randomly up and down within the visible height of the game window. 

Step 8: Now that we have created all the new random positions of these enemies. It is time to store them in a list called ```ENEMIES``` using ```.append```

```python
for _ in range(NUM_ENEMIES):
    enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
    enemy_rect.centery = random.randint(0, HEIGHT - 48)
    ENEMIES.append(enemy_rect)
``` 
Step 9: All the hard work is done! Let's make sure it appears on the screen by using the ```.blit``` function. Where should we place this function?

Remove the (0,0) coordinates as we have set new values in enemy_rect. Once done, run your code! Tell us what do you notice?  

```python
WINDOW.blit(enemy_image, enemy_rect)
```
# 7 Moving the enemies
Goal:
Move the enemies based on the random positions we have set earlier. 
Understand the use of velocity.
Use ```for loop``` and ```if else``` statements to move the enemies.

What you'll learn: 


Step 1: To make the enemies move, we will use velocity in our game constants. Velocity is the speed at which the enemies move horizontally. 

```python
# Game constants
NUM_ENEMIES = 5
BUFFER_DISTANCE = 500
ENEMIES = []
ENEMY_VELOCITY = 10
```
The higher the value of velocity, the faster the enemy moves. 

Step 2: Create a function to store all the enemies' movement only. 

```python
for _ in range(NUM_ENEMIES):
    enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
    enemy_rect.centery = random.randint(0, HEIGHT - 48)
    ENEMIES.append(enemy_rect)

# This is where all your enemies move!
def enemy_move():
```

Step 2: In the ```enemy_move():``` function, use a ```for loop``` to recall every enemy that we have created in the ```ENEMIES``` list. 

```python
def enemy_move():
   for enemy_rect in ENEMIES:
```
Step 3: To ensure that the enemies continuously moves horizontally in and out of screen. And also, returning back into the screen once it's out. First, we need to check, if the enemy's rectangle has moved out of the left side of the screen. 

```python
def enemy_move():
   for enemy_rect in ENEMIES:
   if enemy_rect.right < 0:
```
This means if the enemy's right edge of the rectangle is less than 0, it means that the enemy has moved out of the visible area. 0 is the starting point in the left side of screen. 

Step 4: Now that we have told the computer that if the enemies are out of the screen, we need to continue the loop to ensure that the enemies will return back to the screen again. 

```python
def enemy_move():
   for enemy_rect in ENEMIES:
      if enemy_rect.right < 0:
         enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
         enemy_rect.centery = random.randint(0, HEIGHT - 48)
```
This moves the enemy back to a random position at the right side of the screen, ready to re-enter the visible part of the screen. This also helps ensures that the game will continuously run when the player has not lose. 

Step 5: Great! Now it is time to make the enemies move using ```ENEMIES_VELOCITY``` and ```else```statement based on the conditions that we have set. 

```python
def enemy_move():
   for enemy_rect in ENEMIES:
      if enemy_rect.right < 0:
         enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
         enemy_rect.centery = random.randint(0, HEIGHT - 48)
      else:
         enemy_rect.x -= ENEMY_VELOCITY
```
We use ```rect.x``` because we want the enemies to move from right to left, horizontally (x-axis). ```-= ENEMY_VELOCITY``` moves the enemies by 10 pixels each time. We are using minus to decrease the x-axis coordinates, so that it moves to left. 

# 8 Using keys to move the player 
Goals
Use ```if``` statements to ensure player moves when only assigned keys are pressed. 
Understand the use of velocity.
Understand the position of the player in relative to the keys assigned. 
Player stays within the screen and not move outside of the screen [Ask them why is it important to create a boundary of where the player can move in the screen, game controls]

What you'll learn: 
1. ```pygame.key.get_pressed()``` function to move the player when keys are pressed.
2. ```pygame.K_UP``` and ```pygame.K_DOWN``` to assign up and down arrow keys to move the player. 

Step 1: Just like how we created a function for ```enemy_move():```. Define a function for ```player_move():``` and write it below where we created the rectangle for the player. 

``` python 
def player_move():
```

Step 2: For our game constants, set the speed of our player's movement using velocity. 

```python
PLAYER_VELOCITY = 5
```
Step 3: Assign a variable to the function ```pygame.key.get_pressed()``` under the ```player_move():``` function.

```python
def player_move():
   key_pressed = pygame.key.get_pressed()
```
This examines the state of the keys, whether they are pressed or not. 

Step 4: Using ```if``` statement, make the player move upwards when the UP arrow key is pressed. 

```python
def player_move():
   key_pressed = pygame.key.get_pressed()
   if key_pressed[pygame.K_UP] and player_rect.top > 0:
      player.rect.top -= PLAYER_VELOCITY
```
Run your code! This means that if the UP arrow key is pressed, and if the player's image rectangle top edge is not at the top edge of the screen, the player will be able to move up. This ensures that the player will not disappear off from the screen during the game. 

Step 4: Your turn! Using ```if``` statement, make the player move downwards when the DOWN arrow key is pressed. Make sure that the player does not go outside the screen! 

# 9 Collision detection between player and enemy
Goal:
1. When the enemy rectangle collides with the player rectangle, the game will end.

What you'll learn:
1. Use ```if``` statements to set a condition if the enemy collides with the player, the game will end.
2. ```.colliderect():```:  to check for collisions between two rectangles.

Step 1: Create a new function for ```collision``` below the ```enemy_move``` function 

Step 2: Write an ```if``` statement and ```.colliderect():``` to check for collision between player and enemy

```python
def collision():
   if player_rect.colliderect(enemy_rect):
   quit()
```
Do you think you can explain what this line of code means? It's time to run your code!

# 10 BONUS ITEMS!
Good job! You have made it this far.

We believe that there are many other features that can make the game better!

1. Adding music to the game
2. Adding a score and health for the player
3. Adding ending screen

## Adding music to the game
Step 1: In order to add music to the game, you'll need to use ```.mixer.Sound``` to load your music
```python
background_music = pygame.mixer.Sound("assets/background_music.wav")
```
Step 2: Play the background music in your ```main()``` function
```python
def main():
   clock = pygame.time.Clock()

   # play the background music on a loop
   background_music.play(loops=-1)
   ...

```
Run it and check it out for yourself!

## Adding score and health
Step 1: Initialize font and define initial variables
```python
FONT = pygame.font.SysFont('comicsans', 40)

# define initial health and score
health = 3
score = 0
```
Step 2: Every time the player avoids an enemy, their score increases. Increment the score by 1 for each enemy that passes the player and reaches the end of the screen.
```python
def enemy_move():
   global score

   for enemy_rect in ENEMIES:
      if enemy_rect.right < 0: # once enemy has passed the left side of the screen
            enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
            enemy_rect.centery = random.randint(0, HEIGHT - 48)
            score += 1 # increment score
```
Step 3: Every time the player is hit by an enemy, their health decreases. Decrement the health when checking collisions between enemy and player. (!)
```python
def collision():
   for enemy_rect in ENEMIES:
      if player_rect.colliderect(enemy_rect): # once enemy collides with player
         health -= 1 # decrement score
         ENEMIES.remove(enemy_rect)
         break
```
Step 4: When the player's health is 0, the game should stop running and display the ending screen. Add an ```if``` statement at the end of your main loop in ```main()``` and call ```ending_screen()``` outside your loop.
```python
def main():
	while running:
		... # your function calls blah blah blah..
		if health <= 0: # if health is 0, stop running
            break
	ending_screen()
   pygame.quit()
```
Step 5: Render the texts using ```.render``` and blit the text onto the window in your ```draw()``` function. You'll need to blit the score text below the health. You can do this by adding the height of the health text to the score text's height
```python
def draw():
   health_text = FONT.render("Health: " + str(health), 1, WHITE)
   WIN.blit(health_text, (10, 10))
   score_text = FONT.render("Score: " + str(score), 1, WHITE)
   # score text is positioned below the health message
   WIN.blit(score_text, (10, 10 + health_text.get_height() + 10))
```
Woohoo! We're almost done :D

## Adding ending screen
Step 1: Create an ```ending_screen()``` function and add your global variable ```running```. Recreate a similar game loop from your ```main()``` function here. Everything else should be added before the loop.
```python
def ending_screen():
	global running

	# Insert ending_screen display code here
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				exit()
		pygame.time.delay(100)
```
Step 2: To display an ending message, render and blit your message to the screen. Use the calculation ```(WIDTH // 2 - ending_text.get_width() // 2, HEIGHT // 2 - ending_text.get_height() // 2)``` to find the centre position of the screen
```python
	# display ending message
    ending_text = FONT.render("YOU DIED!", 1, WHITE)
    WIN.blit(ending_text, (WIDTH // 2 - ending_text.get_width() // 2, HEIGHT // 2 - ending_text.get_height() // 2))
```
Step 3: score is displayed below the ending message
```python
	# score is displayed below the ending message
    score_text = FONT.render("Score: " + str(score), 1, WHITE)
	# same calculations except add the height of the ending message
    WIN.blit(score_text, (
    WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2 + ending_text.get_height()))
```
Step 4: Update the display to show the ending text
```python
	pygame.display.update()
```
That's it, You're done! Congratulations (^-^) You can now enjoy your masterpiece and newfound knowledge and even bring it home with you!






















