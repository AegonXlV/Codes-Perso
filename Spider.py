from pathlib import Path
from datetime import datetime
import exifread
from random import*
from string import*

## Lister les photos

def Listing():
    image_dir = 'C:/Users/22404191t/OneDrive/scripts/Snake'  # peut être n'importe quel chemin valide
    image_ext = ['.txt']
    image_files = [f for f in Path(image_dir).resolve().iterdir()
                if f.suffix in image_ext] #liste tt les photos
    return image_files

## Renomer une image

def renaming(Path_Image,i):
    

    old_path = Path(str(Path_Image)) #photo d'origine

    name=str(i)      #new name
    print(name)
    new_name='C:/Users/22404191t/OneDrive/scripts/Snake/'+name+'.txt'
#Insérer le chemin du fichier contenant les photos dans les 1er guimets
            #Mettre des / et pas des \ c'est important
    print(new_name)
    new_path = Path(new_name)
    old_path.rename(new_path)

## AVENGER ! Assemble

def RangementFichers():
    x=1
    liste_photos=Listing()
    for i in liste_photos:
        renaming(i,x)   
        x+=1
