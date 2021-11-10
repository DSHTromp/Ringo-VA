import pygame, sys
import pyautogui

# initialize the pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/Gideon assistant")
icon = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/waveform icon - Copy.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((420, 280),0,32)

font = pygame.font.SysFont(None, 20)

Duo = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/Google-Duo-3 - Copy.png").convert()
vol_up = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/volume up.png").convert()
vol_down = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/volume down.png").convert()
vol_mute = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/volume mute.png").convert()
setings = pygame.image.load("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Main/settings.png").convert()

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
    import Database


while True:

    screen.fill((0, 130, 255))

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(20, 20, 175, 100)
    button_2 = pygame.Rect(30, 150, 100, 100)
    button_3 = pygame.Rect(160, 150, 100, 100)
    button_4 = pygame.Rect(290, 150, 100, 100)
    button_5 = pygame.Rect(260, 20, 100, 100)
    if button_1.collidepoint((mx, my)):
        if click:
            Google_Duo()
    if button_2.collidepoint((mx, my)):
        if click:
            volume_down()
    if button_3.collidepoint((mx, my)):
        if click:
            volume_mute()
    if button_4.collidepoint((mx, my)):
        if click:
            volume_up()
    if button_5.collidepoint((mx, my)):
        if click:
            settings()
    pygame.draw.rect(screen, (0, 222, 200), button_1)
    pygame.draw.rect(screen, (0, 222, 200), button_2)
    pygame.draw.rect(screen, (0, 222, 200), button_3)
    pygame.draw.rect(screen, (0, 222, 200), button_4)
    pygame.draw.rect(screen, (0, 222, 200), button_5)
    screen.blit(Duo, [20, 20])
    screen.blit(vol_down, [30, 150])
    screen.blit(vol_mute, [160, 150])
    screen.blit(vol_up, [290, 150])
    screen.blit(setings, [260, 20])

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
