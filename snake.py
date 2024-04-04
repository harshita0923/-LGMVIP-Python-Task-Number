import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake variables
block_size = 20
snake_speed = 15
snake_list = []
snake_length = 1

# Initial position of the snake
snake_x = width // 2
snake_y = height // 2
snake_x_change = 0
snake_y_change = 0

# Food position
food_x = random.randrange(0, width - block_size, block_size)
food_y = random.randrange(0, height - block_size, block_size)

# Font settings
font = pygame.font.SysFont(None, 25)

# Function to draw snake
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, black, [x, y, block_size, block_size])

# Game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = block_size
                snake_x_change = 0

    # Update snake's position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with boundaries
    if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
        game_over = True

    # Check for collision with itself
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, width - block_size, block_size)
        food_y = random.randrange(0, height - block_size, block_size)
        snake_length += 1

    # Fill screen with white color
    screen.fill(white)

    # Draw food
    pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

    # Draw snake
    draw_snake(snake_list)

    # Update display
    pygame.display.update()

    # Set snake speed
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()