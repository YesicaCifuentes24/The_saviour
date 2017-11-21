import pygame, cons
from platform import Plataforma


from player import Jugador

class Nivel(object):
    # Lista de sprites usada en todos los niveles. Add or remove
    plataforma_lista = None
    enemigos_lista = None
    balas_lista = None
    fondo=pygame.transform.scale(pygame.image.load("files/enviroment/background_01.png"), (3000,600))
    mov_fondo=0

    def __init__(self, jugador):
        self.plataforma_lista = pygame.sprite.Group()
        self.enemigos_lista = pygame.sprite.Group()
        self.elementos_lista = pygame.sprite.Group()
        self.jugador = jugador

    # Actualizamos elementos en el nivel
    def update(self):
        """ Actualiza todo lo que este en este nivel."""
        self.plataforma_lista.update()
        self.enemigos_lista.update()
        self.elementos_lista.update()

    def draw(self, pantalla):
        # Dibujamos fondo
        pantalla.fill(cons.BLUE)

        pantalla.blit(self.fondo, (0,0))
        self.plataforma_lista.draw(pantalla)
        self.enemigos_lista.draw(pantalla)
        self.elementos_lista.draw(pantalla)

    def Mover_fondo(self, mov_x, mov_y):
        self.mov_fondo += mov_x
        for plataforma in self.plataforma_lista:
            plataforma.rect.x += mov_x
        for enemigo in self.enemigos_lista:
            enemigo.rect.x += mov_x

        self.mov_fondo += mov_y
        for plataforma in self.plataforma_lista:
            plataforma.rect.y += mov_y
        for enemigo in self.enemigos_lista:
            enemigo.rect.y += mov_y
        for elemento in self.elementos_lista:
            if(not elemento.bloqueado):
                elemento.rect.y += mov_y


class Nivel_01(Nivel):

    def __init__(self, jugador):
        Nivel.__init__(self, jugador)
        self.limite=-3000
        self.enemigos_lista=pygame.sprite.Group()
        nivel = [
                    [472, 410, "muro_verde"],
                    [540, 320, "muro_verde"],
                    [630, 220, "muro_verde"],
                    [1060, 120, "caja_x"],
                    [1129, 120, "caja_x"],
                    [1198, 120, "caja_x"],
                    [1267, 120, "caja_x"],
                    [1336, 120, "caja_x"],
                    [1120, 300, "caja"],
                    [2000, 200, "caja"],
                    [2150, 300, "caja"],
                    [2300, 400, "caja"],
                    [1500, cons.SCREEN_HEIGHT-100, "caja"],
                    [1800, cons.SCREEN_HEIGHT-100, "caja"],

                 ]

        enemigos_config = [
                ]
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.tipo=plataforma[2]
            bloque.get_from_tipo()
            bloque.jugador = self.jugador
            bloque.update_rect()
            self.plataforma_lista.add(bloque)