import pygame
pygame.init()

window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Chrome's Boring Dino")

RED = (255, 0, 0)
WHITE = (255, 255, 255)
FPS = 30

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
        if dino.x_pos + dino.width >= obstacle.x_pos and dino.:
            print("Collision detected")
        
        # if (dino.x_pos > obstacle.x_pos + obstacle.height) and (dino.x_pos < obstacle.x_pos + obstacle.width + obstacle.height) and\
        #     (dino.y_pos > obstacle.y_pos) and (dino.y_pos < obstacle + obstacle.height):
        #     print("Collide")


        # ######################################

#  def isPointInsideRect(x, y, rect):
#       if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
#           return True
#       else:
#           return False

dino = Dino(50, 500, 50, 100, 5, (255,0,0))
obstacles = []


loop_counter = 0
run = True
while run:
    clock.tick(FPS)
    loop_counter += 1


    #event catching
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dino.x_pos -= dino.speed
    if keys[pygame.K_RIGHT]:
        dino.x_pos += dino.speed
    if keys[pygame.K_SPACE]:
        dino.is_jump = True
    dino.jump()

    
    if loop_counter == 100:
        obstacles.append(Obstacle(1200, 500, 50, 120, 5, RED))
        loop_counter = 0
    
    collide(dino, obstacles)


    window.fill(WHITE)

    for obstacle in obstacles:        
        obstacle.draw(window)
        obstacle.move()
        if obstacle.x_pos < -650:
            obstacles.remove(obstacle)

    dino.draw(window)
    pygame.display.update()


pygame.quit()