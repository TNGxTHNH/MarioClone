import pygame;
import sys;

pygame.init()
backgroud = pygame.image.load("./Grafiken/hintergrund.png")
screen = pygame.display.set_mode((1200, 595))
pygame.display.set_caption("Pupskopf Game")
clock = pygame.time.Clock()

standAnimation = pygame.image.load("./GameCharacter/Idle (1).png")
jumpAnimation = pygame.image.load("./GameCharacter/Jump (1).png")
rightWalkAnimation = [pygame.image.load("./GameCharacter/Run (1).png"), pygame.image.load("./GameCharacter/Run (2).png"),
             pygame.image.load("./GameCharacter/Run (3).png"), pygame.image.load("./GameCharacter/Run (4).png"),
             pygame.image.load("./GameCharacter/Run (5).png"), pygame.image.load("./GameCharacter/Run (6).png"),
             pygame.image.load("./GameCharacter/Run (7).png"), pygame.image.load("./GameCharacter/Run (8).png"),
             pygame.image.load("./GameCharacter/Run (9).png"), pygame.image.load("./GameCharacter/Run (10).png"),
             pygame.image.load("./GameCharacter/Run (11).png"), pygame.image.load("./GameCharacter/Run (12).png"),
             pygame.image.load("./GameCharacter/Run (13).png"), pygame.image.load("./GameCharacter/Run (14).png"),
             pygame.image.load("./GameCharacter/Run (15).png"), pygame.image.load("./GameCharacter/Run (16).png"),
             pygame.image.load("./GameCharacter/Run (17).png"), pygame.image.load("./GameCharacter/Run (18).png"),
             pygame.image.load("./GameCharacter/Run (19).png"), pygame.image.load("./GameCharacter/Run (20).png")]
leftWalkAnimation = [pygame.image.load("./GameCharacter/Run (1) links.png"),
            pygame.image.load("./GameCharacter/Run (2) links.png"),
            pygame.image.load("./GameCharacter/Run (3) links.png"),
            pygame.image.load("./GameCharacter/Run (4) links.png"),
            pygame.image.load("./GameCharacter/Run (5) links.png"),
            pygame.image.load("./GameCharacter/Run (6) links.png"),
            pygame.image.load("./GameCharacter/Run (7) links.png"),
            pygame.image.load("./GameCharacter/Run (8) links.png"),
            pygame.image.load("./GameCharacter/Run (9) links.png"),
            pygame.image.load("./GameCharacter/Run (10) links.png"),
            pygame.image.load("./GameCharacter/Run (11) links.png"),
            pygame.image.load("./GameCharacter/Run (12) links.png"),
            pygame.image.load("./GameCharacter/Run (13) links.png"),
            pygame.image.load("./GameCharacter/Run (14) links.png"),
            pygame.image.load("./GameCharacter/Run (15) links.png"),
            pygame.image.load("./GameCharacter/Run (16) links.png"),
            pygame.image.load("./GameCharacter/Run (17) links.png"),
            pygame.image.load("./GameCharacter/Run (18) links.png"),
            pygame.image.load("./GameCharacter/Run (19) links.png"),
            pygame.image.load("./GameCharacter/Run (20) links.png")]


def draw(list):
    global stepRight,stepLeft

    screen.blit(backgroud, (0, 0))
    if stepRight == 63:
        stepRight = 0
    if stepLeft == 63:
        stepLeft = 0
    if list[0]:
        screen.blit(leftWalkAnimation[stepLeft // 8], (x, y))
    if list[1]:
        screen.blit(rightWalkAnimation[stepRight // 8], (x, y))
    if list[2]:
        screen.blit(standAnimation, (x, y))
    if list[3]:
        screen.blit(jumpAnimation, (x,y))


    pygame.display.update()


x = 300;
y = 480;
speed = 5;
width = 20;
height = 40;
jumpVar = -16

# [links, rechts, stehen, sprung]
moveController = [0, 0, 0, 0]
stepRight = 0;
stepLeft = 0;
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    charRect = pygame.Rect(x, y, 20, 40)
    press = pygame.key.get_pressed()
    moveController = [0, 0, 1, 0]
    if press[pygame.K_UP] and jumpVar == -16:
        jumpVar = 15;
    if press[pygame.K_RIGHT] and not charRect.colliderect(1201, 0, 2, 600):
        x += speed;
        moveController = [0, 1, 0, 0]
        stepRight += 1
    if press[pygame.K_LEFT] and not charRect.colliderect(-2, 0, 2, 600):
        x -= speed;
        moveController = [1, 0, 0, 0]
        stepLeft += 1

    if jumpVar >= -15:
        moveController = [0, 0, 0, 1]
        n = 1
        if jumpVar < 0:
            n = -1
        y -= (jumpVar ** 2) * 0.17 * n
        jumpVar -= 1
    if moveController[2] or moveController[3]:
        stepRight = 0
        stepLeft = 0

    draw(moveController)
    clock.tick(60)
