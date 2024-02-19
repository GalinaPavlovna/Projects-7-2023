import pygame
import sys
import random

# p - экран, h1-воздушный кикорик
n=6
nf=3
pygame.init() #страртует пайгейм
p = pygame.display.set_mode((2000,900)) #экранчик
h1=pygame.image.load("ппр.png") #скачать героя 1
h1.set_colorkey((255,255,255)) #установить прозрачность
e=h1.get_rect(topleft=(10,300)) #перевести в квадрат
p.blit(h1,(e.x,e.y))# нарисовать

#Делаем сов
f1=pygame.image.load("сова.svg")
s_sq=[0]*nf
for f in range (nf):
 s_sq[f] = f1.get_rect(topleft=(random.randrange(-600,0),random.randrange(10,1990)))  # перевести в квадрат
 p.blit(f1, (s_sq[f].x, s_sq[f].y))  # нарисовать
#r=pygame.Surface((10,10))
pygame.draw.circle(p,(255,255,0),(100,100),15)
#p.blit(r,(2,2))
pygame.display.update()# обновить экран
x=[]
y=[]
for r in range (n):
 y.append(random.randrange(-600,0))
 x.append(random.randrange(10,1990))
while True:
#переместить

#Отрисовка
 p.fill((250, 250, 210))#залить
 for r in range (n):
  pygame.draw.circle(p, (255, 255, 0), (x[r], y[r]), 15)
 p.blit(h1, (e.x, e.y))
 for f in range(nf):
  p.blit(f1, (s_sq[f].x, s_sq[f].y))
 pygame.display.update()
#Выход из игры

 q=pygame.event.get()
 for i in q:
  if i.type==pygame.QUIT or i.type==pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
   print(i)
   sys.exit()

#Двигаем героя
 if e.x>1650:
  e.x=1650
 if e.x<200:
  e.x=200
 v = pygame.key.get_pressed()
 if v[pygame.K_d]:
   e.move_ip(15, 0)
 if v[pygame.K_a]:
  e.move_ip(-15, 0)
#Двигаем сов
  for f in range(nf):
   if  s_sq[f].x > 1650:
    s_sq[f].x = 1650
   if  s_sq[f].x < 200:
    s_sq[f].x = 200
   s_sq[f].move_ip(0, 1)



  # if i.type == pygame.KEYDOWN and i.key == pygame.K_a:and i.key == pygame.K_ESCAPE
  #  e.move_ip(-11, 0)
  # if i.type == pygame.KEYDOWN and i.key == pygame.K_d:
  #  e.move_ip(11, 0)
#Двигаем шарики
 for r in range(n):
  y[r]=y[r]+5
  if y[r]>900:
   y[r]=0
   x[r] = random.randrange(10, 1990)
 pygame.time.delay(10)

