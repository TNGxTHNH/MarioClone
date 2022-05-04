import pygame;
import sys;

pygame.init()
backgroud = pygame.image.load("./Grafiken/hintergrund.png")
screen = pygame.display.set_mode((1200, 595))
pygame.display.set_caption("Pupskopf Game")
clock = pygame.time.Clock()

x = 300;
y = 300;
speed = 3;
width = 20;
height = 40;


leftWall = pygame.draw.rect(screen, (0,0,0), (-2,0,2,600), 0)
rightWall = pygame.draw.rect(screen, (0,0,0), (1201,0,2,600), 0)


def draw():
    screen.blit(backgroud, (0, 0))
    pygame.draw.rect(screen, (255, 255, 0), (x, y, width, height))
    pygame.display.update()
    clock.tick(60)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    gamerChar = pygame.Rect(x, y, 20, 40)
    press = pygame.key.get_pressed()
    if press[pygame.K_UP]:
        y -= speed;
    if press[pygame.K_RIGHT] and not gamerChar.colliderect(rightWall):
        x += speed;
    if press[pygame.K_LEFT] and not gamerChar.colliderect(leftWall):
        x -= speed;
    if press[pygame.K_DOWN]:
        y += speed;
    draw()

