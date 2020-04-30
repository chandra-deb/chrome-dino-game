import pygame
import random
pygame.init()

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (211, 211, 211)
GREEN = (50,205,50)

FPS = 30
point = 0

window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Chrome's Boring Dino")
font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render(str(point), True, GREEN, WHITE)
textRect = text.get_rect()  
textRect.center = (1000, 50) 




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
        return pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos, self.width, self.height))



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
            print("Collision detected")
            return True
        




dino = Dino(50, 500, 50, 100, 5, (GREEN))
obstacles = []   
loop_counter = 0
point_counter = 0
level = 1
o_counter = 150
random_speed = 5



game_over = False
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if game_over:
        window.fill(WHITE)
        window.blit(text, textRect)  
        textRect.center = (300, 300)
        text = font.render(":(Game Over :- press enter to play again", True, RED, WHITE)
        ks = pygame.key.get_pressed()
        if ks[pygame.K_RCTRL]:
                game_over = False
                textRect.center = (1000, 50) 
                dino = Dino(50, 500, 50, 100, 5, (GREEN))
                loop_counter = 0
                point_counter = 0
                point = 0
                obstacles = []

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
            dino.x_pos -= dino.speed
        if keys[pygame.K_RIGHT]:
            dino.x_pos += dino.speed
        if keys[pygame.K_SPACE]:
            dino.is_jump = True
            
        dino.jump()

        ###########Level Creator############
        if point == 100:
            level = 2
            loop_counter = 0
            o_counter = 120
        if point == 200:
            Level = 3
            loop_counter = 0
            o_counter = 80
        if point == 300:
            level = 4
            loop_counter = 0
            o_counter = 50
        if point == 400:
            level = 5
            loop_counter = 0
            o_counter = 20
            

        if level == 2:
            random_speed = random.randint(6, 12)
            dino.speed = 7
        elif level == 3:
            random_speed = random.randint(8, 18)
            dino.speed = 9
        elif level == 4:
            random_speed = random.randint(14, 24)
            dino.speed = 12
        elif level == 5:
            random_speed = random.randint(20, 30)
            dino.speed = 15


        
        if loop_counter == o_counter:
            obstacles.append(Obstacle(1200, 500, 50, 120, random_speed, RED))
            print(random_speed)
            loop_counter = 0

        # for i in range(1, (level*2)):
        #     obstacles.append(Obstacle(1200, 500, 50, 120, 5, RED))
            
        
        value = collide(dino, obstacles)
        if value:
            game_over = True


        window.fill(WHITE)
        window.blit(text, textRect) 


        for obstacle in obstacles:        
            obstacle.draw(window)
            obstacle.move()
            if obstacle.x_pos < -650:
                obstacles.remove(obstacle)

        dino.draw(window)
        text = font.render(str(point), True, GREEN, WHITE) 
        pygame.display.update()
    
    

pygame.quit()