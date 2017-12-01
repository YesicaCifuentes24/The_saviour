import pygame, cons
from platform import Plataforma
import characters

class Nivel(object):
    # Lista de sprites usada en todos los niveles. Add or remove
    plataforma_lista = None
    enemigos_lista = None
    balas_lista = None
    addons = None
    fondo=pygame.transform.scale(pygame.image.load("files/enviroment/background_01.png"), (3000,600))
    mov_fondo=0

    def __init__(self, jugador):
        self.plataforma_lista = pygame.sprite.Group()
        self.enemigos_lista = pygame.sprite.Group()
        self.elementos_lista = pygame.sprite.Group()
        self.addons = pygame.sprite.Group()
        self.jugador = jugador

    # Actualizamos elementos en el nivel
    def update(self):
        self.plataforma_lista.update()
        self.enemigos_lista.update()
        self.elementos_lista.update()
        self.addons.update()

    def draw(self, pantalla):
        # Dibujamos fondo
        pantalla.fill(cons.BLACK)

        pantalla.blit(self.fondo, (0,0))
        self.plataforma_lista.draw(pantalla)
        self.enemigos_lista.draw(pantalla)
        self.elementos_lista.draw(pantalla)
        self.addons.draw(pantalla)

    def Mover_fondo(self, mov_x, mov_y):
        self.mov_fondo += mov_x
        for plataforma in self.plataforma_lista:
            plataforma.rect.x += mov_x
        for enemigo in self.enemigos_lista:
            enemigo.rect.x += mov_x
        for addon in self.addons:
            addon.rect.x += mov_x

        self.mov_fondo += mov_y
        for plataforma in self.plataforma_lista:
            plataforma.rect.y += mov_y
        for enemigo in self.enemigos_lista:
            enemigo.rect.y += mov_y
        for addon in self.addons:
            addon.rect.y += mov_y
        for elemento in self.elementos_lista:
            if(not elemento.bloqueado):
                elemento.rect.y += mov_y


class Nivel_01(Nivel):

    def __init__(self, jugador):
        super().__init__(jugador)
        self.limite=-3000
        self.enemigos_lista=pygame.sprite.Group()
        self.addons = pygame.sprite.Group()
        nivel = [
                    [330, 460, "muro_verde"],
                    [540, 320, "muro_verde"],
                    [630, 220, "muro_verde"],
                    [990, 120, "caja_x"],
                    [1129, 120, "caja_x"],
                    [1198, 120, "caja_x"],
                    [1267, 120, "caja_x"],
                    [1336, 120, "caja_x"],

                    [1120, -4, "caja_x"],
                    [1400, -60, "caja_x"],



                    [1120, 300, "caja"],

                    [1800, 30, "portal"],
                    [1800, 100, "caja_x"],

                    [2000, 200, "caja"],
                    [2150, 300, "caja"],
                    [2300, 400, "caja"],
                    [1500, cons.SCREEN_HEIGHT-100, "caja"],
                    [1800, cons.SCREEN_HEIGHT-100, "caja"],

        ]

        enemigos_config = [
                            characters.Enemigo1(1350,40, 50),
                            characters.Enemigo1(1450,cons.SCREEN_HEIGHT-80, 255),
                            characters.Enemigo2(1520,cons.SCREEN_HEIGHT-100, self.plataforma_lista),
                            characters.Enemigo2(1810, cons.SCREEN_HEIGHT - 100, self.plataforma_lista),
                            characters.Enemigo1(2350, cons.SCREEN_HEIGHT-80, 100),
                            characters.Enemigo2(2400, cons.SCREEN_HEIGHT - 80, self.plataforma_lista),

        ]
        for en in enemigos_config:
            self.enemigos_lista.add(en)
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.tipo=plataforma[2]
            bloque.get_from_tipo()
            bloque.jugador = self.jugador
            bloque.update_rect()
            if (plataforma[2] != "portal"):
                self.plataforma_lista.add(bloque)
            else:
                self.addons.add(bloque)

class Nivel_02(Nivel):

    def __init__(self, jugador):
        super().__init__(jugador)
        self.limite=-3000
        self.enemigos_lista=pygame.sprite.Group()
        nivel = [

        ]

        enemigos_config = [

        ]
        for en in enemigos_config:
            self.enemigos_lista.add(en)
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.tipo=plataforma[2]
            bloque.get_from_tipo()
            bloque.jugador = self.jugador
            bloque.update_rect()
