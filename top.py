import pygame
import random

# Oyna o'lchami
WIDTH = 500
HEIGHT = 600

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)

# Pygame boshlash
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎯 Catch the Ball o‘yini")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Ball va platforma o'lchamlari
ball_radius = 15
platform_width = 100
platform_height = 15

# Platforma boshlanish pozitsiyasi
platform_x = WIDTH // 2 - platform_width // 2
platform_y = HEIGHT - 40
platform_speed = 7

# Ball pozitsiyasi
ball_x = random.randint(20, WIDTH - 20)
ball_y = 0
ball_speed = 5

score = 0
lives = 3

run = True
while run:
    win.fill(WHITE)
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Harakat
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:
        platform_x -= platform_speed
    if keys[pygame.K_RIGHT] and platform_x < WIDTH - platform_width:
        platform_x += platform_speed

    # Ball pastga tushadi
    ball_y += ball_speed

    # Ball platformaga tegsa
    if (
        platform_y < ball_y + ball_radius < platform_y + platform_height
        and platform_x < ball_x < platform_x + platform_width
    ):
        score += 1
        ball_y = 0
        ball_x = random.randint(20, WIDTH - 20)

    # Agar tushirib yuborsa
    if ball_y > HEIGHT:
        lives -= 1
        ball_y = 0
        ball_x = random.randint(20, WIDTH - 20)

    # Ball
    pygame.draw.circle(win, RED, (ball_x, ball_y), ball_radius)

    # Platforma
    pygame.draw.rect(win, BLUE, (platform_x, platform_y, platform_width, platform_height))

    # Ball va hayotlar ko‘rsatish
    score_text = font.render("Ball: " + str(score), True, BLACK)
    lives_text = font.render("Hayot: " + str(lives), True, RED)
    win.blit(score_text, (10, 10))
    win.blit(lives_text, (WIDTH - 130, 10))

    pygame.display.update()

    if lives == 0:
        run = False

    clock.tick(60)

# Game over
win.fill(WHITE)
game_over_text = font.render("O‘yin tugadi! Ball: " + str(score), True, BLACK)
win.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
pygame.display.update()
pygame.time.delay(3000)

pygame.quit()
