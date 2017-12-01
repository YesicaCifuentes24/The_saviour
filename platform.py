import pygame
from sprite_functions import cargar_fondo
import cons

class Plataforma(pygame.sprite.Sprite):
    matriz=cargar_fondo("files/enviroment/tiles_spritesheet.png",72,72,True)
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.matriz[0][0]
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.saved = (x,y)

    def update_rect(self):
        self.rect = self.image.get_rect()
        self.rect.x=self.saved[0]
        self.rect.y=self.saved[1]

    def get_from_tipo(self):
        if(self.tipo == "caja"):
            self.image=self.matriz[0][6]
        elif(self.tipo == "caja_x"):
            self.image=self.matriz[0][11]
        elif(self.tipo == "muro_verde"):
            self.image=self.matriz[1][5]
        elif(self.tipo == "caja_adv"):
            self.image=self.matriz[0][2]
        elif(self.tipo == "portal"):
            self.image=self.matriz[6][5]
        else:
            self.image = self.matriz[0][0]