import pygame
import random
import os

pygame.init()

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (211, 211, 211)
GREEN = (50,205,50)

FPS = 30
point = 0
high_score = 0

window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Chrome's Boring Dino")
font = pygame.font.Font('freesansbold.ttf', 32) 

text = font.render(str(point), True, GREEN, WHITE)
textRect = text.get_rect()  
textRect.center = (900, 100) 

score_text = font.render(" ", True, GREEN, WHITE)
score_text_rect = text.get_rect()  
score_text_rect.center = (900, 150) 

ot_score_text = font.render(" ", True, GREEN, WHITE)
ot_score_text_rect = text.get_rect()  
ot_score_text_rect.center = (500, 300) 

show_high_score = font.render(" ", True, GREEN, WHITE)
show_high_score_rect = text.get_rect()  
show_high_score_rect.center = (900, 50)

cong_high_score = font.render(" ", True, GREEN, WHITE)
cong_high_score_rect = text.get_rect()  
cong_high_score_rect.center = (200, 400)

intro_font = pygame.font.Font('freesansbold.ttf', 64) 
intro_text = intro_font.render(" ", True, GREEN, WHITE)
intro_text_rect = intro_text.get_rect()  
intro_text_rect.center = (300, 280)

intro_help_font = pygame.font.Font('freesansbold.ttf', 24) 
intro_help_text = intro_help_font.render(" ", True, GREEN, WHITE)
intro_help_text_rect = intro_help_text.get_rect()  
intro_help_text_rect.center = (250, 450)


#################try to find data file for high score##if unable to find it will create one
try:
    with open('high_score.txt', 'r') as txt_file:
        high_score = txt_file.read()
except:
    with open('high_score.txt', 'w') as txt_file:
        txt_file.write('0')


clock = pygame.time.Clock()

class Dino(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, width, height, speed, color):
    
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.is_jump = False
        self.jump_count = 10    

    def jump(self):
        if self.is_jump == True:
            if self.jump_count >= -10:
                self.y_pos -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else: 
                self.jump_count = 10
                self.is_jump = False

    
    def draw(self, window):
        return pygame.draw.rect(window, self.color, (int(self.x_pos), int(self.y_pos), self.width, self.height))



class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, width, height, speed, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def move(self):
        self.x_pos -= self.speed


    def draw(self, window):
        return pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos, self.width, self.height))



def collide(dino, obstacles):
    for obstacle in obstacles:
        if (dino.x_pos + dino.width >= obstacle.x_pos) and (dino.x_pos <= obstacle.x_pos + obstacle.width)\
        and (dino.y_pos >= obstacle.y_pos):
            return True
        




dino = Dino(50, 500, 50, 100, 5, (GREEN))
obstacles = []   
loop_counter = 0
point_counter = 0
level = 1
o_counter = 150
random_speed = 5
game_start = False
made_high_score = False

