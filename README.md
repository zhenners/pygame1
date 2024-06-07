# Learning Game Development with Pygame

Table of Contents
1. Setting up the environment with Pygame
2. Creating the display window
3. Creating a game loop and event handling
4. Drawing on the window
5. Creating movement of characters
6. Spawning enemies
7. Collision
8. Bonus items! - Adding sound, text (health & score) and bullets

# Setting up the environment with Pygame
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
Goal: 
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

Your code should look something like this:

```python
# Game constants
WIDTH = 800
HEIGHT = 400

# Create display window
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Create text
pygame.display.set_caption("PEW PEW PEW GAME")
```





