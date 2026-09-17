from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=321, height=223, background='#fff')
canvas.pack()
colors=[[(255, 255, 255) for i in range(223)] for i in range(321)]

def color(a,b,c):
    if a<10:
        va='0'+str(a)
    else:
        va=hex(a%256).replace('0x','')
    if b<10:
        vb='0'+str(b)
    else:
        vb=hex(b%256).replace('0x','')
    if c<10:
        vc='0'+str(c)
    else:
        vc=hex(c%256).replace('0x','')
    return '#%s'%(va+vb+vc)

def colr(lis):
    a=lis[0]
    b=lis[1]
    c=lis[2]
    if a%256<10:
        va='0'+str(a%256)
    else:
        va=hex(a%256).replace('0x','')
    if b%256<10:
        vb='0'+str(b%256)
    else:
        vb=hex(b%256).replace('0x','')
    if c%256<10:
        vc='0'+str(c%256)
    else:
        vc=hex(c%256).replace('0x','')
    return '#%s'%(va+vb+vc)

def fill_rect(a,b,c,d,e):
    if type(e)==str:
        canvas.create_rectangle(a+2,b+2,c+a+2,d+b+2,fill=e,outline='')
    else:
        canvas.create_rectangle(a+2,b+2,c+a+2,d+b+2,fill=colr(e),outline='')
    #modifie la valeur de la couleur au pixel x,y
    for x in range(c):
        for y in range(d):
            if (a+x)>=0 and (a+x)<=320 and (b+y)>=0 and (b+y)<=222:
                colors[a+x][b+y]=e
def set_pixel(a,b,e):
    fill_rect(a,b,1,1,e)

def get_pixel(x,y):
    if x>=0 and x<=320 and y>=0 and y<=222:
        return colors[x][y]
    else:
        return (0,0,0)


def fill_circle(x,y,r,c):
  rr=int(r*0.7071067811865475)
  r2=r**2
  fill_rect(x-rr,y-rr,2*rr,2*rr,c)
  for xx in range(x-rr-1,x+rr+1):
    for yy in list(range(y-r-1,y-rr))+list(range(y+rr,y+r+1)):
      if ((yy-y)**2+(xx-x)**2)<=r2:
        set_pixel(xx,yy,c)
  for yy in range(y-rr-1,y+rr+1):
    for xx in list(range(x-r-1,x-rr))+list(range(x+rr,x+r+1)):
      if ((yy-y)**2+(xx-x)**2)<=r2:
        set_pixel(xx,yy,c)


def draw_line(x1,y1,x2,y2,c):
  width=x2-x1
  height=y2-y1
  if abs(width)>=abs(height):
    div=height/width
    for i in range(0,width,(width>0)*2-1):
      set_pixel(x1+i,y1+int(div*i+0.5),c)
  else:
    div=width/height
    for i in range(0,height,(height>0)*2-1):
      set_pixel(x1+int(div*i+0.5),y1+i,c)