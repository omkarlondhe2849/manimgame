import pygame

stat = pygame.init()

# print(stat)

window_1 = pygame.display.set_mode((500,500))

#apne game mein time ki bachodi na ho isliye...
clock_bahi = pygame.time.Clock()

#time passed between two frames..
dt = 0
speed = pygame.Vector2(10 , 30)

#window khuli rakhne ke liye...
running = True

player_pos = pygame.Vector2(window_1.get_width()/2, window_1.get_height()/2)

while running:

	window_1.fill("black")

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	player_pos += speed * dt
    
	gola = pygame.draw.circle(window_1,"white",player_pos,20)
    
    #flip the fucking screen ...
	pygame.display.flip()
    
    player_pos = pygame.Vector2(window_1.get_width)

	dt = clock_bahi.tick(60)/1000
	print(dt)
pygame.quit()