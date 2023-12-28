import random
import pygame
import sys

pygame.init()
width = 1000
height = 1000

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("snake")

clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

snake_size = 100
snake_position = [pygame.Rect(100,100,snake_size,snake_size),
                  pygame.Rect(90,100,snake_size,snake_size),
                  pygame.Rect(80,100,snake_size,snake_size)]
snake_direction = (0,1)
snake_speed = 10





fruit_size = 20
friut_x = (random.randint(0,(width-fruit_size)))
fruit_y = (random.randint(0,(height-fruit_size)))
fruit_position = (friut_x,fruit_y)
fruit_object = pygame.Rect(friut_x,fruit_y,fruit_size,fruit_size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.K_UP and snake_direction!=(0,1):
                snake_direction = (0,-1)
            elif event.type == pygame.K_DOWN and snake_direction!=(0,-1):
                snake_direction = (0,1)
            elif event.type == pygame.K_LEFT and snake_direction!=(1,0):
                snake_direction = (-1,0)
            elif event.type == pygame.K_RIGHT and snake_direction!=(-1,0):
                snake_direction = (1,0)
    
    new_x = snake_position[0].x+(snake_direction[0]*snake_speed)
    new_y = snake_position[0].y+(snake_direction[1]*snake_speed)
    new_position = pygame.Rect(new_x,new_y,snake_size,snake_size)
    snake_position.insert(0,new_position)

    if snake_position[0].colliderect(fruit_position):
        friut_x = (random.randint(0,(width-fruit_size)))
        fruit_y = (random.randint(0,(height-fruit_size)))
        fruit_position = (friut_x,fruit_y)
    else:
        snake_position.pop()
    
    if snake_position[0].left<0 or snake_position[0].right>=width or snake_position[0].top<0 or snake_position[0].bottom<=height or any(segment.colliderect(snake_position[0])  for segment in snake_position[1:]):
        pygame.quit()
        sys.exit()
    

    screen.fill((black))
    pygame.draw.rect(screen,red,fruit_object)
    for segment in snake_position:
        pygame.draw.rect(screen,white,segment)
    pygame.display.flip()
    clock.tick(60)

