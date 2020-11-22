# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()
WIDTH = 500
HEIGHT = 500
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Black Jack')

# ----- Inicia estruturas de dados
game = True
posicao_1_carta_jogador = [300,300]
posicao_2_carta_jogador = [300,300]
posicao_3_carta_jogador = [300,300]

#cartas de copas
dois_de_copas = pygame.image.load('pasta_de_cartas/2_de_copas.PNG').convert()
tres_de_copas = pygame.image.load('pasta_de_cartas/3_de_copas.PNG').convert()
quatro_de_copas = pygame.image.load('pasta_de_cartas/4_de_copas.PNG').convert()
cinco_de_copas = pygame.image.load('pasta_de_cartas/5_de_copas.PNG').convert()
seis_de_copas = pygame.image.load('pasta_de_cartas/6_de_copas.PNG').convert()
sete_de_copas = pygame.image.load('pasta_de_cartas/7_de_copas.PNG').convert()
oito_de_copas = pygame.image.load('pasta_de_cartas/8_de_copas.PNG').convert()
nove_de_copas = pygame.image.load('pasta_de_cartas/9_de_copas.PNG').convert()
dez_de_copas = pygame.image.load('pasta_de_cartas/10_de_copas.PNG').convert()
rei_de_copas = pygame.image.load('pasta_de_cartas/Rei_de_copas.PNG').convert()
rainha_de_copas = pygame.image.load('pasta_de_cartas/Rainha_de_copas.PNG').convert()
valete_de_copas = pygame.image.load('pasta_de_cartas/Valete_de_copas.PNG').convert()
as_de_copas = pygame.image.load('pasta_de_cartas/As_de_copas.PNG').convert()

#carta de ouro
dois_de_ouro = pygame.image.load('pasta_de_cartas/2_de_ouro.PNG').convert()
tres_de_ouro = pygame.image.load('pasta_de_cartas/3_de_ouro.PNG').convert()
quatro_de_ouro = pygame.image.load('pasta_de_cartas/4_de_ouro.PNG').convert()
cinco_de_ouro = pygame.image.load('pasta_de_cartas/5_de_ouro.PNG').convert()
seis_de_ouro = pygame.image.load('pasta_de_cartas/6_de_ouro.PNG').convert()
sete_de_ouro = pygame.image.load('pasta_de_cartas/7_de_ouro.PNG').convert()
oito_de_ouro = pygame.image.load('pasta_de_cartas/8_de_ouro.PNG').convert()
nove_de_ouro = pygame.image.load('pasta_de_cartas/9_de_ouro.PNG').convert()
dez_de_ouro = pygame.image.load('pasta_de_cartas/10_de_ouro.PNG').convert()
rei_de_ouro = pygame.image.load('pasta_de_cartas/Rei_de_ouro.PNG').convert()
rainha_de_ouro = pygame.image.load('pasta_de_cartas/Rainha_de_ouro.PNG').convert()
valete_de_ouro = pygame.image.load('pasta_de_cartas/Valete_de_ouro.PNG').convert()
as_de_ouro = pygame.image.load('pasta_de_cartas/As_de_ouro.PNG').convert()

#carta de espadas
dois_de_espadas = pygame.image.load('pasta_de_cartas/2_de_espadas.PNG').convert()
tres_de_espadas = pygame.image.load('pasta_de_cartas/3_de_espadas.PNG').convert()
quatro_de_espadas = pygame.image.load('pasta_de_cartas/4_de_espadas.PNG').convert()
cinco_de_espadas = pygame.image.load('pasta_de_cartas/5_de_espadas.PNG').convert()
seis_de_espadas = pygame.image.load('pasta_de_cartas/6_de_espadas.PNG').convert()
sete_de_espadas = pygame.image.load('pasta_de_cartas/7_de_espadas.PNG').convert()
oito_de_espadas = pygame.image.load('pasta_de_cartas/8_de_espadas.PNG').convert()
nove_de_espadas = pygame.image.load('pasta_de_cartas/9_de_espadas.PNG').convert()
dez_de_espadas = pygame.image.load('pasta_de_cartas/10_de_espadas.PNG').convert()
rei_de_espadas = pygame.image.load('pasta_de_cartas/Rei_de_espadas.PNG').convert()
rainha_de_espadas = pygame.image.load('pasta_de_cartas/Rainha_de_espadas.PNG').convert()
valete_de_espadas = pygame.image.load('pasta_de_cartas/Valete_de_espadas.PNG').convert()
as_de_espadas = pygame.image.load('pasta_de_cartas/A_de_espadas.PNG').convert()

