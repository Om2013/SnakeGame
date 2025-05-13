import pygame  


# Initialize 
pygame.init()  


# Display
Window_Size = 600
display = pygame.display.set_mode((Window_Size, Window_Size))  
pygame.display.set_caption("Draw Initial S")  


# Colors
Orange = (255, 165, 0)  
Black = (0, 0, 0)  


# Game loop
GameLoop = True  
while GameLoop:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            GameLoop = False  


    # Fill the screen with Orange
    display.fill(Orange)  


    # Draw "S" using rectangles in Black
    pygame.draw.rect(display, Black, (200, 150, 100, 20))  
    pygame.draw.rect(display, Black, (200, 150, 20, 100))  
    pygame.draw.rect(display, Black, (200, 250, 100, 20))  
    pygame.draw.rect(display, Black, (280, 250, 20, 100))  
    pygame.draw.rect(display, Black, (200, 350, 100, 20))  


    # Update the display
    pygame.display.flip()  


pygame.quit()



