import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)

# Font
font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 30)

dice_number = 1
running = True

while running:
    screen.fill(WHITE)

    # Draw dice box
    pygame.draw.rect(screen, BLUE, (150, 80, 100, 100), border_radius=10)

    # Dice number
    text = font.render(str(dice_number), True, WHITE)
    screen.blit(text, (190, 110))

    # Instruction
    info = small_font.render("Click to roll the dice", True, BLACK)
    screen.blit(info, (110, 220))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            dice_number = random.randint(1, 6)

    pygame.display.update()

pygame.quit()