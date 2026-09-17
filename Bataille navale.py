from tkinter import*
from PIL import*

"""ETAPE 1 Créer le plateau"""


cote=60
e=3
decalage=7
width_canvas=2000           #cote*10+11*e-20
height_canvas=2000          #cote*10+11*e-20

"""Création de notre carte"""

fenetre = Tk()
fenetre.title("Toi")
fenetre.geometry("+650+25")
fenetre.geometry(f'{cote*10+e*11-20}x{cote*10+e*11-20}')
fenetre.resizable(width=False,height=False)
canvas=Canvas(fenetre, width=width_canvas,  height=height_canvas, background='#CCCCCC')

for i in range(10):
    for j in range(10):
        canvas.create_rectangle(cote*i+decalage,cote*j+decalage,cote+cote*i+decalage,cote+cote*j+decalage,width=e,state='disabled')
        canvas.pack()
canvas.pack()


""" Creation carte enemi"""

enemi = Tk()
enemi.title("Enemi")
enemi.geometry(f'{cote*10+e*11-20}x{cote*10+e*11-20}')
enemi.geometry("+1275+25")
enemi.resizable(width=False,height=False)

canvas2=Canvas(enemi, width=width_canvas,  height=height_canvas, background='#26c4ec')

for i in range(10):
    for j in range(10):
        canvas2.create_rectangle(cote*i+decalage,cote*j+decalage,cote+cote*i+decalage,cote+cote*j+decalage,width=e,state='disabled')
        canvas2.pack()
canvas2.pack()


"""ETAPE 2 Placer ses bateaux """

""" Definission de la zone de click """


def click_in(x,y,l,e): #revoie le cadran cliqué
    kx,ky=0,0
    while x>= l+l*kx+decalage: kx+=1
    while y>=l+l*ky+decalage: ky+=1
    return kx+1,ky+1


def click_toi(event):  #click dans ta zonec
    xy=click_in(event.x, event.y,cote,e)
    print(f"Placement du navire en {(xy[0],xy[1])}") #le long calcul est juste pour avoir un joli affichage 
    pieces(xy[0],xy[1],cote,e,decalage)
    return xy


def click_enemi(event):  #click dans la zone enemi
    xy2=click_in(event.x, event.y,cote,e)
    print(f"Tire en {xy2}")
    return xy2


""" Placement de ses bateaux """


def Ships(event):
    while


fenetre.bind("<KeyPress-Entry>",Ships)




""" Change de couleur un pixel """

def change_color_pixel(event):
    print("changé")
    coul=canvas.find_closest(15,620)
    print(coul)
    if coul[0]==10: # si c'est gris => c a  la verticale
        direction=0
    else :
        direction=1
    print(direction)
    
    if direction==0:  # si c'est à l'horizontal
        canvas.create_rectangle(10,615,20,635,state='disabled',fill='#CCCCCC') #remplace l'ancien
        canvas.create_rectangle(30,615,50,625,state='disabled',fill='red') #créé celui a la verticale
        direction=1
    elif direction==1: # si c'est à la verticale
        canvas.create_rectangle(30,615,50,625,state='disabled',fill='#CCCCCC') #remplace l'ancien
        canvas.create_rectangle(10,615,20,635,state='disabled',fill='red') #créé celui a l'horizontal
        direction=0
    return direction


fenetre.bind("<KeyPress-c>",change_color_pixel)





fenetre.bind("<Button-1>", click_toi)
# fenetre.bind("<Button-3>", rotate)
enemi.bind("<Button-1>", click_enemi)


"""Créatrion des pieces """


# =============================================================================
# def rotate(event):
#     print(fenetre.getpixel((cote*10+11*e+2,10+2)))
#     
#     if direction==1:
#         canvas.create_rectangle(cote*10+11*e,10,cote*10+11*e+5,15,state='disabled',fill='blue')
#     elif direction==0:
#         canvas.create_rectangle(cote*10+11*e+10,10,cote*10+11*e+15,15,state='disabled',fill='red')
#         
#     return direction
# =============================================================================
        

def pieces(X,Y,l,e,decalage,n=2):
    direction=change_color_pixel

    x=l+l*X+decalage
    y=l+l*Y+decalage
    if direction==0:
        canvas.create_rectangle(x+6,y+6,x+(l)*n-7,y+l-7,fill="red")
    elif direction==1:
        canvas.create_rectangle(x+4,y+4,x+l-8,y+(l+e)*n-8,fill="red")
    canvas.pack()

"""Reset les feuilles"""

def reset(event):
    """Ctr C/V à faire sur le truc qui s'affiche lors de l'execution"""
    """Dépend de l'emplacement du fichier sur l'ordi"""
    print("") #juste pour l'affichage
    close_gui(event)
    
    runfile('C:/Users/22404191T/OneDrive/scripts/Bataille navale.py', wdir='C:/Users/22404191T/OneDrive/scripts')
#    %runfile 'C:/Users/Utilisateur/OneDrive/scripts/Bataille navale.py' --wdir

fenetre.bind("<KeyPress-r>",reset)

"""Ferme les pages"""

def close_gui(event):
    fenetre.destroy()
    enemi.destroy()


fenetre.bind('<Escape>',close_gui) 
enemi.bind('<Escape>',close_gui)



fenetre.mainloop()