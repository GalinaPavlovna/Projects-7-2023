import pygame
import sys
import random

# p - экран, h1-воздушный кикорик
n=6
nf=4
pygame.init() #страртует пайгейм
p = pygame.display.set_mode((2000,900)) #экранчик
h1=pygame.image.load("ппр.png") #скачать героя 1
h1.set_colorkey((255,255,255)) #установить прозрачность
e=h1.get_rect(topleft=(10,300)) #перевести в квадрат
p.blit(h1,(e.x,e.y))# нарисовать
counter=0
#Делаем сов


f1=pygame.image.load("сова.svg")
s_sq=[]
for f in range (nf):
 s_sq.append(f1.get_rect(topleft=(random.randrange(100,1500),random.randrange(-600,0))))  # перевести в квадрат

 p.blit(f1, (s_sq[f].x, s_sq[f].y))  # нарисовать
pygame.draw.circle(p,(255,255,0),(100,100),15)
pygame.display.update()# обновить экранaq
x=[]
y=[]
w=[0]*n
for r in range (n):
 y.append(random.randrange(-600,0))
 x.append(random.randrange(10,1990))
while True:

#Отрисовка
 p.fill((250, 250, 210))#залить
 for f in range(nf):
  p.blit(f1, (s_sq[f].x, s_sq[f].y))
 for r in range (n):
  w[r]=pygame.draw.circle(p, (255, 255, 0), (x[r], y[r]), 15)
 p.blit(h1, (e.x, e.y))

 pygame.display.update()
#Выход из игры

 q=pygame.event.get()
 for i in q:
  if i.type==pygame.QUIT or i.type==pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
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
   if  s_sq[f].y > 900:
    s_sq[f].y = 0
    s_sq[f].x =random.randrange(30, 1985)
   s_sq[f].move_ip(0, 5)

#Убиваемся об сов
 for f in range(nf):
  t=e.colliderect(s_sq[f])
  if t==True:
   sys.exit()
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
#ловим шарики
 for o in range(n):
  t = e.colliderect(w[o])
  if t == True:
   counter+=1
   print(counter)
   y[r] = 0
   x[r] = random.randrange(10, 1990)


