import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 400
FPS = 30

NUM_ENEMIES = 5
BUFFER_DISTANCE = 500
ENEMIES = []
ENEMY_VELOCITY = 7
PLAYER_VELOCITY = 5


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PEW PEW PEW GAME")
background_image = pygame.image.load ("assets/background.png")


player_image = pygame.image.load ("assets/player.png")
player_rect = player_image.get_rect()
player_rect.left = 100
player_rect.centery = HEIGHT//2 

def player_move():
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP] and player_rect.top > 0:
        player_rect.top -= PLAYER_VELOCITY  
    if key_pressed[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect.bottom += PLAYER_VELOCITY
    
enemy_image = pygame.image.load ("assets/enemy.png")
enemy_rect = enemy_image.get_rect()

for _ in range(NUM_ENEMIES):
    enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
    enemy_rect.centery = random.randint(0, HEIGHT - 48)
    ENEMIES.append(enemy_rect)

def enemy_move():
    for enemy_rect in ENEMIES:
        if enemy_rect.right < 0: 
            enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
            enemy_rect.centery = random.randint(0, HEIGHT - 48)
        else: 
            enemy_rect.x -= ENEMY_VELOCITY

def collision():
    if player_rect.colliderect(enemy_rect):
        quit()

def draw():
    WINDOW.blit(background_image, (0,0))
    WINDOW.blit(player_image, player_rect)
    #not sure if this included yet in the guide: gotta double check
    for enemy_rect in ENEMIES:
        WINDOW.blit(enemy_image, enemy_rect)
   
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    
        pygame.display.update()      

        draw()
        player_move()
        enemy_move()
        collision()

main()