#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
from snake.snake_game import snake_welcome
from spaceinvaders import *
from tetris.Tetris import tetris_game

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Arcade')
screen = pygame.display.set_mode((900, 500), 0, 32)

font = pygame.font.SysFont(None, 32)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        draw_text('Choose your game', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        smallfont = pygame.font.SysFont('Corbel', 35)

        text_space = smallfont.render('Space Invaders', True, (255,255,255))
        text_sanke = smallfont.render('Snake', True, (255,255,255))
        text_tetris = smallfont.render('Tetris', True, (255,255,255))

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        screen.blit(text_space, (350, 100))
        screen.blit(text_sanke, (350, 200))
        screen.blit(text_tetris, (350, 300))

        if button_1.collidepoint((mx, my)):

            if click:
                pygame.display.set_mode((800, 600), 0, 32)
                game = SpaceInvaders()
                game.main()

        if button_2.collidepoint((mx, my)):

            if click:
                snake_welcome()

        if button_3.collidepoint((mx, my)):

            if click:
                tetris_game()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


if __name__ == '__main__':
    try:
        main_menu()
    except Exception as e:
        print(e)