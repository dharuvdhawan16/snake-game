import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up game clock
clock = pygame.time.Clock()

# Snake variables
snake_size = 20
snake_speed = 15
snake = [pygame.Rect(100, 100, snake_size, snake_size),
         pygame.Rect(90, 100, snake_size, snake_size),
         pygame.Rect(80, 100, snake_size, snake_size)]  # Initial snake positions
snake_direction = (1, 0)  # Initial direction (right)

# Food variables
food_size = 20
food_position = pygame.Rect(random.randint(0, (width - food_size) // food_size) * food_size,
                            random.randint(0, (height - food_size) // food_size) * food_size,
                            food_size, food_size)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Update snake position
    new_head = pygame.Rect(snake[0].x + snake_direction[0] * snake_size,
                           snake[0].y + snake_direction[1] * snake_size,
                           snake_size, snake_size)
    snake.insert(0, new_head)

    # Check if snake eats food
    if snake[0].colliderect(food_position):
        food_position = pygame.Rect(random.randint(0, (width - food_size) // food_size) * food_size,
                                    random.randint(0, (height - food_size) // food_size) * food_size,
                                    food_size, food_size)
    else:
        snake.pop()

    # Check if snake collides with itself or walls
    if (snake[0].left < 0 or snake[0].right >= width or
            snake[0].top < 0 or snake[0].bottom >= height or
            any(segment.colliderect(snake[0]) for segment in snake[1:])):
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill((0, 0, 0))  # Fill screen with black color
    pygame.draw.rect(screen, (255, 0, 0), food_position)  # Draw food
    for segment in snake:
        pygame.draw.rect(screen, (255, 255, 255), segment)  # Draw snake segments

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(snake_speed)
