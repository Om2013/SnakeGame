import pygame 
import random

pygame.init() #Initialize the pygame


# Display settings (pixels)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Snake and Apple size
SNAKE_SIZE = 20
APPLE_SIZE = 20

# Initial snake head position and movement (start in the center)
head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2

# Track the movement of the snake using snake dx and dy
snake_dx = 0
snake_dy = 0

# Body and score
body_coords = []
score = 0 # Set score to 0 at the start

# Setup
FPS = 10 # Frames per second (Game speed) - After ten seconds a new frame will come  
clock = pygame.time.Clock() # Counts how many FPS have gone by
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Set the window height and width
pygame.display.set_caption("Draw a Snake") # Set the title of the screen
font = pygame.font.SysFont("Arial", 25) # Give the font settings

# Load sound
pick_up_sound = pygame.mixer.Sound(r"C:\Users\omrad\OneDrive\Desktop\Snake Game\pick_up_sound.wav") # Sound has been uploaded (download in files)

# Apple coordinates (generate coardinates for the apple store as tuple)
apple_x = random.randint(0, (WINDOW_WIDTH - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE
apple_y = random.randint(0, (WINDOW_HEIGHT - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE
apple_coord = (apple_x, apple_y, APPLE_SIZE, APPLE_SIZE)

# Game loop (handling user input) - runs until player quits 
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        # Movement controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_UP and snake_dy == 0:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            elif event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # Move the head
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
    head_rect = pygame.Rect(head_coord)
    apple_rect = pygame.Rect(apple_coord)

    # Check collision with apple
    if head_rect.colliderect(apple_rect):
        pick_up_sound.play() # Play the sound
        score += 1 # Add one to the score 

        # New apple position not overlapping snake
        while True:
            apple_x = random.randint(0, (WINDOW_WIDTH - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE
            apple_y = random.randint(0, (WINDOW_HEIGHT - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE
            new_apple = (apple_x, apple_y, APPLE_SIZE, APPLE_SIZE)
            if new_apple[:2] not in [b[:2] for b in body_coords] and new_apple[:2] != head_coord[:2]:
                break
        apple_coord = new_apple
    else:
        if body_coords:
            body_coords.pop()

    # Insert head at front
    body_coords.insert(0, head_coord)

    # Collision with walls (Stops running if snake passes boundaries )
    if head_x < 0 or head_x >= WINDOW_WIDTH or head_y < 0 or head_y >= WINDOW_HEIGHT:
        running = False

    # Collision with self (tuple)
    if head_coord in body_coords[1:]: # List of all body segments 
        running = False # Gameover 

    # Fill background
    display.fill((255, 255, 255)) # WITH WHITE 

    # Draw snake body
    for body in body_coords:
        pygame.draw.rect(display, "darkgreen", body) 

    # Draw apple and head
    pygame.draw.rect(display, "red", apple_coord)
    pygame.draw.rect(display, "green", head_coord)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0)) 
    display.blit(score_text, (10, 10))

    # Update screen
    pygame.display.flip()
    clock.tick(FPS) # Change frames per second 

pygame.quit() 


