import pygame
from pygame.locals import *
import snake
from random import randint

pygame.init()

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = [600, 600]
sq = 20
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 100)


over_text = font.render("GAME OVER", 1, WHITE)
over_rect = over_text.get_rect()
over_rect.centerx, over_rect.centery = size[0]/2, size[1]/2 

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
s = snake.Snake()

def get_food():
    return (sq*(randint(1, (size[0]/sq)-1)), sq*randint(1, (size[1]/sq)-1))

food = get_food()

while s.score >= 0:
    # limit to 10 times per second. Otherwise keeps updating and moving. Uses up cpu power too. 
    clock.tick(10)

    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT and s.dx != 1:
                s.dx, s.dy = -1, 0
            if event.key == K_RIGHT and s.dx != - 1:
                s.dx, s.dy = 1, 0
            if event.key == K_UP and s.dy != 1:
                s.dx, s.dy = 0, -1
            if event.key == K_DOWN and s.dy != -1:
                s.dx, s.dy = 0, 1
            break

    screen.fill(BLACK)
    if not s.move():
        s.score = -1
    if s.x < 0 or s.x >= size[0]/sq or s.y < 0 or s.y >= size[1]/sq:
        s.score = -1

    # draw snake
    for cell in s.body[-1::-1]:
        pygame.draw.rect(screen, WHITE, [cell[0]*sq, cell[1]*sq, 20, 20])
    # check and draw food    
    if s.score >= 0 and (s.x*sq, s.y*sq) == food:
        s.score += 1
        s.grow()
        new_food = get_food() 
        while (new_food[0]/sq, new_food[1]/sq) in s.body:
            new_food = get_food()
        food = new_food 
    pygame.draw.rect(screen, RED, [food[0], food[1], 20, 20])
    pygame.display.update()

screen.blit(over_text, over_rect)
pygame.display.update()
pygame.time.delay(5000)
pygame.quit()
