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
    
    def mover(self): #abaixo, soma +1 aos valores do eixo x e y
        self.texto_rect.x += self.velocidade_x
        self.texto_rect.y += self.velocidade_y

        if self.texto_rect.left <= 0: #Ladoesquerda.
            self.velocidade_x = random.randint(0, 1) #Caso o valor do lado esquerdo seja menor ou igual a 0, ele sorteia velocidade para velo x e y
            self.velocidade_y = random.randint(-1, 1) #O valor de x, nesse caso, não pode ser -1. Se for -1, o texto saira da tela
            self.change_color()

        if self.texto_rect.right >= self.largura: #Lado Direito
            self.velocidade_x = random.randint(-1, 0) #Caso o valor do lado esquerdo seja maior ou igual a largura da tela, ele sorteia um valor a velocidade em x e y
            self.velocidade_y = random.randint(-1, 1) #O valor de x, nesse caso, não pode ser 1. Se for 1, o texto saira da tela
            self.change_color()

        if self.texto_rect.top <= 0:#Lado Superior
            self.velocidade_x = random.randint(-1,1) #Caso o valor do lado superior seja menor ou igual a 0, ele sorteia um valor a velocidade em x e y
            self.velocidade_y = random.randint(0,1) #O valor de y, nesse caso, não pode ser 1. Se for 1, o texto saira da tela
            self.change_color()

        if self.texto_rect.bottom  >= self.altura: #Lado inferior
            self.velocidade_x = random.randint(-1, 1) #Caso o valor do lado inferior seja maior ou igual a altura da tela, ele sorteia um valor a velocidade em x e y
            self.velocidade_y = random.randint(-1, 0) #O valor de y, nesse caso, não pode ser 1. Se for 1, o texto saira da tela
            self.change_color()

#A função sorteia uma nova cor do objeto toda vez que bate na parede.
    def change_color(self):
        cor_texto = (
        random.randint(0, 255), #sorteado no intervalo de 0 a 255
        random.randint(0, 255),
        random.randint(0, 255),
    )
        self.texto_surf = self.fonte.render(self.texto, True, cor_texto)

        
        
        