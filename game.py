import pygame

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


