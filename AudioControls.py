import pygame

pygame.mixer.init()

def __play__(fileName):
    if fileName == "": 
        print("File not found")
        return
    print(fileName)
    pygame.mixer.music.load(fileName)
    pygame.mixer.music.play(-1)

def __pause__():
    pygame.mixer.music.pause()

def __unpause__():
    pygame.mixer.music.unpause()

def __stop__():
    pygame.mixer.music.stop()

def __length__(fileName):
    a = pygame.mixer.Sound(fileName)
    print(a.get_length())
    return a.get_length()
