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

        pj = pygame.sprite.Group()
        pj.add(player)

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

            # Update the player.
            active_sprite_list.update()

            # Update items in the level
            current_level.update()

            # If the player gets near the right side, shift the world left (-x)
            pj.update()
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            current_level.draw(screen)
            active_sprite_list.draw(screen)
            pj.draw(screen)


            pygame.display.flip()

        self.go_menu()




def xd():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
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
    player = characters.Jugador
    current_level = levels.Nivel_01(player)
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()