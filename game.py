import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
food_color = (255, 165, 0)

# Display dimensions
width = 600
height = 400

# Create game window
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cool Snake Game')

# Game clock
clock = pygame.time.Clock()

# Snake properties
snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Particle effect class for eating food
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 6)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.speed = [random.randint(-2, 2), random.randint(-2, 2)]

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.size -= 0.1

    def draw(self, surface):
        if self.size > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))

# Function to display score
def display_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    display.blit(value, [0, 0])

# Function to draw the snake with a gradient effect
def draw_snake(snake_block, snake_list):
    for idx, x in enumerate(snake_list):
        color = (0, 200 + (idx % 55), 0)  # Cool gradient effect
        pygame.draw.rect(display, color, [x[0], x[1], snake_block, snake_block])

# Function to animate game over screen
def game_over_animation():
    for alpha in range(0, 255, 5):
        display.fill(black)
        message = font_style.render("Game Over", True, red)
        display.blit(message, [width / 3, height / 3])
        pygame.display.update()
        time.sleep(0.02)

# Function to display a message
def display_message(msg, color, y_offset=0):
    message = font_style.render(msg, True, color)
    display.blit(message, [width / 6, height / 3 + y_offset])

# Main game loop
def game_loop():
    game_over = False
    game_close = False
    particles = []

    # Snake starting position
    x1 = width / 2
    y1 = height / 2

    # Snake movement direction
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            display.fill(black)
            game_over_animation()
            display_message("Press Q-Quit or C-Play Again", white, 50)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Handle window close event
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()  # Restart the game

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window close event
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(black)

        # Draw glowing food
        pygame.draw.circle(display, food_color, (int(food_x) + 5, int(food_y) + 5), 10)

        # Update snake's body
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Add particle effect when eating food
        for particle in particles:
            particle.move()
            particle.draw(display)

        particles = [p for p in particles if p.size > 0]

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            for _ in range(15):  # Generate particles
                particles.append(Particle(x1, y1))

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Start the game
game_loop()
