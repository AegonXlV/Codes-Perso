from pprint import pprint

from pathlib import Path
from datetime import datetime
import exifread

## Lister les photos

def Listing():
    image_dir = 'F:/TMB'  # peut être n'importe quel chemin valide
    image_ext = ['.jpg', '.jpeg', '.JPG', '.JPEG']
#    image_ext = ['.mp4']
    image_files = [f for f in Path(image_dir).resolve().iterdir()
                if f.suffix in image_ext] #liste tt les photos
    return image_files

## Renomer une image

def renaming(Path_Image,previous_names):
    date=organisation(Date(Path_Image))

    old_path = Path(str(Path_Image)) #photo d'origine

    name=date[0]+date[1]+date[2]+'_'+date[3]+date[4]+date[5] #new name
    while name in previous_names:
        name+=' (2)'
    previous_names.append(name)
    new_name='F:/TMB/'+name+'.jpg'
#    new_name='C:/Users/Utilisateur/Pictures/TMB/'+name+'.mp4'
    new_path = Path(new_name)
    old_path.rename(new_path)
    print(name)
    return previous_names

# Recup la date

def Date(Path_Image):
    image_path = Path_Image
    with open(image_path, 'rb') as my_picture:
        tags = exifread.process_file(my_picture)
        try:
            picture_date = datetime.strptime(str(
                        tags.get('EXIF DateTimeOriginal')),
                        '%Y:%m:%d %H:%M:%S')
        except ValueError:
            picture_date = None
            print("No value for {filename}")
    return str(picture_date)

# Passer de date à liste de charactères

def organisation(date):
    num=['1','2','3','4','5','6','7','8','9','0']
    liste=list(date)
    Rangé=['']
    for l in liste:
        if l in num:
            Rangé[-1]=Rangé[-1]+l
        else:
            Rangé.append('')
    return Rangé


## AVENGER ! Assemble

def RangementPhotos():
    x=0
    previous_names=['']
    liste_photos=Listing()
    for i in liste_photos:
        name=renaming(i,previous_names)
