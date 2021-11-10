import pygame, sys
import pyautogui
import regform

# initialize the pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/Gideon assistant")
icon = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/waveform icon - Copy.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 480),0,32)

font = pygame.font.SysFont(None, 20)
Background = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/1920x1080_triangle-solid-black-gold-4k-abstract.png").convert()

Duo = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/Google-duo Big.png").convert()
volume_Ctrl = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/maxresdefault.png").convert()
setings = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/settings big.png").convert()

def draw_text (text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False


def Google_Duo():
    print("Duo Button pressed")
    pyautogui.hotkey("Alt", "Tab")


def volume_up():
    pyautogui.press("volumeup")


def volume_down():
    pyautogui.press("volumedown")


def volume_mute():
    pyautogui.press("volumemute")


def settings():
    regform.main()


while True:

    screen.blit(Background, [0, 0])

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(340, 80, 740, 416)
    button_2 = pygame.Rect(1180, 98, 380, 380)
    button_3 = pygame.Rect(1140, 600, 360, 320)
    button_4 = pygame.Rect(780, 600, 360, 320)
    button_5 = pygame.Rect(420, 600, 360, 320)
    if button_1.collidepoint((mx, my)):
        if click:
            Google_Duo()
    if button_2.collidepoint((mx, my)):
        if click:
            settings()
    if button_3.collidepoint((mx, my)):
        if click:
            volume_up()
    if button_4.collidepoint((mx, my)):
        if click:
            volume_down()
    if button_5.collidepoint((mx, my)):
        if click:
            volume_mute()

    pygame.draw.rect(screen, (255, 0, 0), button_1)
    pygame.draw.rect(screen, (255, 0, 0), button_2)
    pygame.draw.rect(screen, (255, 0, 0), button_3)
    pygame.draw.rect(screen, (255, 0, 0), button_4)
    pygame.draw.rect(screen, (255, 0, 0), button_5)
    screen.blit(Duo, [340, 80])
    screen.blit(volume_Ctrl, [420, 600])
    screen.blit(setings, [1180, 98])


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
