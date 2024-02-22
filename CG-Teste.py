import sys
import pygame

pygame.init()

#Configurações da tela
largura = 800
altura = 600 

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Amanda", True, BRANCO)
#texto_react = texto.get_rect(center = (largura/2, altura/2)) #Centro 
#texto_react = texto.get_rect(center = (725,575)) #Centro direito
#texto_react = texto.get_rect(center = (75,300)) #Centro esquerdo
#texto_react = texto.get_rect(center = (largura/2, 25)) #Topo
#texto_react = texto.get_rect(center = (75,25)) #Canto superior esquerdo
#texto_react = texto.get_rect(center = (725,25)) #Canto superior direito
#texto_react = texto.get_rect(center = (725,575)) #Canto inferior direito
#texto_react = texto.get_rect(center = (75,575)) #Canto inferior esquerdo
#texto_react = texto.get_rect(center = (400,575)) #centro inferior

#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(PRETO)
    tela.blit(texto, texto_react)
    pygame.display.flip()