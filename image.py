from PIL import Image, ImageTk
import  tkinter as Tk
#cr?ation de la fenetre
 
root = Tk.Tk()
#importationd'une image dans un canvas ? la dimension de l'image
image = Image.open("image.jpg")
photo = ImageTk.PhotoImage(image)
canvas = Tk.Canvas(root, width = image.size[0], height = image.size[1])
canvas.create_image(0,0, anchor = Tk.NW, image=photo)
canvas.pack()
#prend les valeurs de chaque pixel de l'image
i=image
(largeur, hauteur)= i.size
for x in range(largeur):
     for y in range(hauteur):
        (rouge,vert,bleu)= i.getpixel((10,10)) #attribue de nouvelles valeurs ? chaque pixel de l'image
        i.putpixel((x,y),(rouge,vert,bleu))
 
i.save("new_unamed.png","PNG") # sauvegarde l'image form? avec un nom
print (rouge,vert,bleu)
root.mainloop() # boucle d'attente d'?venement