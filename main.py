import pygame
pygame.init()
    
WIDTH = 800
HEIGHT = 400
FPS = 30


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PEW PEW PEW GAME")
background_image = pygame.image.load ("assets/background.png")


player_image = pygame.image.load ("assets/player.png")
player_rect = player_image.get_rect()
player_rect.left = 100
player_rect.centery = HEIGHT//2 


enemy_image = pygame.image.load ("assets/enemy.png")
enemy_rect = enemy_image.get_rect()
    


def draw():
    WINDOW.blit(background_image, (0,0))
    WINDOW.blit(player_image, player_rect)

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


main()