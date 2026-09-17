from tkinter import*
from turtle import*

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2)
y = x * np.sqrt(x**2 + 1)
plt.plot(x, y, '.', label='$y=x\sqrt{x^2+ 1}$')
# tout ce qui suit : decoration (axes, legende...)
plt.grid(True, ls='--')
plt.axhline(color='red')
plt.axvline(color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='center', bbox_to_anchor=(.2, 0.75) , shadow=True) ;

 #a copier dans l'editeur de Spyder
a = np.arange(20)
print(a)
print(a[3])
print(a[3:6])
print(a[3:])
print(a[:3])
print(a[3:10:2])
print(a[5::3])
print(a[:-1])
print(a[10:2:-1])

import numpy as np
x = np.arange(15)
print(x)
x[0] = 200
print(x)
x[5:10] = -5
print(x)  #vu ?

 #dans l'editeur de Spyder
a = np.array([4, 5, 7])
b = np.array([12, -3, 11])
c = np.array([2, 3])
print('a=', a)
print('b=', b)
print('c=', c)
# somme de 2 tableaux
som = a + b
print('a+b=', som)
# produit (terme a terme)
print('a*b=', a * b)

import numpy as np

print('racine carree de 5 :', np.sqrt(5))
x = np.arange(0, 5.1, .5)
print('x=', x)
print('racine carree des elements de x=', np.sqrt(x))
import numpy as np

def f(x):
    return x**3/5 + 2*x**2 - 7

# 10 valeurs de x dans [-5,5]
x = np.arange(-5, 5.1, 1)
y = f(x)
print('x=', x)
print('y=f(x)=', y)

import pandas as pd

df = pd.DataFrame({'x': x, 'y': y})
print(df)
import numpy as np

A = np.array([[1, 2], [4, 5]])
B = np.array([[-1, 0], [3, 2]])
print(A, B, sep='\n')
print('somme terme a terme :')
print(A + B)
print('produit terme a terme :')
print(A * B)
print('produit matriciel :')#  pour ceux qui connaissent
print(A@B)
print(A.dot(B))
print(np.dot(A, B))

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.arange(8)
print(A.ndim)  #nombre de dimensions : vecteur, matrice...
print(A.shape)  #nombre de lignes et de colonnes
print(B.ndim)
print(B.shape)
# modification de "forme"
print('**C = B.reshape(4, 2)**')
C = B.reshape(4, 2)
print(C)
print(C.ndim)
print(C.shape)
print('**C = B.reshape(2, 4)**')
C = B.reshape(2, 4)
print(C)
print(C.ndim)
print(C.shape)

import numpy as np
import matplotlib.pyplot as plt # pour utiliser matplotlib

x = np.array([1, 2.5, 3, 5.8])
y = np.array([2, 1.2, 1.1, 0.8])
plt.plot(x, y) ; 

import numpy as np
import matplotlib.pyplot as plt  #pour utiliser matplotlib

x = np.array([1, 2.5, 3, 5.8])
y = np.array([2, 1.2, 1.1, 0.8])
plt.plot(x, y, 'ro:') ; 

"""
DECORATION : avec plusieurs series de points
"""
 #pas de marqueur, trait jaune (yellow), tirets
plt.plot([5, 10, 20, 22], 'y--')
 #marqueurs ronds relies par un trait continu
plt.plot([15, 12, 5, 15], 'o-');

"""
DECORATION : avec plusieurs series de points
"""
 #lw = linewidth - unite = le pt
plt.plot([5, 10, 20, 22], 'y--', lw = 5)
plt.plot([15, 12, 5, 15], 'r-.d')  #red et diamond
plt.plot([10, 20, 19, 12], 'g:s')  #green et square
plt.plot([2, 1, 3, 0], 'ko') ;  k = 'black'

import matplotlib.pyplot as plt
import numpy as np
# 10 valeurs de x dans l'intervalle [-2,2]
x = np.linspace(-2, 2, 10)
# Les valeurs de y correspondantes
y = x**2
# pour tracer : instruction plot
plt.plot(x, y) ;

x = np.linspace(-4*np.pi, 4*np.pi) # intervalle [-4,4] en x
y = 2 * x + np.sin(x)
plt.plot(x, y) ;

x = np.linspace(-2 * np.pi, 2 * np.pi, 20)  #20 points
y = np.sin(x)
plt.plot(x, y) ;

x = np.linspace(-5, 5, 200)#  200 points
y = np.sin(x)
plt.plot(x, y) ;

def g(x):
    return np.sin(2*x) * np.exp(-x/15)

x = np.linspace(0, 4*np.pi, 200)
plt.plot(x, g(x)) ;

"""
decoration : eviter les marqueurs si nombre de point eleve
"""
x = np.linspace(-4 * np.pi, 4 * np.pi, 200)#  200 points
y = np.sin(x)
plt.plot(x, y, 'o') ;

"""
COURBE PARAMETREE : cercle de centre (2;1) et de rayon 3
"""
# definir une figure "carree" pour voir un "vrai" cercle (pas aplati)
plt.figure(figsize=(5, 5))
t = np.linspace(0, 2*np.pi, 100)
x = 2 + 3*np.cos(t)
y = 1 + 3*np.sin(t)
plt.plot(x, y, 'g') 
# pour voir les axes :
plt.axhline(color='r')
plt.axvline(color='r')
plt.grid(True, ls='--') ;

