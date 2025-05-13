import pygame 
pygame.init()

WINDOW_SIZE = 600
display = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Making Shapes in Pygame")

# Game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # Colors and screen fill
    display.fill((255, 255, 255))
    
    # Rectangle codes 
    pygame.draw.rect(display, (255, 0, 0), (250, 250, 50, 50)) 
    pygame.draw.rect(display, (255, 0, 0), (265, 250, 50, 50))
    pygame.draw.rect(display, (255, 0, 0), (280, 250, 50, 50))
    pygame.draw.rect(display, (255, 0, 0), (295, 250, 50, 50))

    # Triangle using rectangles
    pygame.draw.rect(display, (0, 0, 255), (275, 200, 50, 10))
    pygame.draw.rect(display, (0, 0, 255), (265, 210, 70, 10))
    pygame.draw.rect(display, (0, 0, 255), (255, 220, 90, 10))
    pygame.draw.rect(display, (0, 0, 255), (245, 230, 110, 10))
    pygame.draw.rect(display, (0, 0, 255), (235, 240, 130, 10))

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
