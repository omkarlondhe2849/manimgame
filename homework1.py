import pygame
from pygame.draw import circle

pygame.init()

window_1 = pygame.display.set_mode((500, 500))
clock_bhai = pygame.time.Clock()
dt = 1
speed = pygame.Vector2(20, 30)  # Set initial speed
player_pos = pygame.Vector2(window_1.get_width() / 2, window_1.get_height() / 2)
colors = [(255, 255, 0), (0, 255, 255), (255, 0, 255)]  # List of colors
current_color_index = 0
running = True

while running:
    window_1.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_pos += speed * dt
    gola = pygame.draw.circle(window_1, colors[current_color_index], (int(player_pos.x), int(player_pos.y)), 50)

    # Check for collision with window boundaries and reverse the speed if needed
    if player_pos.y < 20 or player_pos.y > window_1.get_height() - 10:
        speed.y *= -1
        current_color_index = (current_color_index + 1) % len(colors)  # Cycle through colors

    if player_pos.x < 20 or player_pos.x > window_1.get_width() - 10:
        speed.x *= -1
        current_color_index = (current_color_index + 1) % len(colors)  # Cycle through colors

    pygame.display.flip()
    dt = clock_bhai.tick(165) / 60

pygame.quit()