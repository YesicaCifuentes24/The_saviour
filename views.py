import pygame
import levels
import cons
import characters
import main
from sprite_functions import checkCollision


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
    current_nivel_no = 1
    def go_menu(self):
        pygame.mixer.quit()
        pygame.display.quit()
        pygame.font.quit()
        main.main()

    def draw_status(self, screen, player, ticks):
        tipo = pygame.font.Font('files/fonts/coders_crux.ttf', 20)
        text = tipo.render("Vida: ", 1, cons.WHITE)
        screen.blit(text, (20, cons.SCREEN_HEIGHT + 20))
        if (player.blood > 75):
            color = cons.GREEN
        elif (player.blood > 50):
            color = cons.YELLOW
        else:
            color = cons.RED
        pygame.draw.rect(screen, color, (60, cons.SCREEN_HEIGHT + 20, player.blood, 10))

        tipo = pygame.font.Font('files/fonts/coders_crux.ttf', 20)
        text = tipo.render("Kunais restantes: ", 1, cons.WHITE)
        screen.blit(text, (190, cons.SCREEN_HEIGHT + 20))

        if(player.kunais >= 15):
            color = cons.GREEN
        elif(player.kunais >= 10):
            color = cons.YELLOW
        else:
            color = cons.RED

        tipo = pygame.font.Font('files/fonts/coders_crux.ttf', 20)
        text = tipo.render(str(player.kunais), 1, color)
        screen.blit(text, (320, cons.SCREEN_HEIGHT + 20))

        tipo = pygame.font.Font('files/fonts/coders_crux.ttf', 20)
        text = tipo.render("Tiempo restante: ", 1, cons.WHITE)
        screen.blit(text, (350, cons.SCREEN_HEIGHT + 20))

        remaining = 120000 - ticks
        seconds = (remaining / 1000) % 60
        seconds = int(seconds)
        minutes = (remaining / (1000 * 60)) % 60
        minutes = int(minutes)

        tipo = pygame.font.Font('files/fonts/coders_crux.ttf', 20)
        text = tipo.render(str(minutes) + ":" + str(seconds), 1, cons.WHITE)
        screen.blit(text, (470, cons.SCREEN_HEIGHT + 20))

    def game_over(self, screen):
        screen.fill(cons.BLACK)
        tipo = pygame.font.Font('files/fonts/coders_crux.ttf', 200)
        text = tipo.render("GAME OVER", 1, cons.RED)
        screen.blit(text, (60, cons.SCREEN_HEIGHT / 2 - 20))
        tipo = pygame.font.Font('files/fonts/coders_crux.ttf', 40)
        text = tipo.render("Press e to continue", 1, cons.RED)
        screen.blit(text, (cons.SCREEN_WIDTH / 2 - 150, cons.SCREEN_HEIGHT / 2 + 100))

    def winner(self,screen):
        screen.fill(cons.BLACK)
        tipo = pygame.font.Font('files/fonts/coders_crux.ttf', 200)
        text = tipo.render("GANASTE !!", 1, cons.GREEN)
        screen.blit(text, (60, cons.SCREEN_HEIGHT / 2 - 20))
        tipo = pygame.font.Font('files/fonts/coders_crux.ttf', 40)
        text = tipo.render("Press e to continue", 1, cons.GREEN)
        screen.blit(text, (cons.SCREEN_WIDTH / 2 - 150, cons.SCREEN_HEIGHT / 2 + 100))

    def start(self):
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init()

        size = [cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT + 100]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("The saviour - LVL 1")

        # Create all the levels
        level_list = []

        # Set the current level
        active_sprite_list = pygame.sprite.Group()

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
        in_portal=False
        winner = False
        sound_die = True
        # -------- Main Program Loop -----------
        while not done:
            if(player.blood <= 0):
                player.blood=0
                if(sound_die):
                    sound = pygame.mixer.Sound("files/sounds/die.ogg")
                    sound.play()
                    sound_die=False
                player.die()

            if(player.muerto):
                self.game_over(screen)

            if(self.current_nivel_no == 3 and len(current_level.enemigos_lista) == 0):
                winner = True
            else:
                print("Epa", len(current_level.enemigos_lista))

            if(winner):
                self.winner(screen)

            for evento in pygame.event.get():  # El usuario realizó alguna acción
                if evento.type == pygame.QUIT:  # Si el usuario hizo click en salir
                    self.go_menu()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT and player.blood > 0:
                        player.ir_izquierda()
                    if evento.key == pygame.K_RIGHT and player.blood > 0:
                        player.ir_derecha()
                    if evento.key == pygame.K_UP and player.blood > 0:
                        player.saltar()

                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT and player.cambio_x < 0:
                        player.stop()
                    if evento.key == pygame.K_RIGHT and player.cambio_x > 0:
                        player.stop()
                    if evento.key == pygame.K_SPACE:
                        if(player.kunais > 0 and player.blood > 0):
                            new_kunai = characters.Kunai(player.dir, player.rect.x, player.rect.y + 40)
                            player_group.add(new_kunai)
                            player_kunai.add(new_kunai)
                            player.kunais-=1
                    if evento.key == pygame.K_e:
                        if(player.muerto):
                            self.go_menu()
                        if(winner):
                            self.go_menu()

                        for elementx in current_level.addons:
                            if(checkCollision(elementx,player)):
                                if(elementx.tipo == "portal"):
                                    current_level = levels.Portal(player)
                                    player.nivel = current_level
                                    in_portal = True
                                elif(elementx.tipo == "medkit"):
                                    player.blood = 100
                                    current_level.addons.remove(elementx)
                                elif(elementx.tipo == "backpack"):
                                    player.kunais += 30
                                    current_level.addons.remove(elementx)
                                elif(elementx.tipo == "portal_b"):
                                    current_level = levels.Boss_level(player)
                                    player.nivel = current_level
                                    self.current_nivel_no = 3
                                elif(elementx.tipo == "portal_m"):
                                    player.blood=0



            ## Checkeo de colisiones
            for element in current_level.plataforma_lista:
                pygame.sprite.spritecollide(element, player_kunai, True)
                pygame.sprite.spritecollide(element, current_level.balas_lista, True)
            for elementx in current_level.addons:
                if (checkCollision(elementx, player)):
                    if (elementx.tipo == "spike"):
                        player.blood = 0
                        player.die()

            for bala_en in current_level.balas_lista:
                if(checkCollision(player,bala_en)):
                    if(bala_en.tipo == "bone"):
                        player.blood -= 15
                    elif(bala_en.tipo == "blast"):
                        player.blood -= 30
                    elif (bala_en.tipo == "blast_boss"):
                        player.blood -= 70
                    current_level.balas_lista.remove(bala_en)


            for enemigo in current_level.enemigos_lista:
                if (checkCollision(player, enemigo)):
                    print("choca")
                    sound = pygame.mixer.Sound("files/sounds/hit.ogg")
                    sound.play()
                    player.blood -= 2
                if (enemigo.blood <= 0):
                    current_level.enemigos_lista.remove(enemigo)
                for bala in player_kunai:
                    if(checkCollision(bala,enemigo)):
                        player_kunai.remove(bala)
                        player_group.remove(bala)
                        enemigo.blood -= 50





            if player.rect.x >= 500:
                dif = player.rect.x - 500
                player.rect.x = 500
                current_level.Mover_fondo(-dif, 0)


            if player.rect.x <= 120:
                dif = 120 - player.rect.x
                player.rect.x = 120
                current_level.Mover_fondo(dif, 0)

            #if(pygame.time.get_ticks() >= 60000):
            #    print("game over")

            pos_actual = player.rect.x + current_level.mov_fondo
            if pos_actual < current_level.limite:
                player.rect.x = 120
                if(in_portal):
                    current_level = levels.Nivel_01(player)
                    player.nivel = current_level
                    player.rect.x = 1825
                    player.rect.y = 20
                    in_portal=False
                else:
                    self.current_nivel_no+=1
                    if(self.current_nivel_no == 1):
                        current_level = levels.Nivel_01(player)
                        player.nivel = current_level
                    elif(self.current_nivel_no == 2):
                        current_level = levels.Nivel_02(player)
                        player.nivel = current_level
                    elif(self.current_nivel_no == 3):
                        current_level = levels.Boss_level(player)
                        player.nivel = current_level

            if(pygame.time.get_ticks() >= 120000):
                player.blood=0

            # Update the player.
            if(not player.muerto and not winner):
                active_sprite_list.update()

                # Update items in the level
                current_level.update()
                player_group.update()
                # If the player gets near the right side, shift the world left (-x)

                # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
                current_level.draw(screen)
                active_sprite_list.draw(screen)
                player_group.draw(screen)
                self.draw_status(screen,player, pygame.time.get_ticks())
            clock.tick(60)

            pygame.display.flip()

        self.go_menu()