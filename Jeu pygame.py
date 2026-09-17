# Example file showing a circle moving on screen
import pygame as pyg
from math import sqrt

# pygame setup
pyg.init()
screen = pyg.display.set_mode((600, 500),flag=pyg.RESIZABLE)
clock = pyg.time.Clock()
running = True

# Astre 1

circle1_pos = pyg.Vector2(screen.get_width() / 3, screen.get_height() / 2)
V1 = pyg.Vector2(0,0)
A1 = pyg.Vector2(0,0)

# Astre 2

circle2_pos = pyg.Vector2(2*screen.get_width() / 3, screen.get_height() / 2)
V2 = pyg.Vector2(0,0)
A2 = pyg.Vector2(0,0)

# Astre 3

circle3_pos = pyg.Vector2(3*screen.get_width() / 3, screen.get_height() / 2)
V3 = pyg.Vector2(0,0)
A3 = pyg.Vector2(0,0)



# mouse_pos = pyg.mouse.get_pos()

follow = True

m1=1000

m2=1

G=2 #constante gravitationelle
screen.fill("white")
while running:
    
    mouse_pos = pyg.Vector2(pyg.mouse.get_pos())
    
    # poll for events
    # pyg.QUIT event means the user clicked X to close your window
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    screen.fill("white")

    pyg.draw.circle(screen, "black", circle1_pos, 10)
    pyg.draw.circle(screen, "red", circle2_pos, 10)
    
    keys = pyg.mouse.get_pressed()
    if keys[0]:          # Relie le bouton gauche de la souris avec la bille noir
        circle1_pos=pyg.Vector2(pyg.mouse.get_pos())
        V1 *=0
    else :
        follow = True
    if keys[2]:         # Relie le bouton droit de la souris avec la bille noir
        circle2_pos=pyg.Vector2(pyg.mouse.get_pos())
        V2 *=0
    if keys[1]:         # Ferme la fenetre si le bouton du milieu es tappuyé
        screen.fill("white")

    A1 = pyg.Vector2(circle2_pos.x-circle1_pos.x,circle2_pos.y-circle1_pos.y)
    A2 = pyg.Vector2(circle1_pos.x-circle2_pos.x,circle1_pos.y-circle2_pos.y)

    if follow:
        if circle2_pos.y == circle1_pos.y:
            V1.y += 0
            V2.y += 0
        else :
            V1.y += A1.y/20
            V2.y += A2.y/20
        if circle2_pos.x == circle1_pos.x:
            V1.x += 0
            V2.x += 0
        else :
            V1.x += A1.x/20
            V2.x += A2.x/20
            
        circle1_pos += V1
        circle2_pos += V2
        
        # print("V1 = ", sqrt(V1.x**2+V1.y**2))
        # print("V2 = ", sqrt(V2.x**2+V2.y**2))
        # print("")
    
    
    # flip() the display to put your work on screen
    pyg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pyg.quit()