import pygame;
import sys;


pygame.init()
backgroud = pygame.image.load("./Grafiken/hintergrund.png")
screen = pygame.display.set_mode((1200, 595))
pygame.display.set_caption("Pupskopf Game")
clock = pygame.time.Clock()

def draw():
    screen.blit(backgroud, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    pygame.display.update()


x = 300;
y = 480;
speed = 5;
width = 20;
height = 40;


jumpVar = -16
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    charRect = pygame.Rect(x, y, 20, 40)
    press = pygame.key.get_pressed()
    if press[pygame.K_UP] and jumpVar == -16:
        jumpVar = 15;
    if press[pygame.K_RIGHT] and not charRect.colliderect(1201, 0, 2, 600):
        x += speed;
    if press[pygame.K_LEFT] and not charRect.colliderect(-2, 0, 2, 600):
        x -= speed;
    if jumpVar >= -15:
        n = 1
        if jumpVar < 0:
            n = -1
        y -= (jumpVar ** 2) * 0.17 * n
        jumpVar -= 1
    draw()
    clock.tick(60)
