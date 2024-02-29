import sys
import pygame
import random

pygame.init()

#Configurações da tela
largura = 800
altura = 600 

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
ROSA = (255, 0, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Amanda", True, BRANCO)
texto_rect = texto.get_rect(center = (largura/2, altura/2)) #Centro 
#texto_rect = texto.get_rect(center = (725,575)) #Centro direito
#texto_rect = texto.get_rect(center = (75,300)) #Centro esquerdo
#texto_rect = texto.get_rect(center = (largura/2, 25)) #Topo
#texto_rect = texto.get_rect(center = (75,25)) #Canto superior esquerdo
#texto_rect = texto.get_rect(center = (725,25)) #Canto superior direito
#texto_rect = texto.get_rect(center = (725,575)) #Canto inferior direito
#texto_rect = texto.get_rect(center = (75,575)) #Canto inferior esquerdo
#texto_rect = texto.get_rect(center = (400,575)) #centro inferior
#texto_rect = texto.get_rect() #Canto-Superior-Esquerdo
#texto_rect.left = 0
#texto_rect.top = 0
#texto_rect = texto.get_rect() #Canto-Superior-Direito
#texto_rect.right = 800
#texto_rect.top = 0
#texto_rect = texto.get_rect() #Meio-Direito
#texto_rect.right = 800
#texto_rect.bottom = 300
#texto_rect = texto.get_rect() #Meio-Esquerdo
#texto_rect.left = 0
#texto_rect.bottom = 300
#texto_rect = texto.get_rect() #Conto-Inferior-Direito
#texto_rect.right = 800
#texto_rect.bottom= 600

clock = pygame.time.Clock() #tempo do processamento do nome
#velocidade_x = 1
#velocidade_y = 1

velocidade_x = random.randint(-1,1)
velocidade_y = random.randint(-1,1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1,1)
while velocidade_y == 0:
    velocidade_y = random.randint(-1,1)
    
#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    texto_rect.x += velocidade_x #+= é encremento, cada loop ele soma 1
    texto_rect.y += velocidade_y

    if texto_rect.right >= largura: #não pode colocar dentro do if, está me loop. 
        velocidade_x = -velocidade_x 
        texto = fonte.render("Amanda", True, VERMELHO)
        velocidade_y = random.randint(-1,1)
    if texto_rect.left <= 0: #não pode colocar dentro do if, está me loop. 
        velocidade_x = -velocidade_x 
        texto = fonte.render("Amanda", True, ROSA)
        velocidade_y = random.randint(-1,1)
    if texto_rect.bottom  >= altura:# quando o bottom for maior ou igual a 600 ou o top for menor ou igual a 0
        velocidade_y = -velocidade_y 
        texto = fonte.render("Amanda", True, AZUL)
        velocidade_x = random.randint(-1,1)
    if texto_rect.top <= 0:# quando o bottom for maior ou igual a 600 ou o top for menor ou igual a 0
        velocidade_y = -velocidade_y 
        texto = fonte.render("Amanda", True, VERDE)
        velocidade_x = random.randint(-1,1)
        
    
    clock.tick(220) #tempo
    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()