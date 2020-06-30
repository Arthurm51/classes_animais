import pygame
import time
import random

pygame.init()

larguraTela = 800
alturaTela = 600
gamedisplay = pygame.display.set_mode((larguraTela,alturaTela))
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
zoologoImg = pygame.image.load('imgs/zoologo.png')
baleiaImg = pygame.image.load('imgs/baleia.png')
cachorroImg = pygame.image.load('imgs/cachorro.png')
cobraImg = pygame.image.load('imgs/cobra.png')
galinhaImg = pygame.image.load('imgs/galinha.png')
gatoImg = pygame.image.load('imgs/gato.png')
homemImg = pygame.image.load('imgs/homem.png')
lagartoImg = pygame.image.load('imgs/lagarto.png')
macacoImg = pygame.image.load('imgs/macaco.png')
mulherImg = pygame.image.load('imgs/mulher.png')
porcoImg = pygame.image.load('imgs/porco.png')

def mostraZoo( x, y):
    gamedisplay.blit(zoologoImg, (x,y) )

def mostraBaleia( x, y):
    gamedisplay.blit(baleiaImg, (x,y) )

def mostraCachorro( x, y):
    gamedisplay.blit(cachorroImg, (x,y) )

def mostraCobra( x, y):
    gamedisplay.blit(cobraImg, (x,y) )

def mostraGalinha( x, y):
    gamedisplay.blit(galinhaImg, (x,y) )

def mostraGato( x, y):
    gamedisplay.blit(gatoImg, (x,y) )

def mostraHomem( x, y):
    gamedisplay.blit(homemImg, (x,y) )

def mostraLagarto( x, y):
    gamedisplay.blit(lagartoImg, (x,y) )

def mostraMacaco( x, y):
    gamedisplay.blit(macacoImg, (x,y) )

def mostraMulher( x, y):
    gamedisplay.blit(mulherImg, (x,y) )

def mostraPorco( x, y):
    gamedisplay.blit(porcoImg, (x,y) )


def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((larguraTela/2, alturaTela/2))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def perdeu():
    message_display("Você perdeu!")

def game_loop():
    zooPosicaoX = larguraTela /2 - 50
    zooPosicaoY = alturaTela - 150
    movimentoX = 0
    zooLargura = 150
    zooAltura = 150
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoX = -5
                elif event.key == pygame.K_RIGHT:
                    movimentoX = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movimentoX = 0

        zooPosicaoX = zooPosicaoX + movimentoX

        gamedisplay.fill(white)
        mostraZoo(zooPosicaoX,zooPosicaoY)

        if zooPosicaoX > larguraTela - zooLargura:
            zooPosicaoX = larguraTela-zooLargura
        elif zooPosicaoX < 0:
                zooPosicaoX = 0

        pygame.display.update()
        clock.tick(60)

game_loop()


