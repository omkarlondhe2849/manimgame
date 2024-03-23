import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
height = 450
width = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bouncing Ball Game')

# Load images
background_image = pygame.image.load("background.jpg")
ball_image = pygame.image.load("ball1.jpg")
slider_image = pygame.image.load("slidder1.jpg")

# Get image dimensions
ball_rect = ball_image.get_rect()

# Initial position and speed of the ball
ball_x = random.randint(0, width - ball_rect.width)
ball_y = random.randint(0, height - ball_rect.height)
ball_speed_x = 5
ball_speed_y = 5

# Initial position and speed of the slider
slider_width = slider_image.get_width()
slider_x = (width - slider_width) // 2
slider_y = height - slider_image.get_height()
slider_speed = 7

# Score
score = 0

# Font
font = pygame.font.Font(None, 36)

# Game state
game_running = False

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_running = True

    if game_running:
        # Move the slider
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and slider_x > 0:
            slider_x -= slider_speed
        if keys[pygame.K_RIGHT] and slider_x < width - slider_width:
            slider_x += slider_speed

        # Update ball position
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Check for collisions with walls
        if ball_x <= 0 or ball_x >= width - ball_rect.width:
            ball_speed_x = -ball_speed_x
        if ball_y <= 0:  # Check for collision with top wall
            ball_speed_y = -ball_speed_y

        # Check if ball falls below the screen
        if ball_y >= height:
            # Game over
            game_running = False
            ball_x = random.randint(0, width - ball_rect.width)
            ball_y = random.randint(0, height // 2)
            ball_speed_y = 5
            score = 0  # Reset score
            continue

        # Check collision with slider
        if ball_y + ball_rect.height >= slider_y and ball_x + ball_rect.width >= slider_x and ball_x <= slider_x + slider_width:
            ball_speed_y = -ball_speed_y
            score += 1

    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))
    screen.blit(ball_image, (ball_x, ball_y))
    screen.blit(slider_image, (slider_x, slider_y))

    if not game_running:
        # Render "Press Space to Start"
        start_text = font.render("Press Space to Start", True, (255, 0, 0))
        start_text_rect = start_text.get_rect(center=(width // 2, height // 2))
        screen.blit(start_text, start_text_rect)

    # Render score
    score_text = font.render("Score: " + str(score), True, (255, 255, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
