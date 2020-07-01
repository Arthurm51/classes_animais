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
lagartoImg = pygame.image.load('imgs/lagarto.png')
porcoImg = pygame.image.load('imgs/porco.png')
macacoImg = pygame.image.load('imgs/macaco.png')
avestruzImg = pygame.image.load('imgs/avestruz.png')
jacareImg = pygame.image.load('imgs/jacare.png')
peixeImg = pygame.image.load('imgs/peixe.png')
tartarugaImg = pygame.image.load('imgs/tartaruga.png')
girafaImg = pygame.image.load('imgs/girafa.png')
leaoImg = pygame.image.load('imgs/leao.png')
elefanteImg = pygame.image.load('imgs/elefante.png')

background = pygame.image.load('imgs/zoo2.png')
gameicon = pygame.image.load('imgs/icon.png')
pygame.display.set_icon(gameicon)
pygame.display.set_caption('Mamiferos')

def mostraZoo( x, y):
    gamedisplay.blit(zoologoImg, (x,y) )

    
def sorteioImagem():
    img = random.randrange(0, 16)
    return img




def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((larguraTela/2, alturaTela/2))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def perdeu():
    message_display("Você perdeu!")

def placar(contador):
    font = pygame.font.SysFont(None,40)
    text = font.render("Pontuação: "+str(contador), True, black)
    gamedisplay.blit(text, (10, 30))

def game_loop():
    zooPosicaoX = larguraTela /2 - 50
    zooPosicaoY = alturaTela - 150
    movimentoX = 0
    zooLargura = 150
    zooAltura = 150
    posicaoImgY = -100
    larguraImg = 120
    alturaImg = 80
    imgSpeed = 7
    sorteio = 0
    ateimg = larguraTela - larguraImg
    posicaoImgX = random.randrange(0, ateimg)
    contador = 0

    while True:
        
        
        if sorteio == 0:
            img = sorteioImagem()
            sorteio = 1
        
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
        gamedisplay.blit(background, (0, 0))
        mostraZoo(zooPosicaoX,zooPosicaoY)
        placar(contador)
        
        if img == 0:
            gamedisplay.blit(porcoImg, (posicaoImgX,posicaoImgY) )
        elif img == 1:
            gamedisplay.blit(lagartoImg, (posicaoImgX,posicaoImgY) )
        elif img == 2:
            gamedisplay.blit(gatoImg, (posicaoImgX,posicaoImgY) )
        elif img == 3:
            gamedisplay.blit(galinhaImg, (posicaoImgX,posicaoImgY) )
        elif img == 4:
            gamedisplay.blit(cobraImg, (posicaoImgX,posicaoImgY) )
        elif img == 5:
            gamedisplay.blit(cachorroImg, (posicaoImgX,posicaoImgY) )
        elif img == 6:
            gamedisplay.blit(baleiaImg, (posicaoImgX,posicaoImgY) )
        elif img == 7:
            gamedisplay.blit(macacoImg, (posicaoImgX,posicaoImgY) )
        elif img == 8:
            gamedisplay.blit(avestruzImg, (posicaoImgX,posicaoImgY) )
        elif img == 9:
            gamedisplay.blit(jacareImg, (posicaoImgX,posicaoImgY) )
        elif img == 10:
            gamedisplay.blit(tartarugaImg, (posicaoImgX,posicaoImgY) )
        elif img == 11:
            gamedisplay.blit(elefanteImg, (posicaoImgX,posicaoImgY) )
        elif img == 12:
            gamedisplay.blit(peixeImg, (posicaoImgX,posicaoImgY) )
        elif img == 13:
            gamedisplay.blit(girafaImg, (posicaoImgX,posicaoImgY) )
        elif img == 14:
            gamedisplay.blit(leaoImg, (posicaoImgX,posicaoImgY) )
        

        posicaoImgY = posicaoImgY + imgSpeed
        

        if zooPosicaoX > larguraTela - zooLargura:
            zooPosicaoX = larguraTela-zooLargura
        elif zooPosicaoX < 0:
                zooPosicaoX = 0

        if zooPosicaoY + 50 < posicaoImgY + alturaImg:
            if zooPosicaoX < posicaoImgX and zooPosicaoX + zooLargura > posicaoImgX or posicaoImgX+larguraImg > zooPosicaoX and posicaoImgX+larguraImg < zooPosicaoX + zooLargura:
                if img == 1 or img == 3 or img == 4 or img == 8 or img == 9 or img == 10 or img == 12:
                    perdeu()
                elif img == 0 or img == 2 or img == 5 or img == 6 or img == 7 or img == 13 or img == 14 or img == 11:
                    contador = contador + 1
                    posicaoImgY = 0 - alturaImg
                    posicaoImgX = random.randrange(0,ateimg)
                    sorteio = 0
                    
                    
            elif posicaoImgY > alturaTela:
                if img == 0 or img == 2 or img == 5 or img == 6 or img == 7 or img == 13 or img == 14 or img == 11:
                    perdeu()
                elif img == 1 or img == 3 or img == 4 or img == 8 or img == 9 or img == 10 or img == 12:
                    contador = contador + 1
                    sorteio = 0
                    posicaoImgY = 0 - alturaImg
                    posicaoImgX = random.randrange(0,ateimg)  

        pygame.display.update()
        clock.tick(60)
        
game_loop()