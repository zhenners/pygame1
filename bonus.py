import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 400
WHITE = (255, 255, 255)
FPS = 30

NUM_ENEMIES = 5
BUFFER_DISTANCE = 500
ENEMIES = []
ENEMY_VELOCITY = 7
PLAYER_VELOCITY = 5

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PEW PEW PEW GAME")
background_image = pygame.image.load ("assets/background.png")
background_music = pygame.mixer.Sound("assets/background_music.wav")

FONT = pygame.font.SysFont('comicsans', 40)
health = 3
score = 0

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
    global score

    for enemy_rect in ENEMIES:
        if enemy_rect.right < 0:
            enemy_rect.left = random.randint(WIDTH, WIDTH + BUFFER_DISTANCE)
            enemy_rect.centery = random.randint(0, HEIGHT - 48)
            score += 1
        else:
            enemy_rect.x -= ENEMY_VELOCITY

def collision():
    global health

    for enemy_rect in ENEMIES:
        if player_rect.colliderect(enemy_rect):
            health -= 1
            ENEMIES.remove(enemy_rect)
            break

def draw():
    WINDOW.blit(background_image, (0,0))
    WINDOW.blit(player_image, player_rect)

    health_text = FONT.render("Health: " + str(health), 1, WHITE)
    WINDOW.blit(health_text, (10, 10))
    score_text = FONT.render("Score: " + str(score), 1, WHITE)
    WINDOW.blit(score_text, (10, 10 + health_text.get_height() + 10))
    for enemy_rect in ENEMIES:
        WINDOW.blit(enemy_image, enemy_rect)

def ending_screen(running):
    ending_text = FONT.render("YOU DIED!", 1, WHITE)
    WINDOW.blit(ending_text, (WIDTH // 2 - ending_text.get_width() // 2, HEIGHT // 2 - ending_text.get_height() // 2))
    score_text = FONT.render("Score: " + str(score), 1, WHITE)
    WINDOW.blit(score_text, ( WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2 + ending_text.get_height()))

    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
        pygame.time.delay(100)

def main():
    clock = pygame.time.Clock()
    background_music.play(loops=-1)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

        player_move()
        enemy_move()
        draw()
        collision()

        if health <= 0:
            break

    ending_screen(running)
    pygame.quit()

main()
