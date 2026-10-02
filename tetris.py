import pygame

pygame.init()
rodando = True
pygame.display.set_caption("tetris")

janela = pygame.display.set_mode((500, 700))
quadrado1=  pygame.Rect(50, 50, 50, 50),

color_white = (255, 255, 255)

def abaixar(a):
    for abaixando in range(1, 10):
        a["quadrado1"] -= 50
        return a

while rodando:  
    janela.fill((0, 0, 0))

    pygame.draw.rect(janela, color_white, quadrado1)

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
         
        if evento.type == pygame.KEYDOWN: 
            match evento.key:
                case pygame.K_d:
                    quadrado1.d += 50
                case pygame.K_a:
                    quadrado1.x -= 50
pygame.quit()



