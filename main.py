import pygame
import os

img_path = os.path.join('kiwi.png')

class kiwi(object):
 def__init__(self):
 pygame.sprite.Sprite.__init__(self)

    character.image = pygame.image.load ('player.png')
  self.image = character.image
  self.image = pygame.transform.scale(self.image(50,50)

  self.x = 50
  self.y = 50
  self.hitbox = (self.x,self.y,55,50)

  def draw(self, surface):
     surface.blit(self.image,(self.x,self.y)




pygame.init()
screen_width = 600
screen_hight = 600
screen = pygame,display.set_mode((screen_width,screen_hight))  

Sprite = character()
clock = pygame.time.Clock()

running = True
while running:

  for  event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False

  screen.fill((255,255))
Sprite.draw(screen)

pygame.disply.update()

clock.tick(60)

kiwi.png = character

