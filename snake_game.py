import pygame 
pygame.init()

# Display
WINDOW_SIZE=600
display=pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Draw a Snake")

# Rectangle properties
rect_x=250
rect_y=250

# Gameloop
running = True 
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False



# Move the rectangle
    rect_x += 2
    rect_y += 2

# Fill the screen color with white
    display.fill((255,255,255)) 
    
# Draw the square (snake)
    pygame.draw.rect(display,(0,0,0),(rect_x,rect_y,20,20))

# Update the screen
    pygame.display.flip()

# Control the frame rate
    pygame.time.Clock().tick(60)
# Quit Pygame
pygame.quit()

