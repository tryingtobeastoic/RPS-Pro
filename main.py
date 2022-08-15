import random
import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("RPS Pro")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Images
rock = pygame.image.load('rock.png')
paper = pygame.image.load('paper.png')
scissors = pygame.image.load('scissors.png')
swords = pygame.image.load('swords.png')

#Variables
x_swords = 330
y_swords = 250
x_UI = 80
y_UI = 250
x_player = 650
y_player = 250
UI_score = 0
player_score = 0
font = pygame.font.SysFont('comicsansms', 30, False, False)
intro_message = "Welcome. Press r, p or s for rock, paper or scissors."
intro_rendering = font.render(intro_message, 1, (0, 0, 0))

def choices(UI_choice, player_choice):
    screen.fill((255, 215, 0))
    screen.blit(swords, (x_swords, y_swords))
    screen.blit(UI_choice, (x_UI, y_UI))
    screen.blit(player_choice, (x_player, y_player))
    score_counter = font.render(str(UI_score) + " - " + str(player_score), 1, (0, 0, 0))
    screen.blit(score_counter, (370, 20))




screen.fill((255, 215, 0))
screen.blit(intro_rendering, (55, 250))



#Game-loop
running = True
while running:
    UI_value = random.randint(1, 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if UI_value == 1 and event.key == pygame.K_r:
                choices(rock, rock)

            elif UI_value == 1 and event.key == pygame.K_p:
                player_score += 1
                choices(rock, paper)
               
            elif UI_value == 1 and event.key == pygame.K_s:
                UI_score += 1
                choices(rock, scissors)

            elif UI_value == 2 and event.key == pygame.K_r:
                UI_score += 1
                choices(paper, rock)
            
            elif UI_value == 2 and event.key == pygame.K_p:
                choices(paper, paper)
            
            elif UI_value == 2 and event.key == pygame.K_s:
                player_score+=1
                choices(paper, scissors)
            
            elif UI_value == 3 and event.key == pygame.K_r:
                player_score += 1
                choices(scissors, rock)
            
            elif UI_value == 3 and event.key == pygame.K_p:
                UI_score += 1
                choices(scissors, paper)
            
            elif UI_value == 3 and event.key == pygame.K_s:
                choices(scissors, scissors)
    pygame.display.update()

pygame.quit()
    
