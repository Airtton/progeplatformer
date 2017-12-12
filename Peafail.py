import pygame
import os

img_path = os.path.join('tegelane.png')
background = pygame.image.load("winter.png")
backgroundRect = background.get_rect()
size = (800, 600 )
background.get_size()
class player(object):
    def __init__(self):
        self.image = pygame.image.load(img_path)
        # playeri positsioon
        self.x = 200
        self.y = 200
        self.hspeed = 2
        self.vspeed = 0
        self.gravity = 0.5
        self.OnGround = True


    def liikumine(self):
        nupud = pygame.key.get_pressed()
        hüpe = 5
        dist = 1
        #self.y += dist
        if nupud[pygame.K_DOWN]:
            self.y += dist
        if nupud[pygame.K_UP]:
                for i in range(20):  # Delay the falling down as loops are very fast
                    if i <= 10:
                        self.y -= 0.5
                    elif i > 10:
                        self.y += 0.5
        if nupud[pygame.K_RIGHT]:
            self.x += dist
        if nupud[pygame.K_LEFT]:
            self.x -= dist

    def draw(self,surface):
        surface.blit(self.image,(self.x,self.y))
def hüppamine():
    hüppekõrgus = 10
pygame.init()
aken = pygame.display.set_mode((800,600))

player = player()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False
    player.liikumine()
    #aken.fill((255,255,255)) # fill the screen with white
    aken.blit(background, backgroundRect)
    player.draw(aken) # draw the pall to the screen
    pygame.display.update() # update the screen


    clock.tick(200)
