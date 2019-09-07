import pygame
from libreria import*


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([640,480])
    origen=[320,240]
    pto0=[0,100]
    pto1=[-100,200]
    plano(pantalla,480,640,origen)
    pygame.display.flip()
    angle=0
    pos =[]
    fin=False
    while not fin:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = event.pos
                    pygame.draw.circle(pantalla,VERDE,pos,2)
                    pygame.display.flip()
                if event.button == 4:
                    angle+=5
                    angulo_rotado = Cart_plano(rotacionHora(Plano_cart(pos,origen),angle),origen)
                    pygame.draw.circle(pantalla,VERDE,angulo_rotado,2)
                    pygame.display.flip()
                if event.button == 5:
                    angle+=5
                    angulo_rotado = Cart_plano(rotacionAnti(Plano_cart(pos,origen),angle),origen)
                    pygame.draw.circle(pantalla,AZUL,angulo_rotado,2)
                    pygame.display.flip()
