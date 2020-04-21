import pygame
import pdb

HEIGHT = 600
WIDTH = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving ball")
clock = pygame.time.Clock()

def game_over():
    pygame.quit()
    sys.exit()

ball = pygame.image.load('Day 5/ball.gif')
ballrect = ball.get_rect()
ballrect.center = WIDTH/2, HEIGHT/2
speed = [2, 3]

while True:
    #====================
    # EASY
    # The program doesn't exit correctly (can't close the window; stalls and freezes). How can you fix that?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            

    #=========================
    # HARD
    # How can you make it so that when you press the up, left, down, and right arrows, the background color changes?
    # Assign these colors to each direction:
    # Up -  BLUE
    # LEFT - GREEN
    # DOWN - RED
    # RIGHT - BLACK

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > WIDTH:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > HEIGHT:
        speed[1] = -speed[1]

    #======================
    # MEDIUM
    # The ball sprite moves all over, but leaves a trace of itself with each movement. How can we get rid of that and have a white background? 
    screen.fill(WHITE)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(FPS)