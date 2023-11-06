import pygame
import json

lrc = []
lrcTrack = []

def LoadSaikoLrc(file:str):
    global lrc,lrcTrack
    with open(file,'r',encoding='utf-8') as f:
        tmp = json.loads(f.read())
        lrc = tmp[0]
        lrcTrack = tmp[1]

def Init():
    pygame.init()
    CirSize = (800,600)
    CirScreen = pygame.display.set_mode(CirSize)
    pygame.display.set_caption('さいこのCirclePlayer')
    HeadICO = pygame.image.load('res/player.ico')
    pygame.display.set_icon(HeadICO)

# TODO:awa
