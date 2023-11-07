import pygame
import json
import time

lrc = []
lrcTrack = []

def LoadSaikoLrc(file:str):
    global lrc,lrcTrack
    with open(file+'.saikolrc','r',encoding='utf-8') as f:
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
# 我实在不知道怎么写了
# 这个代码先挂在这里了

def ConsoleMain(file,SampleRate=64000):
    pygame.mixer.init()
    pygame.mixer.music.load(file+'.wav')
    pygame.mixer.music.set_volume(1.)
    pygame.mixer.music.play()

    start_time = time.time()
    pointer = 0
    print()
    while pygame.mixer.music.get_busy():
        if pointer < len(lrcTrack):
            if time.time()-start_time >= lrcTrack[pointer]/SampleRate:
                print(lrc[pointer])
                pointer+=1
        pass

if __name__ == '__main__':
    import sys
    LoadSaikoLrc(sys.argv[1])
    ConsoleMain(sys.argv[1])