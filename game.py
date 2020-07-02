import pygame
import time
import random
from functions import sorteioImagem, sorteioClasse, mostraZoo, text_objects
pygame.init()
pedido = 0
larguraTela = 800
alturaTela = 600
gamedisplay = pygame.display.set_mode((larguraTela,alturaTela))
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)


aveImg = pygame.image.load('imgs/ave.png')
peixepImg = pygame.image.load('imgs/peixep.png')
mamiferoImg = pygame.image.load('imgs/mamifero.png')
anfibioImg = pygame.image.load('imgs/anfibio.png')
reptilImg = pygame.image.load('imgs/reptil.png')
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
sapoImg = pygame.image.load('imgs/sapo.png')
background = pygame.image.load('imgs/zoo2.png')
gameicon = pygame.image.load('imgs/icon.png')
pygame.display.set_icon(gameicon)
pygame.display.set_caption('Mamiferos')
'''
def message_display("Você perdeu!"):
    import pygame
    from game import message_display
    message_display("Você perdeu!")
'''
def message_display(text):
    import pygame
    import time
    from game import game_loop
    larguraTela = 800
    alturaTela = 600
    gamedisplay = pygame.display.set_mode((larguraTela,alturaTela))
    background = pygame.image.load('imgs/zoo2.png')
    gamedisplay.blit(background, (0, 0))
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((larguraTela/2, alturaTela/2))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    arquivo = open("jogadores.txt", "a")
    nome = input("Digite aqui seu nome: ")
    email = input("Digite aqui seu e-mail: ")
    arquivo.write("\nNome: "+ nome+ "\nE-mail: "+ email+ "\nPontuação: "+ "\n")
    time.sleep(2)
    game_loop()

def placar(contador):
    import pygame
    font = pygame.font.SysFont(None,40)
    text = font.render("Pontuação: "+str(contador), True, black)
    gamedisplay.blit(text, (10, 30))

def game_loop():
    
    import pygame
    import time
    import random
    pygame.mixer.music.load('imgs/fazendinha.mp3')
    pygame.mixer.music.play(-1)
    zooPosicaoX = larguraTela /2 - 50
    zooPosicaoY = alturaTela - 50
    movimentoX = 0
    zooLargura = 150
    zooAltura = 150
    posicaoImgY = -100
    larguraImg = 120
    alturaImg = 80
    imgSpeed = 5
    sorteio = 0
    ateimg = larguraTela - larguraImg
    posicaoImgX = random.randrange(0, ateimg)
    contador = 0
    
    while True:    
        if sorteio == 0:
            img = sorteioImagem()
            imgClasse = sorteioClasse(zooPosicaoX, zooPosicaoY)
            sorteio = 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoX = -8
                elif event.key == pygame.K_RIGHT:
                    movimentoX = 8

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movimentoX = 0

        zooPosicaoX = zooPosicaoX + movimentoX
        gamedisplay.fill(white)
        gamedisplay.blit(background, (0, 0))
        
        if imgClasse == 0:
            gamedisplay.blit(aveImg, (zooPosicaoX,zooPosicaoY) )
        elif imgClasse == 1:
            gamedisplay.blit(peixepImg, (zooPosicaoX,zooPosicaoY) )
        elif imgClasse == 2:
            gamedisplay.blit(mamiferoImg, (zooPosicaoX,zooPosicaoY) )
        elif imgClasse == 3:
            gamedisplay.blit(anfibioImg, (zooPosicaoX,zooPosicaoY) )
        elif imgClasse == 4:
            gamedisplay.blit(reptilImg, (zooPosicaoX,zooPosicaoY) )
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
        elif img == 15:
            gamedisplay.blit(sapoImg, (posicaoImgX,posicaoImgY) )
        
        posicaoImgY = posicaoImgY + imgSpeed
        
        if zooPosicaoX > larguraTela - zooLargura:
            zooPosicaoX = larguraTela-zooLargura
        elif zooPosicaoX < 0:
                zooPosicaoX = 0

        if zooPosicaoY + 50 < posicaoImgY + alturaImg:
            if zooPosicaoX < posicaoImgX and zooPosicaoX + zooLargura > posicaoImgX or posicaoImgX+larguraImg > zooPosicaoX and posicaoImgX+larguraImg < zooPosicaoX + zooLargura:
                if imgClasse == 2:
                    if img == 0 or img == 2 or img == 5 or img == 6 or img == 7 or img == 13 or img == 14 or img == 11:
                        contador = contador + 1
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        sorteio = 0
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1
                    else:
                        message_display("Você perdeu!")
                elif imgClasse == 0:
                    if img == 3 or img == 8:
                        contador = contador + 1
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        sorteio = 0
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1
                    else:
                        message_display("Você perdeu!")
                elif imgClasse == 1:
                    if img == 12:
                        contador = contador + 1
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        sorteio = 0
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1
                    else:
                        message_display("Você perdeu!")
                elif imgClasse == 3:
                    if img == 15:
                        contador = contador + 1
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        sorteio = 0
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1
                    else:
                        message_display("Você perdeu!")
                elif imgClasse == 4:
                    if img == 1 or img == 4 or img == 9 or img == 10:
                        contador = contador + 1
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        sorteio = 0
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1
                    else:
                        message_display("Você perdeu!")
            elif posicaoImgY > alturaTela:
                if imgClasse == 2:
                    if img == 0 or img == 2 or img == 5 or img == 6 or img == 7 or img == 13 or img == 14 or img == 11:
                        message_display("Você perdeu!")
                    else:
                        contador = contador + 1
                        sorteio = 0
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1
                elif imgClasse == 0:
                    if img == 3 or img == 8:
                        message_display("Você perdeu!")
                    else:
                        contador = contador + 1
                        sorteio = 0
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1
                elif imgClasse == 1:
                    if img == 12:
                        message_display("Você perdeu!")
                    else:
                        contador = contador + 1
                        sorteio = 0
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1
                elif imgClasse == 3:
                    if img == 15:
                        message_display("Você perdeu!")
                    else:
                        contador = contador + 1
                        sorteio = 0
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1
                elif imgClasse == 4:
                    if img == 1 or img == 4 or img == 9 or img == 10:
                        message_display("Você perdeu!")
                    else:
                        contador = contador + 1
                        sorteio = 0
                        posicaoImgY = 0 - alturaImg
                        posicaoImgX = random.randrange(0,ateimg)
                        if imgSpeed < 15:
                            imgSpeed = imgSpeed + 1

        pygame.display.update()
        clock.tick(60)
        
game_loop()