from math import *
from turtle import *
from kandinsky import *
from time import *
from numpy import*




def Aff(object):
  for x in range(len(object)):
    print(object[x])

def DemiCarre(d):
  P=list(position())
  goto(P[0],P[1]+d)
  goto(P[0]-d,P[1]+d)
  goto(P[0],P[1]+d)

def GRILLE():
  H=linspace(0,36.3*7,7)
  V=linspace(0,36.3*8,8)
  for x in range(7):
    fill_rect(10,H[x],175,2,'black')
    fill_rect(V[x],10,2,175,'black')
    if x==6:
      fill_rect(10,H[x],175,2,'black')


def Grille():
  hideturtle()
  speed(15)
  penup()
  goto(-140,109)  #36.3*3
  pendown()
  goto(-140,-110)
  goto(-140+36.3,-110)
  for xx in range(2,9):
    for x in range(6):
      DemiCarre(36.3)
    penup()
    goto(-140+36.3*xx,-110)
    pendown()

def Jeu():
  L=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[7,7,7,7,7,7,7]]

  showturtle()
  penup()
  Curseur=[140.0,115.0-36.3*3]
  M=[0,3]  # Haut/Bas Gauche/Droite Position initiale
  GRILLE()
  J=1
  goto(36.3*3,0)
  while keyboard(KEY_RETURN)!=True:
    if keyboard(KEY_LEFT):
      Curseur[0]-=36.3
      M[1]-=1
      sleep(0.2)
      setheading(180)
      forward(36.3)
    if keydown(KEY_RIGHT):
      draw_string(" ",int(Curseur[0]),int(Curseur[1]))
      Curseur[0]+=36.3
      M[1]+=1
      sleep(0.2)
      setheading(0)
      forward(36.3)
    if keydown(KEY_UP):
      draw_string(" ",int(Curseur[0]),int(Curseur[1]))
      Curseur[1]-=36.3
      M[0]-=1
      sleep(0.2)
    if keydown(KEY_DOWN):
      draw_string(" ",int(Curseur[0]),int(Curseur[1]))
      Curseur[1]+=36.3
      M[0]+=1
      sleep(0.2)
    m=0
    if keydown(KEY_OK):
      sleep(0.2)
      if j==1:
        while L[int(M[0]+m)][M[1]]==0:
          m+=1
        L[M[0]+m-1][M[1]]=1
        fill_rect(int(Curseur[0]+(m-1)*36.3),int(Curseur[1]),31,31,"red")
        j=2
        fill_rect(250,10,5,5,"yellow")
      elif j==2:
        while L[int(M[0]+m)][M[1]]==0:
          m+=1
        L[M[0]+m-1][M[1]]=1
        fill_rect(int(Curseur[0]+(m-1)*36.3),int(Curseur[1]),31,31,"yellow")
        j=1
        fill_rect(250,10,5,5,"red")


    if keydown(KEY_ONE):
      m=0
      while L[int(M[0]+m)][M[1]]==0:
        m+=1
      L[M[0]+m-1][M[1]]=1
      fill_rect(int(Curseur[0]+(m-1)*36.3),int(Curseur[1]),31,31,"red")
      C=1
      sleep(0.2)



    if keydown(KEY_TWO):
      m=0
      while L[int(M[0]+m)][M[1]]==0:
        m+=1
      L[M[0]+m-1][M[1]]=2
      fill_rect(int(Curseur[0]+(m-1)*36.3),int(Curseur[1]),31,31,"yellow")
      C=2
      sleep(0.2)





#    draw_string("X",int(Curseur[0]),int(Curseur[1]))
