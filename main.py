import pygame
from pygame.locals import *
import snake
from random import randint

def is_coinciding(arr, point):
    for a in arr:
        if a == point:
            return True
    return False

pygame.init()

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = [600, 600]
screen = pygame.display.set_mode(size)
sq = 20
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
done = False
s = snake.Snake()

def get_food():
    return (sq*(randint(0, size[0]/sq)), sq*randint(0, size[1]/sq))

food = get_food()

while not done:
    # limit to 10 times per second. Otherwise keeps updating and moving. Uses up cpu power too. 
    clock.tick(10)

    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                s.dx, s.dy = -1, 0
            if event.key == K_RIGHT:
                s.dx, s.dy = 1, 0
            if event.key == K_UP:
                s.dx, s.dy = 0, -1
            if event.key == K_DOWN:
                s.dx, s.dy = 0, 1

    screen.fill(BLACK)
    
    s.move()
    # draw snake
    for cell in s.body[-1::-1]:
        pygame.draw.rect(screen, WHITE, [cell[0]*sq, cell[1]*sq, 20, 20])
    # draw food    

    if (s.x*sq, s.y*sq) == food:
        s.grow()
        new_food = get_food() 
        while is_coinciding(s.body, (new_food[0]/sq, new_food[1]/sq)):
            new_food = get_food()
        food = new_food 
    pygame.draw.rect(screen, RED, [food[0], food[1], 20, 20])

    pygame.display.update()

