import pygame
import levels
import cons
import characters
import main


class Menu:
    lista = []
    tam_font = 32
    font_path = 'files/fonts/coders_crux.ttf'
    font = pygame.font.Font
    dest_surface = pygame.Surface
    start=(0,0)
    def __init__(self, datos, surface, position):
        self.lista = datos
        self.dest_surface = surface
        self.start = position
        self.color_n = (255,0,0)
        self.color_s = (0,255,0)
        self.cursor = 0
        self.imagem = pygame.image.load("files/enviroment/menu.jpg")
        self.imagem = pygame.transform.scale(self.imagem, (800, 600))


    def get_color(self):
        l_colores=[]
        for i in range(len(self.lista)):
            l_colores.append(self.color_n)
        l_colores[self.cursor] = self.color_s
        return l_colores

    def draw_menu(self):
        y=self.start[1]
        self.dest_surface.blit(self.imagem, [0,0])
        l = self.get_color()
        for i in range(len(self.lista)):
            tipo = pygame.font.Font(self.font_path, self.tam_font)
            text = tipo.render(self.lista[i] , 1 , l[i])
            self.dest_surface.blit(text, (self.start[0],y))
            y+=50
        pygame.display.flip()

class game():

    def go_menu(self):
        pygame.mixer.quit()
        pygame.display.quit()
        pygame.font.quit()
        main.main()

    def start(self):
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init()

        size = [cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Platformer with sprite sheets")

        # Create all the levels
        level_list = []

        # Set the current level
        active_sprite_list = pygame.sprite.Group()
        current_level_no = 0

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        player = characters.Jugador()
        player.rect.x = 0 + player.rect.left + 100
        player.rect.y = cons.SCREEN_HEIGHT - player.rect.bottom - 20

        player_group = pygame.sprite.Group()
        player_kunai = pygame.sprite.Group()
        player_group.add(player)

        current_level = levels.Nivel_01(player)
        player.nivel = current_level
        # -------- Main Program Loop -----------
        while not done:
            for evento in pygame.event.get():  # El usuario realizó alguna acción
                if evento.type == pygame.QUIT:  # Si el usuario hizo click en salir
                    self.go_menu()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        player.ir_izquierda()
                    if evento.key == pygame.K_RIGHT:
                        player.ir_derecha()
                    if evento.key == pygame.K_UP:
                        player.saltar()

                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT and player.cambio_x < 0:
                        player.stop()
                    if evento.key == pygame.K_RIGHT and player.cambio_x > 0:
                        player.stop()
                    if evento.key == pygame.K_SPACE:
                        new_kunai = characters.Kunai(player.dir, player.rect.x, player.rect.y + 40)
                        player_group.add(new_kunai)
                        player_kunai.add(new_kunai)

            ## Checkeo de colisiones
            for element in current_level.plataforma_lista:
                pygame.sprite.spritecollide(element, player_kunai, True)


            if player.rect.x >= 500:
                dif = player.rect.x - 500
                player.rect.x = 500
                current_level.Mover_fondo(-dif, 0)


            if player.rect.x <= 120:
                dif = 120 - player.rect.x
                player.rect.x = 120
                current_level.Mover_fondo(dif, 0)


            pos_actual = player.rect.x + current_level.mov_fondo
            if pos_actual < current_level.limite:
                player.rect.x = 120
                print("pasaste")

            # Update the player.
            active_sprite_list.update()

            # Update items in the level
            current_level.update()
            player_group.update()
            # If the player gets near the right side, shift the world left (-x)

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            current_level.draw(screen)
            active_sprite_list.draw(screen)
            player_group.draw(screen)


            pygame.display.flip()

        self.go_menu()