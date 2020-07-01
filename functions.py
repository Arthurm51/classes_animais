def mostraZoo( x, y):
    import pygame
    larguraTela = 800
    alturaTela = 600
    zoologoImg = pygame.image.load('imgs/zoologo.png')
    gamedisplay = pygame.display.set_mode((larguraTela,alturaTela))
    a = gamedisplay.blit(zoologoImg, (x,y) )
    return a

def sorteioImagem():
    import random
    img = random.randrange(0, 16)
    return img

def text_objects(text,font):
    import pygame
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    import pygame
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((larguraTela/2, alturaTela/2))
    b = gamedisplay.blit(TextSurf, TextRect)
    return a
    pygame.display.update()
    time.sleep(2)
    game_loop()
    

def perdeu():
    import pygame
    c = message_display("Você perdeu!")
    return c

def placar(contador):
    import pygame
    larguraTela = 800
    alturaTela = 600
    gamedisplay = pygame.display.set_mode((larguraTela,alturaTela))
    black = (0,0,0)
    font = pygame.font.SysFont(None,40)
    text = font.render("Pontuação: "+str(contador), True, black)
    d = gamedisplay.blit(text, (10, 30))