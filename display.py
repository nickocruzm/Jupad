import pygame

screen = pygame.display.set_mode((640, 240))
running = True
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = false

pygame.quit()
