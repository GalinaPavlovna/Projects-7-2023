import pygame
import sys
import random

# p - экран, h1-воздушный кикорик
n=4
pygame.init() #страртует пайгейм
p = pygame.display.set_mode((800,786)) #экранчик
h1=pygame.image.load("b1.jpg") #скачать героя 1
h1=pygame.transform.scale(h1,(55,80))
h1.set_colorkey((255,255,255)) #установить прозрачность
e=h1.get_rect(topleft=(10,300)) #перевести в квадрат
p.blit(h1,(e.x,e.y))# нарисовать
h2=[ ]
for i in range (n):
 h2.append(pygame.Rect(random.randint(100,700),(i+1)*100,40,40))
while True:
 # Отрисовка
 p.fill((250, 250, 210))#залить
 p.blit(h1, (e.x, e.y))
 for i in h2:
     pygame.draw.rect(p,(0,0,0),i)
 pygame.display.update()

#Выход
 q=pygame.event.get()
 for i in q:
  if i.type==pygame.QUIT or i.type==pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
   print(i)
   sys.exit()

#Движение героя
 if e.x>750:
  e.x=0
 if e.x<0:
  e.x=750
 if e.y>650:
  e.y=650
 if e.y<0:
  e.y=0
 v=pygame.key.get_pressed()
 if v[pygame.K_d]:
   e.move_ip(8, 0)
 if v[pygame.K_a]:
   e.move_ip(-8, 0)
 if v[pygame.K_w]:
   e.move_ip(0,-8)
 if v[pygame.K_s]:
   e.move_ip(0,8)

#Скорость игры
 pygame.time.delay(10)

#Теперь миша портит
#движение цензуры
 # if h2.x>750:
 #  h2.x=0
 # h2.move_ip(12,0)

#лок сталкновения