"""
enregistrement du graphique
"""
x = np.linspace(0, 2, 200)
y = np.exp(-x) * np.sin(10*x)
plt.plot(x, y)
plt.savefig('fig.png') ;

import matplotlib.pyplot as plt
import numpy as np
 #10 valeurs de x dans l'intervalle [-2,2]
x = np.linspace(-2, 2, 50)
 #Les valeurs de y correspondantes
y1 = x**2      #1ere fonction
y2 = x/2 - 4   #2eme fonction
 #pour tracer : instruction plot
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid(True) ;        

"""
PLUSIEURS FONCTIONS SUR MEME GRAPHIQUE avec meme intervalle
"""
def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

def g(t):
    return np.exp(-t)

def h(t):
    return -np.exp(-t)

t = np.linspace(0, 4, 100)

plt.plot(t, f(t), label='$y=\sin(2\pi x)\exp(-x)$')
plt.plot(t, g(t), '--', label='$y=\exp(-x)$')
plt.plot(t, h(t), '--', label='$y=-\exp(-x)$')
 #legende, voir aussi plus loin
plt.legend(loc='upper right');

"""
PLUSIEURS FONCTIONS SUR MEME GRAPHIQUE : avec intervalles differents
"""
def f(t):
    return 2*t**3 - 3*t**2 - 12*t

def df(t):
    """
    derivee de f
    """
    return 6*t**2 - 6*t - 12

def tgte(t, a):
    """
    approximation affine (de degre 1) de f au point (a,f(a))
    --> representation graphique = tangente
    """
    return df(a) * (t - a) + f(a)

 #trace de la fonction sur [-3,4]
t = np.linspace(-3, 4, 200)
plt.plot(t, f(t), lw=2)

#trace des tangentes en x1=-1, x2=2 et x3=1/2 (pt inflexion)
for a in [-1, 2, 1/2]:
    t1 = np.linspace(a-2, a+2)
    plt.plot(t1, tgte(t1, a))
    
#2 = np.array([-1, 2, 1/2])
plt.plot(t1, f(t1), 'bo') 
 #representation des axes
plt.axhline(color='k',ls=':')
plt.axvline(color='k',ls=':') ;

"""
autre - les mêmes fonctions definies dans la cellule precedente
"""
for a in np.arange(-2.8, 3.6, .2):
    t1 = np.linspace(a-2, a+2)
    plt.plot(t1, tgte(t1, a), 'k:')   
t = np.linspace(-3, 4, 200)
plt.plot(t, f(t),'r', lw=2) 
plt.axhline(ls='--')
plt.axvline(ls='--') ;

"""
DECORATIONS : TITRES
"""
x = np.linspace(-5, 5, 100)
# marqeurs affiches : pas tres joli
 #les supprimer pour voir la difference
plt.plot(x, np.sin(x), 'r-*',x , np.cos(x), 'b-s')
plt.grid(True)
plt.title("jolis graphes de sin et cos")
plt.xlabel('temps')
plt.ylabel('fonction du temps')


"""
DECORATION : LEGENDES
"""
x = np.linspace(-5, 5, 100)
# entre $ : syntaxe latex
plt.plot(x, np.sin(x), 'r-', label='$y=\sin(x)$')
plt.plot(x , np.cos(x), 'b-', label='$y=\cos(x)$')
plt.grid(True)
plt.title("jolis graphes de sin et cos")
plt.xlabel('temps')
plt.ylabel('fonction du temps')
plt.legend() ;

"""
DECORATION : GRADUATIONS DES AXES
"""
def f(t):
    return 2*t**3 - 3*t**2 - 12*t

t = np.linspace(-3, 4, 200)
plt.plot(t, f(t), lw=2)
plt.grid(True)
plt.xticks([-2, 0, 2, 4])
plt.yticks(range(-40, 41, 20)) ;


"""
DECORATION : GRADUATIONS DES AXES
"""
from numpy import pi
x = np.linspace(-pi, pi, 100)
y = np.sin(x)
plt.xticks([-pi/2, 0, pi/2], ['-pi/2', '0', 'pi/2'])
plt.grid(True)
plt.xlim(-pi, pi)
plt.plot(x, y) ;

"""
GRAPHIQUES MULTIPLES
"""
x = np.linspace(-2, 2)
y1 = 2 * x + 3
y2 = np.sin(np.pi * 3 * x)
y3 = x**2
plt.subplot(121)
plt.plot(x, y1)
plt.subplot(222)
plt.plot(x, y2)
plt.subplot(224)
plt.plot(x, y3)
plt.axis('off') ;

plt.figure(figsize=(8, 6))  #taille de la fenetre
plt.subplot(221)
plt.title('plot 1')
# lt.axis([0, 2, 1, 3])
plt.xlim(-1, 1)
plt.ylim(1, 4)
plt.xticks([])
plt.subplot(222)
plt.grid(True)
plt.axis([0, 2, 4, 6]) # autre methode pour delimiter les axes en x et y
plt.subplot(223)
plt.plot([3, 1, 0, 5])
plt.subplot(224)
plt.title('plot 4')
t = np.linspace(-1, 1)
plt.plot(t, t, label='t')
plt.plot(t, t**2, label='$t^2$')
plt.xlabel('temps')
plt.ylim(-2, 2)
plt.legend()
plt.suptitle('ts les plots')
plt.tight_layout(pad=2);

3.4e23



             