import pygame
pygame.init()

window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Chrome's Boring Dino")

RED = (255, 0, 0)
FPS = 30

clock = pygame.time.Clock()

class Dino(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, width, height, speed, color):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.is_jump = False
        self.jump_count = 10
        self.rect = self.image.get_rect()
    

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
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.Surface((width, height))
        # self.width = width
        # self.height = height
        self.speed = speed
        self.image.fill(color)
        self.color = color
        self.rect = self.image.get_rect()
    
    def move(self):
        self.x_pos -= self.speed


    def draw(self, window):
        return pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos, self.width, self.height))


dino = Dino(50, 500, 50, 100, 5, (255,0,0))
# obstacles = []
# for i in range(10):
#     obstacles.append(Obstacle(1000, 500, 40, 120, 5, (45,43,99)))
#     print("obstacles created")

all_sprites = pygame.sprite.Group()
all_sprites.add(dino)
d_sprite = pygame.sprite.Group()
d_sprite.add(dino)


obstacles = []


running = True

# dino = pygame.draw.rect(window, RED, (50, 50))

while running: 
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        dino.x_pos += 5
    if keys[pygame.K_LEFT]:
        dino.x_pos -= 5
    if keys[pygame.K_SPACE]:
        dino.is_jump = True
    
    dino.jump()




    # count = 10
    # for obstacle in obstacles:
    #     obstacle.move()
    #     print("obstacle moved")
    #     print(obstacles)
    #     while count >= 0:
    #         count -= 1
    # else:
    #     obstacles.pop(obstacles.index(obstacle))


    for i in range(100):
        obstacles.append(Obstacle(1225, 500, 60, 150, 5, (53,59,21)))
        

    

    window.fill((255,255,255))
    # pygame.draw.rect(window, RED, ((dino_x_pos, dino_y_pos, 50, 100)))

    # dino.x_pos -= 5
    i = 0
    
    dino_group = pygame.sprite.Group.add(dino)
    for obstacle in obstacles:
        obstacle.move()
        i += 1
        if i == 10000:
            obstacle.draw(window)
            i =  0
    # obstacle.draw(window)
    for os in obstacles:
        all_obstacles = pygame.sprite.Group.add(os)
    dino.draw(window)
    if pygame.sprite.spritecollide(dino, all_obstacles, True):
        print("collision")
    pygame.display.update()

pygame.quit()