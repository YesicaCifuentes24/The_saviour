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
        self.balas_lista = pygame.sprite.Group()
        self.addons = pygame.sprite.Group()
        self.jugador = jugador

    # Actualizamos elementos en el nivel
    def update(self):
        self.plataforma_lista.update()
        self.enemigos_lista.update()
        self.elementos_lista.update()
        self.addons.update()
        self.balas_lista.update()

    def draw(self, pantalla):
        # Dibujamos fondo
        pantalla.fill(cons.BLACK)

        pantalla.blit(self.fondo, (0,0))
        self.plataforma_lista.draw(pantalla)
        self.enemigos_lista.draw(pantalla)
        self.elementos_lista.draw(pantalla)
        self.addons.draw(pantalla)
        self.balas_lista.draw(pantalla)

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

class Portal(Nivel):

    def __init__(self, jugador):
        super().__init__(jugador)
        self.limite=-100
        self.enemigos_lista=pygame.sprite.Group()
        self.addons = pygame.sprite.Group()
        self.fondo = pygame.transform.scale(pygame.image.load("files/enviroment/portal_background.png"), (800,600))
        nivel = [
            [330, 400, "muro_verde"],
            [540, 320, "muro_verde"],
            [200, cons.SCREEN_HEIGHT-20, "medkit"],
            [270, cons.SCREEN_HEIGHT-50, "portal_m"],
            [400, cons.SCREEN_HEIGHT-60, "backpack"],
            [460, cons.SCREEN_HEIGHT-50, "portal_b"],
        ]

        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.tipo=plataforma[2]
            bloque.get_from_tipo()
            bloque.jugador = self.jugador
            bloque.update_rect()
            if(bloque.tipo in ["medkit","backpack","portal_b","portal_m"]):
                self.addons.add(bloque)
            else:
                self.plataforma_lista.add(bloque)

    def draw(self, pantalla):
        pantalla.fill(cons.CYAN)
        pantalla.blit(self.fondo, (0, 0))
        self.plataforma_lista.draw(pantalla)
        self.addons.draw(pantalla)

class Nivel_02(Nivel):

    def __init__(self, jugador):
        super().__init__(jugador)
        self.limite=-3000
        self.enemigos_lista=pygame.sprite.Group()
        self.addons = pygame.sprite.Group()
        self.balas_lista=pygame.sprite.Group()
        self.fondo = pygame.transform.scale(pygame.image.load("files/enviroment/background_02.png"), (3000,600))
        nivel = [
                    [330, cons.SCREEN_HEIGHT-50, "spike"],
                    [350, cons.SCREEN_HEIGHT - 50, "spike"],
                    [370, cons.SCREEN_HEIGHT - 50, "spike"],
                    [390, cons.SCREEN_HEIGHT - 50, "spike"],

                    [490, cons.SCREEN_HEIGHT - 50, "spike"],
                    [510, cons.SCREEN_HEIGHT - 50, "spike"],
                    [530, cons.SCREEN_HEIGHT - 50, "spike"],

                    [800, cons.SCREEN_HEIGHT - 100, "caja_x"],
                    [872, cons.SCREEN_HEIGHT - 100, "caja_x"],
                    [944, cons.SCREEN_HEIGHT - 100, "caja_x"],
                    [1050, cons.SCREEN_HEIGHT - 50, "spike"],
                    [1088, cons.SCREEN_HEIGHT - 100, "caja_x"],
                    [1160, cons.SCREEN_HEIGHT - 100, "caja_x"],


                    [1240, cons.SCREEN_HEIGHT - 50, "spike"],
                    [1260, cons.SCREEN_HEIGHT - 50, "spike"],
                    [1280, cons.SCREEN_HEIGHT - 50, "spike"],
                    [1300, cons.SCREEN_HEIGHT - 50, "spike"],
                    [1304, cons.SCREEN_HEIGHT - 250, "caja_x"],

                    [1890, cons.SCREEN_HEIGHT - 72, "caja"],
                    [1962, cons.SCREEN_HEIGHT - (72*2), "caja"],
                    [2034, cons.SCREEN_HEIGHT - (72 * 3), "caja"],

                    [2034, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2054, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2074, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2094, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2114, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2134, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2154, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2174, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2194, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2214, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2234, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2254, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2274, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2294, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2314, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2334, cons.SCREEN_HEIGHT - 50, "spike"],
                    [2354, cons.SCREEN_HEIGHT - 50, "spike"],


                    [2300, cons.SCREEN_HEIGHT - (72 * 3), "caja"],
                    [2372, cons.SCREEN_HEIGHT - (72 * 2), "caja"],
                    [2444, cons.SCREEN_HEIGHT - (72), "caja"],


        ]

        enemigos_config = [
                            characters.Enemigo4(580, cons.SCREEN_HEIGHT - 100, 100, self),
                            characters.Enemigo1(990, cons.SCREEN_HEIGHT - (100+80), 45),
                            characters.Enemigo3(1085, cons.SCREEN_HEIGHT - 200, 100, self),
                            characters.Enemigo1(1800, cons.SCREEN_HEIGHT - (80), 100),
                            characters.Enemigo3(1895, cons.SCREEN_HEIGHT - (72+100), 100, self),
                            characters.Enemigo4(2040, cons.SCREEN_HEIGHT - (100+(72*3)), 100, self),
                            characters.Enemigo1(2900, cons.SCREEN_HEIGHT - (80), 80),
        ]
        for en in enemigos_config:
            self.enemigos_lista.add(en)
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.tipo=plataforma[2]
            bloque.get_from_tipo()
            bloque.jugador = self.jugador
            bloque.update_rect()
            if(plataforma[2] in ["portal","spike"]):
                self.addons.add(bloque)
            else:
                self.plataforma_lista.add(bloque)
    def draw(self, pantalla):
        # Dibujamos fondo
        pantalla.fill(cons.BLACK)
        pantalla.blit(self.fondo, (0,0))
        self.plataforma_lista.draw(pantalla)
        self.enemigos_lista.draw(pantalla)
        self.elementos_lista.draw(pantalla)
        self.addons.draw(pantalla)
        self.balas_lista.draw(pantalla)