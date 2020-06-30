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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    mostraZoo(400,400)
    pygame.display.update()
    clock.tick(60)


