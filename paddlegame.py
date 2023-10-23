import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
WHITE = (255, 255, 255)
BALL_COLOR = (255, 0, 0)
PADDLE_COLOR = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Initialize the paddle's position
paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT

# Initialize the ball's position and velocity
ball_x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
ball_y = 0
ball_speed_y = 5

# Game loop
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= 5
    if keys[pygame.K_RIGHT]:
        paddle_x += 5

    # Update ball position
    ball_y += ball_speed_y

    # Ball collision with the paddle
    if (
        ball_y >= paddle_y - BALL_SIZE
        and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH
    ):
        score += 1
        ball_x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
        ball_y = 0

    # Ball misses the paddle and goes off-screen
    if ball_y > SCREEN_HEIGHT:
        ball_x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
        ball_y = 0

    # Clear the screen
    screen.fill(WHITE)

    # Draw the paddle
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_SIZE)

    pygame.display.flip()

# Game over
pygame.quit()
print(f"Game Over! Your Score: {score}")

