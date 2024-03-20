import pygame
import sys
from MecMovimento import MovendoTexto 

class Game:
    def __init__(self):
        pygame.init()
        self.largura = 800 #Define a largura da janela
        self.altura = 600 #Define a altura da janela
        self.tela = pygame.display.set_mode((self.largura, self.altura)) #Criar a janela de acordo com a largura e altura
        pygame.display.set_caption("Bate-Bate") #Adiciona o nome na janela
        self.clock = pygame.time.Clock() #Tempo de velocidade do nome na janela
        self.MovendoTexto = MovendoTexto("Amanda", 50, self.largura, self.altura) #Cria o atributo para criar retangulo respeitando as informações de fonte, largura e altura

    def run(self): #Método para rodar o jogo
        rodando = True 
        while rodando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False
            self.MovendoTexto.mover() #Atributo para mover o retangulo
            self.tela.fill((0, 0, 0)) #Cor de fundo
            self.tela.blit(self.MovendoTexto.texto_surf, self.MovendoTexto.texto_rect) #Cria o retangulo
            pygame.display.flip() #Atualiza a janela
            self.clock.tick(60) #Velocidade


        pygame.quit() #Fecha o jogo
        sys.exit() 