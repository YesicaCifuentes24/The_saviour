import pygame
import views, sys
import cons

def end_execution():
    pygame.mixer.quit()
    pygame.display.quit()
    pygame.font.quit()

def main():
    pygame.display.init()
    pygame.font.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((cons.SCREEN_WIDTH,cons.SCREEN_HEIGHT))
    screen.fill((51,51,51))
    m =views.Menu(['Iniciar juego','Controles', 'Salir'], screen, (cons.SCREEN_WIDTH/2-150,cons.SCREEN_HEIGHT/2+100))
    m.tam_font = 68
    m.draw_menu()
    pygame.display.flip()
    sound = pygame.mixer.Sound("files/sounds/menu.ogg")
    sound.play()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if(m.cursor >= len(m.lista)-1):
                        m.cursor=0
                    else:
                        m.cursor += 1
                if event.key == pygame.K_UP:
                    if(m.cursor <= 0):
                        m.cursor=len(m.lista)-1
                    else:
                        m.cursor -= 1
                if event.key == pygame.K_RETURN:
                    if m.cursor == 2:
                        end_execution()
                        sys.exit(0)
                    if m.cursor == 0:
                        print("Empieza el juego")
                        sound.stop()
                    if m.cursor == 1:
                        print("Menu help")
        m.draw_menu()

if __name__ == "__main__":
    main()
