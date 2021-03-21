import sys, pygame

size = width, height = 320, 240
black = 0, 0, 0
screen = pygame.display.set_mode(size)
while True:
    screen.fill(black)
    pygame.display.flip()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        break;
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()