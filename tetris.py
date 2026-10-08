import pygame

pygame.init()
pygame.display.set_caption("tetris")
janela = pygame.display.set_mode((500, 700))

CELULA = 50
quadrado1 = pygame.Rect(200, 0, CELULA, CELULA)  # no trailing comma
color_white = (255, 255, 255)

CAIR = pygame.USEREVENT + 1
pygame.time.set_timer(CAIR, 500)  # fires every 500 ms

fixos = []

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
       
        if evento.type == CAIR:
            if quadrado1.bottom < 700:
                quadrado1.y += CELULA
                if quadrado1.y == 650:
                    quadrado2 = pygame.Rect(200, 0, CELULA, 50)
                    quadrado2.copy()
                    fixos.append(quadrado2)
                    print(fixos)
         
        if evento.type == pygame.KEYDOWN:
            match evento.key:
                case pygame.K_d:
                    if quadrado1.right < 500:
                        quadrado1.x += CELULA
                case pygame.K_a:
                    if quadrado1.left > 0:
                        quadrado1.x -= CELULA

    janela.fill((0, 0, 0))
    pygame.draw.rect(janela, color_white, quadrado1)
    pygame.display.flip()

pygame.quit()