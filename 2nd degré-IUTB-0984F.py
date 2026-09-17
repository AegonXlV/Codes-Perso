from math import*

def Delta(a,b,c):
    return -4*a*c+b**2

def racines(a,b,c,valeur_exacte=True):
    delta=Delta(a,b,c)
    
    if delta>0:
        x1=(delta**(1/2)-b)/2*a
        x2=(-delta**(1/2)-b)/2*a
        if valeur_exacte==False:
            print("Delta =",delta,"donc les racines sont :\nx1=",x1,"\nx2=",x2)
        else:
            print("x1=[√(",delta,")+",-b,"]/",2*a,"\nx2=[-√(",delta,")+",-b,"]/",2*a)
            
    elif delta==0:
        x=-b/(2*a)
        if valeur_exacte==False:
            print("Delta = 0 donc les doubles racines sont : x=",x)
        else:
            print("x=",-b,"]/",2*a)

    elif delta<0:
        delta=abs(delta)
        x1=sqrt(delta)/2*a
        x2=-sqrt(delta)/2*a
        if valeur_exacte==False:
            print("Delta < 0 donc les  racines sont :\nx1= i*",x1,"+",-b/2*a,"\nx2= i*",x2,"+",-b/2*a)
        else: 
            print("z=[±i*√(",delta,")+",-b,"]/",2*a)


def g(t):
    return sqrt(2)*sin(2*pi*t+pi/4)
