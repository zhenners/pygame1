# Learning Game Development with Pygame

Table of Contents
1. Learning how to use VSCode
2. Setting up the environment with Pygame
3. Creating the display window
4. Creating a game loop and event handling
5. Drawing on the window
6. Creating movement of characters
7. Spawning enemies
8. Collision
9. Bonus items! - Adding sound, text (health & score) and bullets

# 1. How to use VSCode

Here are some things you need to know to use VSCode!

1. Running your code: Just like the 'green flag' button on Scratch, we type this commmand ``` python3 main.py ``` in the ```terminal```. Or you can press the ``` up ``` button on the keyboard to avoid always typing the command.
2. Debugging: Sometimes your code will not run and we don't know why! Not to worry, the ```terminal``` lets you know where the error is in your code. 


# 2. Setting up the environment with Pygame
Goal: Import library and initialise Pygame

What you'll learn:
1. import pygame: We need to import Pygame because it brings all the tools and functions we need to create our game. Without importing Pygame, your programme won't have access too the things that make games work!
2. pygame.init(): Initialises all the Pygame modules. Think of it like flipping a switch to turn on all the different parts of the game. This function turns on all the parts of Pygame so you can start creating your game.

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
2. pygame.display.set_mode(): Makes the programme create a window of your preferred size.
3. pygame.display.set_caption(): Sets the text that appears on the top of the window. 

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
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Create text
pygame.display.set_caption("PEW PEW PEW GAME")
```

# 3. Creating the game loop and event handling
Goals:
1. Keep the game running
2. Processing user inputs and system events to control the game aka event handling
3. Manage the game's frame rate per second

What you'll learn: 
1. Creating a main game loop function using ```def main():```. This serves as the core of the game. It initialises the game, contains the main game loop, updates the game state and renders the graphics.
2. pygame.event.get(): retrieves the list of events
3. pygame.QUIT: quitting the game

1. Frame rate per second (FPS): refers to the number of frames (images) that are displayed on the screen every second in a video or game. It is a measure of how smooth the animation appears to the user.
[ask them why is it important that we have fps]
2. pygame.time.Clock(): creates a Clock that helps control the frame rate
3. clock.tick(FPS): makes sure that the game runs at the specified frame rates per second.

Step 1: Let's create our first function called main():.

```python
def main():
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
```
Step 2: Let's set the desired FPS in our game constants

```python
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
# 4. Drawing on the window