intro = True
while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_start = True
    intro_text = intro_font.render("Press Space to Play", True, GREEN, WHITE)
    intro_help_text = intro_help_font.render("Press K_LEFT, K_RIGHT to Move and Press SPACE to jump", True, GREEN, WHITE)
    window.fill(WHITE)
    window.blit(intro_text, intro_text_rect)
    window.blit(intro_help_text, intro_help_text_rect)
    pygame.display.update()

    if game_start:

        game_over = False
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    intro = False

            if game_over:
                window.fill(WHITE)
                window.blit(text, textRect)  
                textRect.center = (300, 200)

                text = font.render(":(Game Over :- press Tab to play again", True, RED, WHITE)
                ot_score_text = font.render("SCORE: " + str(point), True, GREEN, WHITE)

                with open('high_score.txt', 'r') as txt_file:
                    high_score = txt_file.read()


                if int(point) > int(high_score):
                    made_high_score = True
                    # cong_high_score = font.render(":)Congratulations! You are now the highest scorer.", True, GREEN, WHITE)
                    # window.blit(cong_high_score, cong_high_score_rect)
                    with open('high_score.txt', 'w') as txt_file:
                        txt_file.write(str(point))
                
                # if made_high_score:
                #     cong_high_score = font.render(":)Congratulations! You are now the highest scorer.", True, GREEN, WHITE)
                #     window.blit(cong_high_score, cong_high_score_rect)                   
                
                window.blit(ot_score_text, ot_score_text_rect)

                
                

                        
                # window.blit(ot_score_text, ot_score_text_rect)

                ks = pygame.key.get_pressed()
                if ks[pygame.K_TAB]:
                        game_over = False
                        textRect.center = (900, 100) 
                        dino = Dino(50, 500, 50, 100, 5, (GREEN))
                        loop_counter = 0
                        point_counter = 0
                        point = 0
                        obstacles = []
                        level = 1
                        o_counter = 150
                        random_speed = 5

                pygame.display.update()

                    

            if not game_over:
                loop_counter += 1
                if point_counter == 5:
                    point += 1
                    point_counter = 0
                point_counter += 1
            




                #event catching
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    if dino.x_pos > 25:
                        dino.x_pos -= dino.speed
                if keys[pygame.K_RIGHT]:
                    if dino.x_pos < 1100:
                        dino.x_pos += dino.speed
                if keys[pygame.K_SPACE]:
                    dino.is_jump = True

                dino.jump()

                ###########Level Creator############

                if point == 100:
                    level = 2
                    loop_counter = 0
                    o_counter = 100
                if point == 300:
                    Level = 3
                    loop_counter = 0
                    o_counter = 70
                if point == 500:
                    level = 4
                    loop_counter = 0
                    o_counter = 50
                if point == 700:
                    level = 5
                    loop_counter = 0
                    o_counter = 40
                if point == 850:
                    level = 6
                    loop_counter = 0
                    o_counter = 35
                if point == 950:
                    level = 7
                    loop_counter = 0
                    o_counter = 30
                if point == 1200:
                    level = 8
                    loop_counter = 0
                    o_counter = 25
                if point == 1350:
                    level = 9
                    loop_counter = 0
                    o_counter = 20
                if point == 1500:
                    level = 10
                    loop_counter = 0
                    o_counter = 15
                    

                elif level == 2:
                    random_speed = random.randint(6, 12)
                    dino.speed = 6
                elif level == 3:
                    random_speed = random.randint(7, 14)
                    dino.speed = 8
                elif level == 4:
                    random_speed = random.randint(8, 16)
                    dino.speed = 10
                elif level == 5:
                    random_speed = random.randint(9, 18)
                    dino.speed = 12
                elif level == 6:
                    random_speed = random.randint(10, 20)
                    dino.speed = 14
                elif level == 7:
                    random_speed = random.randint(11, 22)
                    dino.speed = 16
                elif level == 8:
                    random_speed = random.randint(12, 24)
                    dino.speed = 17
                elif level == 9:
                    random_speed = random.randint(13, 26)
                    dino.speed = 18
                elif level == 10:
                    random_speed = random.randint(15, 30)
                    dino.speed = 20
                


                
                if loop_counter == o_counter:
                    obstacles.append(Obstacle(1200, 500, 50, 120, random_speed, RED))
                    loop_counter = 0

                ######check if dino collide with obstacles######
                value = collide(dino, obstacles)
                if value:
                    game_over = True

                text = font.render("SCORE: " + str(point), True, GREEN, WHITE)
                score_text = font.render("LEVEL: " + str(level), True, GREEN, WHITE) 
                show_high_score = font.render("HIGH SCORE: " + str(high_score), True, GREEN, WHITE)

                window.fill(WHITE)
                window.blit(show_high_score, show_high_score_rect) 
                window.blit(score_text, score_text_rect)
                window.blit(text, textRect)
                
                


                for obstacle in obstacles:        
                    obstacle.draw(window)
                    obstacle.move()
                    if obstacle.x_pos < -650:
                        obstacles.remove(obstacle)

                dino.draw(window)

                pygame.display.update()
            
            

pygame.quit()