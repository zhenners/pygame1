# Learning Game Development with Pygame

Table of Contents
1. Learning how to use VSCode
2. Setting up the environment with Pygame
3. Creating the display window
4. Creating a game loop and event handling
5. Drawing on the window (The Background and The Player)
6. Setting the position of enemies
7. Creating movement of characters
8. Spawning enemies
9. Collision
10. Bonus items! - Adding sound, text (health & score) and bullets

# 1. How to use VSCode

Here are some things you need to know to use VSCode!

1. Running your code: Just like the 'green flag' button on Scratch, we type this commmand ``` python3 main.py ``` in the ```terminal```. Or you can press the ``` up ``` button on the keyboard to avoid always typing the command.
2. Debugging: Sometimes your code will not run and we don't know why! Not to worry, the ```terminal``` lets you know where the error is in your code. 


# 2. Setting up the environment with Pygame
Goal: Import library and initialise Pygame

What you'll learn:
1. import ```pygame```: We need to import Pygame because it brings all the tools and functions we need to create our game. Without importing Pygame, your programme won't have access too the things that make games work!
2. ```pygame.init()```: Initialises all the Pygame modules. Think of it like flipping a switch to turn on all the different parts of the game. This function turns on all the parts of Pygame so you can start creating your game.

**Step 1: Type the following code below
**
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
   (include a picture of width and height)
2. ```pygame.display.set_mode()```: Makes the programme create a window of your preferred size.
3. ```pygame.display.set_caption()```: Sets the text that appears on the top of the window. 

Let's try it out with the following measurements and see how your screen changes in size!

   Step 1: Define the game constants. These are fixed values used throughout your game, meaning they don't change while the game is running. 

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
[ask them why is it important that we have fps]
2. ```pygame.time.Clock()```: creates a Clock that helps control the frame rate
3. ```clock.tick(FPS)```: makes sure that the game runs at the specified frame rates per second.

Step 1: Let's create our first function called main():.

```python
# The main game loop
def main():
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
```
Step 2: Let's set the desired FPS in our game constants

```python
# Game constants
WIDTH = 800
HEIGHT = 400
FPS = 30
```
Step 3: Use a function to manage the frame rate per second in the game

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

LOADING THE IMAGES 
Step 1: Assign a variable to the function and specify the file path. 

```python
background_image = pygame.image.load("assets/background.png")
```
This means:
background_image = our variable
pygame.image.load = function
assets = folder name (file path)
background.png = name of the image

Step 2: Your turn to load the player and enemy image!

MAKING THE IMAGE APPEAR ON SCREEN
Step 1: Create a ```draw``` function that will compartmentalise all our images and display. It should be above the ```main``` function

```python
# This where all your images/characters will come alive!
def draw():

# The main game loop
def main():
   clock = pygame.time.Clock()
   running = True
   while running:
```
Step 2: In the ```def draw():``` function, blit the image 

```python
def draw():
   WINDOW. blit(background_image, (0,0))
```
Let's break this down:
WINDOW = our variable that represents the window surface
background_image = our image loaded from the file
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

Step 2: Move the player to the left by 100 pixels from its current position

```python
player_image = pygame.image.load ("assets/player.png")
player_rect = player_image.get_rect()
player_rect.left = 100
```
Yay! The rocket has moved to the left. Let's position it to the middle.

Step 2: Move the player to the middle from its current position

```python
player_image = pygame.image.load ("assets/player.png")
player_rect = player_image.get_rect()
player_rect.left = 100
player_rect.centery = HEIGHT//2
```
For a sure shot to place the player in the middle, we took the ```HEIGHT``` and divided it by 2. 





# Setting the position of the enemies
Goal:
1. Create an invisible rectangle to around our enemy image
2. Draw the enemy image onto the display screen.
3. Understand factors like the number of enemies, spacing between the enemies and enemy behavior in gameplay.
4. Utilise the ```random``` module to generate random positions of the enemies for variability and unpredictability in the game.

What you'll learn: 

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
BUFFER_DISTANCE = To control where the enemies start appearing. We want some distance for the enemies before they appear into the screen, so that it looks realistic! This means we're setting an extra 500 of unseen space to our window width of 400 (400 + 500).
* draw a box of the extended 500

Step 4: We will create a ```list``` to hold all the enemies together.  [Ask why do we need a list to hold them?]

```python
# Our game constants
WIDTH = 800
HEIGHT = 400
FPS = 30
NUM_ENEMIES = 5
BUFFER_DISTANCE = 500
ENEMIES = []
```
Step 5: Let's create a loop for each enemy to appear by using ```random.randint``` function

```python
for _ in range(NUM_ENEMIES):
enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
```
This sets the left (x-coordinate) 




















