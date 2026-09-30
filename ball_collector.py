import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Balls")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont(None, 36)

basket = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 30, 100, 20)
ball = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)

basket_speed = 10
ball_speed = 5
score = 0
lives = 3

running = True
clock = pygame.time.Clock()


while running:

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        basket.x -= basket_speed

    if keys[pygame.K_RIGHT]:
        basket.x += basket_speed

    if basket.left < 0:
        basket.left = 0

    
    if basket.right > WIDTH:
        basket.right = WIDTH

    ball.y += ball_speed

    if ball.colliderect(basket):
        score +=1
        ball.x = random.randint(0,WIDTH - 20)
        ball.y = 0

    if ball.top > HEIGHT:
        lives -= 1
        ball.x = random.randint(0,WIDTH - 20)
        ball.y = 0

    if lives == 0:
        running = False

    pygame.draw.rect(screen, BLACK, basket)
    pygame.draw.ellipse(screen, RED, ball)

    score_text = font.render("Score: " + str(score), True, BLACK)
    lives_text = font.render("Lives: " + str(lives), True, BLACK)

    screen.blit(score_text, (10,10))
    screen.blit(lives_text, (480,10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()


    
    