import pygame, sys
import pyautogui
from tkinter import *
from time import sleep

# initialize the pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Gideon assistant')
icon = pygame.image.load('waveform icon - Copy.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1920, 1080),0,32)
root = Tk()

font = pygame.font.SysFont(None, 20)

Duo = pygame.image.load("Google-Duo-3 - Copy.png").convert()


def draw_text (text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False


def main_menu():
    while True:

        screen.fill((0, 222, 255))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(20, 20, 175, 100)
        button_2 = pygame.Rect(20, 140, 190, 80)
        if button_1.collidepoint((mx, my)):
            if click:
                Google_Duo()
        if button_2.collidepoint((mx, my)):
            if click:
                pass
        pygame.draw.rect(screen, (0, 222, 200), button_1)
        pygame.draw.rect(screen, (0, 222, 200), button_2)
        screen.blit(Duo, [20, 20])

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

        horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
        horizontal.pack
        pygame.display.update()
        mainClock.tick(60)


def Google_Duo():

    print("Duo Button pressed")
    pyautogui.hotkey("Alt", "Tab")



root.mainloop()
main_menu()
