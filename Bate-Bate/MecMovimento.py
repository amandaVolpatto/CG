import pygame
import random

#Animais - classe
#Cachorro, Gato - atributos
#Cachorro: late, Gato: Miau - metodos

class MovendoTexto:
    def __init__(self, texto, fonte_tamanho, largura, altura):
        self.fonte = pygame.font.SysFont(None, fonte_tamanho) #self = Falando dele mesmo
        self.texto = texto 
        self.largura = largura #parametro (atributo)
        self.altura = altura
        self.texto_surf = self.fonte.render(texto, True, (255, 255, 255))
        self.texto_rect = self.texto_surf.get_rect(center=(largura/2, altura/2)) #encadeamento do codigo

        self.velocidade_x = self.gerar_numero_nao_zero() 
        self.velocidade_y = self.gerar_numero_nao_zero()

    def gerar_numero_nao_zero(selt): #criei a função dentro do atributo (metodos)
        numero = 0 
        while numero == 0:
            numero = random.randint(-1, 1)
        return numero        
    
    def mover(self):
        self.texto_rect.x += self.velocidade_x
        self.texto_rect.y += self.velocidade_y

        if self.texto_rect.left <= 0: #Condicional que texto vai para esquerda.
            self.velocidade_x = random.randint(0, 1) #sorteia denovo mais não pode ser x
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()

        if self.texto_rect.right >= self.largura:
            self.velocidade_x = random.randint(-1, 0) 
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()

        if self.texto_rect.top <= 0:
            self.velocidade_x = random.randint(-1,1) 
            self.velocidade_y = random.randint(0,1)
            self.change_color()

        if self.texto_rect.bottom  >= self.altura:
            self.velocidade_x = random.randint(-1, 1) 
            self.velocidade_y = random.randint(-1, 0)
            self.change_color()

    def change_color(self):
        cor_texto = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
        self.texto_surf = self.fonte.render(self.texto, True, cor_texto)

        
        
        