#carta de paus
dois_de_paus = pygame.image.load('pasta_de_cartas/2_de_paus.PNG').convert()
tres_de_paus = pygame.image.load('pasta_de_cartas/3_de_paus.PNG').convert()
quatro_de_paus = pygame.image.load('pasta_de_cartas/4_de_paus.PNG').convert()
cinco_de_paus = pygame.image.load('pasta_de_cartas/5_de_paus.PNG').convert()
seis_de_paus = pygame.image.load('pasta_de_cartas/6_de_paus.PNG').convert()
sete_de_paus = pygame.image.load('pasta_de_cartas/7_de_paus.PNG').convert()
oito_de_paus = pygame.image.load('pasta_de_cartas/8_de_paus.PNG').convert()
nove_de_paus = pygame.image.load('pasta_de_cartas/9_de_paus.PNG').convert()
dez_de_paus = pygame.image.load('pasta_de_cartas/10_de_paus.PNG').convert()
rei_de_paus = pygame.image.load('pasta_de_cartas/Rei_de_paus.PNG').convert()
rainha_de_paus = pygame.image.load('pasta_de_cartas/Rainha_de_paus.PNG').convert()
valete_de_paus = pygame.image.load('pasta_de_cartas/Valete_de_paus.PNG').convert()
as_de_paus = pygame.image.load('pasta_de_cartas/As_de_paus (2).PNG').convert()

class carta_pra_cima_posicao1(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.speedx = 0
        self.speedy = 10
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y > posicao_1_carta_jogador[1] :
            self.rect.x = 10
            self.rect.y = 300
        

class carta_pra_cima_posicao2(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedx = 5
        self.speedy = 10
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y > posicao_2_carta_jogador[1] :
            self.rect.x = 150
            self.rect.y = 300
        
       


class carta_pra_cima_posicao3(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedx = 10
        self.speedy = 10
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y > posicao_3_carta_jogador[1]:
            self.rect.x = 300
            self.rect.y = 300
        
        



FPS = 30
clock = pygame.time.Clock()

#criando val de copas
all_sprites = pygame.sprite.Group()
valcopas = carta_pra_cima_posicao1(valete_de_copas)
rainhacopas = carta_pra_cima_posicao2(rainha_de_copas)
reicopas = carta_pra_cima_posicao3(rei_de_copas)
all_sprites.add(valcopas)
all_sprites.add(rainhacopas)
all_sprites.add(reicopas)

# colors 
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35)

# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100)

# rendering a text written in 
# this font 
Quit = smallfont.render('quit' , True , white)
Iniciar = smallfont.render('Iniciar' , True , white)
Blackjack = smallfont.render('BlackJack' , True , white)


# text surface object 
textRect = Blackjack.get_rect()  
  
# set the center of the rectangular object. 
textRect.center = (WIDTH // 2, HEIGHT // 4) 

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # botão fechar o jogo
            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40: 
                window.fill(white)
            if WIDTH/4-40 <= mouse[0] <= WIDTH/4-40+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                pygame.quit()
            # botão de começar o jogo
    # ----- Gera saídas
    window.fill(green)
    
    display_surface.blit(Blackjack, textRect) 

    
    # Cria posição do mouse
    mouse = pygame.mouse.get_pos() 

    if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40: 
        pygame.draw.rect(window,color_light,[WIDTH/2,HEIGHT/2,140,40]) 
          
    else: 
        pygame.draw.rect(window,color_dark,[WIDTH/2,HEIGHT/2,140,40]) 
    window.blit(Quit , (WIDTH/2+50,HEIGHT/2))

    if WIDTH/4-40 <= mouse[0] <= WIDTH/4-40+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40: 
        pygame.draw.rect(window,color_light,[WIDTH/4-40,HEIGHT/2,140,40]) 
          
    else: 
        pygame.draw.rect(window,color_dark,[WIDTH/4-40,HEIGHT/2,140,40]) 
    window.blit(Iniciar , (WIDTH/4-10,HEIGHT/2)) 

    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====