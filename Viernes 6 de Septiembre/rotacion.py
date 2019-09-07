import pygame
import math


NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
BLANCO = [255,255,255]

def plano(pantalla,ALTO,ANCHO,origen):
    ox = origen[0]
    oy = origen[1]
    pygame.draw.line(pantalla,BLANCO,[ox,0],[ox,ALTO])
    pygame.draw.line(pantalla,BLANCO,[0,oy],[ANCHO,oy])
    pygame.display.flip()

def rotacionAnti(pto,angulo):
    angulo = math.radians(angulo)
    xr=int((pto[0]*math.cos(angulo))-(pto[1]*math.sin(angulo)))
    yr=int((pto[0]*math.sin(angulo))+(pto[1]*math.cos(angulo)))
    return [xr,yr]

def Plano_cart(pto,origen):
    x = pto[0]-origen[0]
    y = origen[1]-pto[1]
    return [x,y]

def Cart_plano(pto,origen):
    x = pto[0]
    y = pto[1]
    xp = x + origen[0]
    yp = -y + origen[1]
    return [xp,yp]

def rotacionHora(pto,angulo):
    angulo = math.radians(angulo)
    xr=int((pto[0]*math.cos(angulo))-(pto[1]*math.sin(angulo)))
    yr=int((-pto[0]*math.sin(angulo))+(pto[1]*math.cos(angulo)))
    return [xr,yr]

def linea(pantalla,inicio,final):
    pygame.draw.line(pantalla,BLANCO,inicio,final,1)
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([640,480])
    origen=[320,240]
    pto0=[0,100]
    pto1=[-100,200]
    plano(pantalla,480,640,origen)
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.circle(pantalla,VERDE,event.pos,2)
                angulo_rotado = Cart_plano(rotacionAnti(Plano_cart(event.pos,origen),90),origen)
                pygame.draw.circle(pantalla,VERDE,angulo_rotado,2)
                pygame.display.flip()
