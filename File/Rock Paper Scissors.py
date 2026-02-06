import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rick Paper Scissors")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
BLUE = (70, 130, 180)

font = pygame.font.SysFont("arial", 30)
big_font = pygame.font.SysFont("arial", 40)

player_score = 0
computer_score = 0
result_text = " "

rock_btn = pygame.Rect(100, 350, 150, 60)
paper_btn = pygame.Rect(325, 350, 150, 60)
Scissors_btn = pygame.Rect(550, 350, 150, 60)
choices = ["Rock", "Paper", "Scissors"]

def draw_button(rect, text):
    pygame.draw.rect(screen, BLUE, rect)
    txt = font.render(text, True, WHITE)
    screen.blit(txt, (rect.x + 30, rect.y + 15))

def get_winner(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "Player"
    else:
        return "Computer"

running = True
clock = pygame.time.Clock()
    
while running:

    screen.fill(GRAY)

    title = big_font.render("Rock Paper Scissors", True, BLACK)

    screen.blit(title, (250, 30))   

    score = font.render(f"Player: {player_score} Computer: {computer_score}", True, BLACK)

    screen.blit(score, (260, 90))

    result = font.render(result_text, True, BLACK)

    screen.blit(result, (300, 150))
    draw_button(rock_btn, "Rock")
    draw_button(paper_btn, "Paper")
    draw_button(Scissors_btn, "Scissors")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rock_btn.collidepoint(mouse_pos):
                player_choice = "Rock"
            elif Scissors_btn.collidepoint(mouse_pos):
                player_choice = "Scissors"
            elif paper_btn.collidepoint(mouse_pos):
                player_choice = "Paper"
            else:
                "continue"

            computer_choice = random.choice(choices)
            winner = get_winner(player_choice, computer_choice)

            if winner == "Player":
                player_score += 1
                result_text = f"You chose {player_choice}, Computer chose {computer_choice} → You Win!"
            elif winner == "Computer":
                computer_score += 1
                result_text = f"You chose {player_choice}, Computer chose {computer_choice} → You Lose!"
            else:
                result_text = f"Both chose {player_choice} → Draw!"

    pygame.display.update()
    clock.tick(30)

pygame.quit()