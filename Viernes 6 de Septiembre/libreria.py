import pygame
import math

NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
BLANCO = [255,255,255]

def plano(pantalla,ALTO,ANCHO,origen,color=BLANCO):
    ox = origen[0]
    oy = origen[1]
    pygame.draw.line(pantalla,color,[ox,0],[ox,ALTO])
    pygame.draw.line(pantalla,color,[0,oy],[ANCHO,oy])
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
    xr=int(-(pto[0]*math.cos(angulo))+(pto[1]*math.sin(angulo)))
    yr=int((pto[0]*math.sin(angulo))+(pto[1]*math.cos(angulo)))
    return [xr,yr]

def linea(pantalla,inicio,final,color=BLANCO):
    pygame.draw.line(pantalla,color,inicio,final,1)
    pygame.display.flip()

def escala(pto,scalar):
    sx=pto[0]*scalar[0]
    sy=pto[1]*scalar[1]
    return [sx, sy]

def Triangulo(pantalla,VERDE,puntos):
    pygame.draw.polygon(pantalla,VERDE,puntos, 1)
    pygame.display.flip()
