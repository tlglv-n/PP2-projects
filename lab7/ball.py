import pygame

pygame.init()
W, H = 850, 450
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
BLUE = (0, 0, 255)
RED = (255, 0, 0)
r = 25
x = W // 2
y = H // 2
move = 20
done = False
while not done:
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keydowns = pygame.key.get_pressed()
    if keydowns[pygame.K_UP] and y - r > 0:
        y -= move
    if keydowns[pygame.K_DOWN] and y + r < H:
        y += move
    if keydowns[pygame.K_LEFT] and x - r > 0:
        x -= move
    if keydowns[pygame.K_RIGHT] and x + r < W:
        x += move

    pygame.draw.circle(screen, RED, (x, y), r)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
