def sorteioImagem():
    import random
    img = random.randrange(0, 16)
    return img

def sorteioClasse(x, y):
    import random
    imgClasse = random.randrange(0, 5)
    return imgClasse

def mostraZoo( x, y):
    imgClasse = sorteioClasse(x, y)
    return imgClasse

def text_objects(text,font):
    import pygame
    white = (255,255,255)
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

