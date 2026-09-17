def Probleme1(n=2013):
    S=0
    for i in range (n):
        if i%7==0 or i%5==0:
           S+=i
    return S

# =============================================================================

def Probleme2():
    S=2
    fibo=[1,1]
    while fibo[-1]<4e6:
        new=fibo[0]+fibo[1]
        if new%2==1:
            S+=new
        fibo.append(new)
        del(fibo[0])
    return S

# =============================================================================

def NbPremier(n):
    L = [2]
    for i in range(3, n + 1, 2):
        verif = True
        for j in L: 
            if i % j == 0:
                verif = False
        if verif:
            L.append(i)     
    return L

def Probleme3(N=19):
    n=N//2
    L=NbPremier(n)
    divs=[]
    while n!=1:
        for  i in L:
            if n%i==0:
                n=n/i
                print(n)
                divs.append(i)
    print(divs)

# =============================================================================

def palindrome():
    for i in range(10000,1000,-1):
        for j in range(1000,100,-1):
            verif=0
            n=str(i*j)
            for x in range(len(n)//2):
                if n[0+x]==n[-1-x]:
                    verif+=1
            if verif==len(n)//2:
                return f"{i}x{j}={i*j} est un palindrome"

# =============================================================================

def Probleme5():
    n=str(2**222)
    S=0
    for i in n:
        S+=int(i)
    print(S)

# =============================================================================

def facto(n):
    if n !=1:
        return n*facto(n-1)
    else :
        return n

def Probleme6():
    nb=str(facto(1558)) #max facto(1558) par manque de digits
    S=0
    for i in nb:
        S+=int(i)
    print(S)

# =============================================================================

def liste_des_NbPremier(n):
    i=3
    L = [2]
    while len(L)<n:
        verif = True
        for j in L:
            if i % j == 0:
                verif = False
        if verif:
            L.append(i)   
        i+=2
    return L

def Probleme7(n=23456):
    liste=liste_des_NbPremier(n)
    print(liste[-1])

# =============================================================================

def TripletsPytagoriciens():
    nb=[0]
    for a in range(3600):
        for b in range(3600):
            c=3600-a-b
            if c>=0:
                if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2 :
                    print(a,b,c)
                    if a*b*c>nb[0]:
                        nb=[a*b*c,a,b,c]
                        print("new nb :",nb[0])
    return nb

# =============================================================================

def mirroir(nb):
    nb=str(nb)
    palindrome=''
    for i in range(len(nb),0,-1):
        palindrome+=nb[i-1]
    return int(palindrome)

def Probleme11():
    condition=False
    n=10000000
    while condition==False :
        n-=1
        m=str(n)
        if int(m[1]+m[0])%4==0:
            if mirroir(n)==4*n:
                condition=True
    return n

# =============================================================================
import itertools

def Probleme12():
    possibilitées=list(itertools.permutations(range(1, 10)))
    memoire=[10**1000,'',0,'']
    for grille in possibilitées:
        somme=0
        for i in range(3):
            somme+=grille[i*3]*grille[i*3+1]*grille[i*3+2]+grille[0+i]*grille[3+i]*grille[6+i]
        if somme<memoire[0]:
            memoire[0]=somme
            memoire[1]=grille
            print("new min :",memoire[0])
        if somme>memoire[2]:
            memoire[2]=somme
            memoire[3]=grille
            print("NEW MAX :",memoire[2])
    return memoire[0]*memoire[2]