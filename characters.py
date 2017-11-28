import pygame, cons
from sprite_functions import checkCollision, load_img, mirror_img


class Enemigo1(pygame.sprite.Sprite):
    dir = "L"
    cambio_x = -4
    run_right = []
    run_left = []
    counter_mov = 0
    sprite_sheet_counter_right = 0
    sprite_sheet_counter_left = 0
    sleep_image = 0
    def __init__(self, x, y, time_mov = 0):
        super().__init__()
        for i in range(1,11):
            self.run_right.append(pygame.transform.scale(pygame.image.load("files\characters\enemies\enemy1\Run"+ str(i) + ".png"),(40,80)))
            self.run_left.append(mirror_img(pygame.transform.scale(pygame.image.load("files\characters\enemies\enemy1\Run" + str(i) + ".png"),(40, 80))))

        self.image = self.run_right[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time_mov = time_mov

    def change_direction(self):
        if(self.dir == "L"):
            self.dir = "R"
            self.cambio_x = 4
        else:
            self.dir = "L"
            self.cambio_x = -4

    def update(self):
        if(self.counter_mov >= self.time_mov):
            self.counter_mov = 0
            self.change_direction()
        else:
            self.counter_mov+=1
            self.rect.x += self.cambio_x
            if (self.dir == "R"):
                self.sprite_sheet_counter_left=0
                if(self.sprite_sheet_counter_right >= 9):
                    self.sprite_sheet_counter_right=0
                else:
                    if(self.sleep_image >= 2):
                        self.sleep_image = 0
                        self.sprite_sheet_counter_right+=1
                        self.image = self.run_right[self.sprite_sheet_counter_right]
                    else:
                        self.sleep_image+=1
            else:
                self.sprite_sheet_counter_right=0
                if (self.sprite_sheet_counter_left >= 9):
                    self.sprite_sheet_counter_left = 0
                else:
                    if (self.sleep_image >= 2):
                        self.sleep_image = 0
                        self.sprite_sheet_counter_left += 1
                        self.image = self.run_left[self.sprite_sheet_counter_left]
                    else:
                        self.sleep_image+=1



class Kunai(pygame.sprite.Sprite):
    cambio_x = 8
    dir = "R"
    nivel = None
    def __init__(self, direccion, x,y):
        super().__init__()
        self.dir = direccion
        self.image = pygame.transform.scale(pygame.image.load("files\characters\player\Kunai.png"), (80,20))
        self.image_r = pygame.transform.scale(pygame.image.load("files\characters\player\Kunai.png"), (80,20))
        self.image_l = mirror_img(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if(self.dir == "R"):
            self.image = self.image_r
            self.rect.x += self.cambio_x
        else:
            self.image = self.image_l
            self.rect.x -= self.cambio_x


class Jugador(pygame.sprite.Sprite):

    cambio_x = 0
    cambio_y = 0

    #Tamaño para resizear el sprite
    height = 100
    weight = 60
    # Lista de todos los sprites contra los que podemos botar
    nivel = None
    run_right = []
    run_left = []
    idle_right = []
    idle_left = []
    dir = "R"
    sprite_sheet_counter_right = 0
    sprite_sheet_counter_left = 0
    # -- Métodos
    def __init__(self):
        """ Función Constructor  """

        #  -- Llama al constructor padre
        super().__init__()

        # Crea una imagen del bloque y lo rellena con color rojo.
        # También podríamos usar una imagen guardada en disco

        for i in range(0,10):
            self.run_right.append(load_img("files/characters/player/Run__00"+str(i)+".png", self.weight,self.height))
            self.run_left.append(mirror_img(load_img("files/characters/player/Run__00"+str(i)+".png", self.weight,self.height)))

        self.idle_right.append(load_img("files/characters/player/Idle__000.png", self.weight, self.height))
        self.idle_left.append(mirror_img(load_img("files/characters/player/Idle__000.png", self.weight, self.height)))

        self.image = self.run_left[0]

        # Establecemos una referencia hacia la imagen rectangular
        self.rect = self.image.get_rect()

    def update(self):
        """ Desplazamos al protagonista. """
        # Gravedad
        self.calc_grav()

        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x

        if(self.dir == "R" and self.cambio_x > 0):
            self.sprite_sheet_counter_left = 0
            if(self.sprite_sheet_counter_right >= 9):
                self.sprite_sheet_counter_right = 0
            else:
                self.sprite_sheet_counter_right+=1
                self.image = self.run_right[self.sprite_sheet_counter_right]
        elif(self.dir == "L" and self.cambio_x < 0):
            self.sprite_sheet_counter_right = 0
            if (self.sprite_sheet_counter_left >= 9):
                self.sprite_sheet_counter_left = 0
            else:
                self.sprite_sheet_counter_left += 1
                self.image = self.run_left[self.sprite_sheet_counter_left]

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right

        # Desplazar arriba/abajo
        self.rect.y += self.cambio_y

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        for bloque in lista_impactos_bloques:

            # Restablecemos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom

            # Detenemos nuestro movimiento vertical
            self.cambio_y = 0

    def calc_grav(self):
        """ Calculamos el efecto de la gravedad. """
        if self.cambio_y == 0:
            self.cambio_y = 1
        else:
            self.cambio_y += .35

        # Observamos si nos encontramos sobre el suelo.
        if self.rect.y >= cons.SCREEN_HEIGHT - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = cons.SCREEN_HEIGHT - self.rect.height

    def saltar(self):
        """ Llamado cuando el usuario pulsa el botón de 'saltar'. """

        # Descendemos un poco y observamos si hay una plataforma debajo nuestro.
        # Descendemos 2 píxels (con una plataforma que está  descendiendo, no funciona bien
        # si solo descendemos uno).
        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        self.rect.y -= 2

        # Si está listo para saltar, aumentamos nuestra velocidad hacia arriba
        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= cons.SCREEN_HEIGHT:
            self.cambio_y = -10

    # Movimiento controlado por el protagonista
    def ir_izquierda(self):
        """ Es llamado cuando el usuario pulsa la flecha izquierda """
        self.dir = "L"
        self.cambio_x = -6

    def ir_derecha(self):
        """ Es llamado cuando el usuario pulsa la flecha derecha """
        self.dir = "R"
        self.cambio_x = 6

    def stop(self):
        """ Es llamado cuando el usuario abandona el teclado """
        self.cambio_x = 0