import pygame
import sys
import random

# p - экран, h1-воздушный кикорик
n=6
nf=3
pygame.init() #страртует пайгейм
p = pygame.display.set_mode((800,786)) #экранчик
h1=pygame.image.load("b1.jpg") #скачать героя 1
h1=pygame.transform.scale(h1,(55,80))
h1.set_colorkey((255,255,255)) #установить прозрачность
e=h1.get_rect(topleft=(10,300)) #перевести в квадрат
p.blit(h1,(e.x,e.y))# нарисовать

while True:
 # Отрисовка
 p.fill((250, 250, 210))#залить
 p.blit(h1, (e.x, e.y))
 pygame.display.update()

#Выход
 q=pygame.event.get()
 for i in q:
  if i.type==pygame.QUIT or i.type==pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
   print(i)
   sys.exit()

#Движение героя
 if e.x>750:
  e.x=750
 if e.x<0:
  e.x=0
 if e.y>650:
  e.y=650
 if e.y<0:
  e.y=0
 v=pygame.key.get_pressed()
 if v[pygame.K_d]:
   e.move_ip(11, 0)
 if v[pygame.K_a]:
   e.move_ip(-11, 0)
 if v[pygame.K_w]:
   e.move_ip(0,-11)
 if v[pygame.K_s]:
   e.move_ip(0,11)

#Скорость игры
 pygame.time.delay(10)

#Теперь миша портит
 h2=pygame.Rect(400,400,50,50)