# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from collections import namedtuple
from itertools import product
import random
import time
import math
import copy

WIDTH = 640
HEIGHT = 480

pygame.init()

#carta de costas
C_costas = pygame.image.load('BARALHO/cardback.png')

#cartas de copas
D_C = pygame.image.load('pasta_de_cartas/2_de_copas.PNG')
T_C = pygame.image.load('pasta_de_cartas/3_de_copas.PNG')
Q_C = pygame.image.load('pasta_de_cartas/4_de_copas.PNG')
C_C = pygame.image.load('pasta_de_cartas/5_de_copas.PNG')
S_C = pygame.image.load('pasta_de_cartas/6_de_copas.PNG')
s_C = pygame.image.load('pasta_de_cartas/7_de_copas.PNG')
O_C = pygame.image.load('pasta_de_cartas/8_de_copas.PNG')
N_C = pygame.image.load('pasta_de_cartas/9_de_copas.PNG')
X_C = pygame.image.load('pasta_de_cartas/10_de_copas.PNG')
K_C = pygame.image.load('pasta_de_cartas/Rei_de_copas.PNG')
R_C = pygame.image.load('pasta_de_cartas/Rainha_de_copas.PNG')
V_C = pygame.image.load('pasta_de_cartas/Valete_de_copas.PNG')
A_C = pygame.image.load('pasta_de_cartas/As_de_copas.PNG')

#carta de ouro
D_O = pygame.image.load('pasta_de_cartas/2_de_ouro.PNG')
T_O = pygame.image.load('pasta_de_cartas/3_de_ouro.PNG')
Q_O = pygame.image.load('pasta_de_cartas/4_de_ouro.PNG')
C_O = pygame.image.load('pasta_de_cartas/5_de_ouro.PNG')
S_O = pygame.image.load('pasta_de_cartas/6_de_ouro.PNG')
s_O = pygame.image.load('pasta_de_cartas/7_de_ouro.PNG')
O_O = pygame.image.load('pasta_de_cartas/8_de_ouro.PNG')
N_O = pygame.image.load('pasta_de_cartas/9_de_ouro.PNG')
X_O = pygame.image.load('pasta_de_cartas/10_de_ouro.PNG')
K_O = pygame.image.load('pasta_de_cartas/Rei_de_ouro.PNG')
R_O = pygame.image.load('pasta_de_cartas/Rainha_de_ouro.PNG')
V_O = pygame.image.load('pasta_de_cartas/Valete_de_ouro.PNG')
A_O = pygame.image.load('pasta_de_cartas/As_de_ouro.PNG')

#carta de espadas
D_E = pygame.image.load('pasta_de_cartas/2_de_espadas.PNG')
T_E = pygame.image.load('pasta_de_cartas/3_de_espadas.PNG')
Q_E = pygame.image.load('pasta_de_cartas/4_de_espadas.PNG')
C_E = pygame.image.load('pasta_de_cartas/5_de_espadas.PNG')
S_E = pygame.image.load('pasta_de_cartas/6_de_espadas.PNG')
s_E = pygame.image.load('pasta_de_cartas/7_de_espadas.PNG')
O_E = pygame.image.load('pasta_de_cartas/8_de_espadas.PNG')
N_E = pygame.image.load('pasta_de_cartas/9_de_espadas.PNG')
X_E = pygame.image.load('pasta_de_cartas/10_de_espadas.PNG')
K_E = pygame.image.load('pasta_de_cartas/Rei_de_espadas.PNG')
R_E = pygame.image.load('pasta_de_cartas/Rainha_de_espadas.PNG')
V_E = pygame.image.load('pasta_de_cartas/Valete_de_espadas.PNG')
A_E = pygame.image.load('pasta_de_cartas/A_de_espadas.PNG')

#carta de paus
D_P = pygame.image.load('pasta_de_cartas/2_de_paus.PNG')
T_P = pygame.image.load('pasta_de_cartas/3_de_paus.PNG')
Q_P = pygame.image.load('pasta_de_cartas/4_de_paus.PNG')
C_P = pygame.image.load('pasta_de_cartas/5_de_paus.PNG')
S_P = pygame.image.load('pasta_de_cartas/6_de_paus.PNG')
s_P = pygame.image.load('pasta_de_cartas/7_de_paus.PNG')
O_P = pygame.image.load('pasta_de_cartas/8_de_paus.PNG')
N_P = pygame.image.load('pasta_de_cartas/9_de_paus.PNG')
X_P = pygame.image.load('pasta_de_cartas/10_de_paus.PNG')
K_P = pygame.image.load('pasta_de_cartas/Rei_de_paus.PNG')
R_P = pygame.image.load('pasta_de_cartas/Rainha_de_paus.PNG')
V_P = pygame.image.load('pasta_de_cartas/Valete_de_paus.PNG')
A_P = pygame.image.load('pasta_de_cartas/As_de_paus (2).PNG')

#Classe das cartas que vao chegar no jogador
class carta_pra_cima_posicao(pygame.sprite.Sprite):
    def __init__(self,img,x_final,y_final):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 0
        self.speedx = (x_final + 10)/70
        self.speedy = (y_final)/70
        self.x_final = x_final
        self.y_final = y_final
        self.som_embaralhar = som_shuffle 
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.som_embaralhar.play()
        if self.rect.y > self.y_final :
            self.rect.y = self.y_final
        if self.rect.x > self.x_final :
            self.rect.x = self.x_final
    
# classes de valores das cartas 
baralho = [ A_C, A_O, A_E, A_P, D_C, D_O, D_E, D_P, T_C, T_O, T_E, T_P, \
Q_C, Q_O, Q_E, Q_P ,C_C, C_O, C_E, C_P ,S_C, S_O, S_E, S_P, \
s_C, s_O, s_E, s_P ,O_C, O_O, O_E, O_P ,N_C, N_O, N_E, N_P, \
D_C, D_O, D_E, D_P, V_C, V_O, V_E, V_P, R_C, R_O, R_E, R_P, \
K_C, K_O, K_E, K_P ]
CartaA = [ A_C, A_O, A_E, A_P ]
Carta2 = [ D_C, D_O, D_E, D_P ]
Carta3 = [T_C, T_O, T_E, T_P ]
Carta4 = [ Q_C, Q_O, Q_E, Q_P ]
Carta5 = [ C_C, C_O, C_E, C_P ]
Carta6 = [ S_C, S_O, S_E, S_P ]
Carta7 = [ s_C, s_O, s_E, s_P ]
Carta8 = [ O_C, O_O, O_E, O_P ]
Carta9 = [ N_C, N_O, N_E, N_P ]
Carta10 = [ D_C, D_O, D_E, D_P, \
            V_C, V_O, V_E, V_P, \
            R_C, R_O, R_E, R_P, \
            K_C, K_O, K_E, K_P ]

def pontuacao(carta):
    if carta in CartaA:
        return 11
    elif carta in Carta2:
        return 2
    elif carta in Carta3:        
        return 3
    elif carta in Carta4:        
        return 4
    elif carta in Carta5:        
        return 5
    elif carta in Carta6:        
        return 6
    elif carta in Carta7:        
        return 7
    elif carta in Carta8:        
        return 8
    elif carta in Carta9:        
        return 9
    elif carta in Carta10:
        return 10

def embaralhar(baralho, mao):
    carta = random.choice(baralho)
    baralho.remove(carta)
    mao.append(carta)
    return carta

def inicio(cartas, mao_jogador, mao_banco):
    carta1 = embaralhar(cartas, mao_jogador)
    carta2 = embaralhar(cartas, mao_banco)
    carta3 = embaralhar(cartas, mao_jogador)
    carta4 = embaralhar(cartas, mao_banco)
    # retorna mao
    return pontuacao(carta1) + pontuacao(carta3), pontuacao(carta2) + pontuacao(carta4) 
# colors 
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
gray = (192,192,192)

# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100)


#definir variaveis
cartas = copy.copy(baralho)
mao_jogador = []
mao_banco = []
vitoria = 0
derrota = 0
continuar = False

# ----- Gera tela principal

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BlackJack')
font = pygame.font.SysFont('Corbel',15)
jogador, banco = inicio(cartas, mao_jogador, mao_banco)

#Arquivos de som
pygame.mixer.music.load('tetris_beatbox.wav.wav')
pygame.mixer.music.set_volume(0.03)
som_shuffle = pygame.mixer.Sound('card_shuffle.wav.wav')

# textos
Quit = font.render('quit' , True , white)
Blackjack = font.render('BlackJack!' , True , white)
Comprar = font.render('Comprar' , True , white)
Continuar = font.render('Continuar' , True , white)
Gameover = font.render('Gameover' , True , white)
Reiniciar = font.render('Reiniciar' , True , white)
Vitoria = font.render('Você ganhou!', True, white)
Derrota = font.render('Você perdeu!', True,white)

#montar tela
background = pygame.Surface(window.get_size())
background = background.convert()
background.fill((80, 150, 15))
comprarb = pygame.draw.rect(background, color_dark, (10, 445, 75, 25))
continuarb = pygame.draw.rect(background, color_dark, (95, 445, 75, 25))


#==TELA DE INICIO==
black=(0,0,0)
tela_inicio=False
instrucoes = True
while (tela_inicio==False):
    window.fill(black)
    titulo=pygame.font.SysFont("Black Jack", 40)
    titulo_na_tela=pygame.image.load('pasta_de_cartas/2_de_paus.PNG') #ainda eh necessario colocar imagem
    for event in pygame.event.get():
        if event.type== pygame.MOUSEBUTTONDOWN:
            tela_inicio=True
            instrucoes = False
    window.blit(titulo_na_tela,(0,0))
    pygame.display.flip()

#==TELA DAS INSTRUCOES==
while (instrucoes==False):
    window.fill(black)
    titulo=pygame.font.SysFont("Black Jack", 40)
    titulo_na_tela=pygame.image.load('instrucoes_black_jack.png')
    for event in pygame.event.get():
        if event.type== pygame.MOUSEBUTTONDOWN:
            instrucoes = True
    window.blit(titulo_na_tela,(0,0))
    pygame.display.flip()




# ===== Loop principal =====
game = True
pygame.mixer.music.play(loops =- 1)
while game:
    #se o jogo acabou
    gameover = True if jogador >= 21 else False
    if jogador == 21:
        gameover = True
    elif banco == 21:
        gameover = True

    #background needs to be redisplayed because it gets updated
    vitoria_txt = font.render('Wins: %i' % vitoria, 1, white)
    derrota_txt = font.render('Losses: %i' % derrota, 1, white)
    
    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or continuar) and comprarb.collidepoint(pygame.mouse.get_pos()):
            #da carta ao jogador se ele nao quebra as regras do blackjack
            carta = embaralhar(cartas, mao_jogador)
            jogador += pontuacao(carta)
            print('Jogador: %i' % jogador)
            while jogador > 21 and carta in CartaA:
                jogador -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and continuarb.collidepoint(pygame.mouse.get_pos()):
            continuar = True
            while banco <= jogador and banco < 17:
                carta = embaralhar(cartas, mao_banco)
                banco += pontuacao(carta)
                print('Banco: %i' % banco)
                while banco > 21 and carta in CartaA:
                    banco -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or continuar) and reiniciarb.collidepoint(pygame.mouse.get_pos()):
            if jogador == banco:
                pass
            elif jogador == 21 or banco < jogador or banco > 21:
                vitoria += 1
            else:
                derrota += 1
            gameover = False
            continuar = False
            mao_jogador = []
            mao_banco = []
            jogador, banco = inicio(cartas, mao_jogador, mao_banco)
            reiniciarb = pygame.draw.rect(background, (80, 150, 15), (270, 225, 75, 25))

    window.blit(background, (0, 0))
    window.blit(Comprar, (25, 448))
    window.blit(Continuar, (105, 448))
    window.blit(vitoria_txt, (565, 423))
    window.blit(derrota_txt, (565, 448))

    # mostrar carta do banco
    for card in mao_banco:
        x = 10 + mao_banco.index(card) * 110
        window.blit(card, (x, 10))
    window.blit(C_costas, (120, 10))

    # mostrar carta do jogador
    for card in mao_jogador:
        x = 10 + mao_jogador.index(card) * 110
        window.blit(card, (x, 295))

    # Mostrar segunda carta do banco e perguntar do reinicio
    if gameover or continuar:
        window.blit(Gameover, (270, 200))
        reiniciarb = pygame.draw.rect(background, gray, (270, 225, 75, 25))
        window.blit(Reiniciar, (287, 228))
        window.blit(mao_banco[1], (120, 10))
            
    pygame.display.update()

#         print(event) # ----- Verifica consequência    
#         if event.type == pygame.MOUSEBUTTONDOWN:  #if the mouse is clicked on the               
#             # COMECA JOGO
#             if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40: 
#                 gameDisplay.fill(white)
#                 pygame.display.update()
#             #PARA JOGO
#             elif WIDTH/4-40 <= mouse[0] <= WIDTH/4-40+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:               
#                 pygame.quit()

#     # ----- Gera saídas  
#     gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
#     gameDisplay.fill(green) 

#     # Cria posição do mouse
#     mouse = pygame.mouse.get_pos() 

#     #DESENHA BOTAO DE INICIAR
#     WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40
#     pygame.draw.rect(window,color_light,[WIDTH/2,HEIGHT/2,140,40]) 
#     pygame.draw.rect(window,color_dark,[WIDTH/2,HEIGHT/2,140,40]) 
#     window.blit(Quit , (WIDTH/2+50,HEIGHT/2))

#     #DESENHA BOTAO DE QUIT
#     WIDTH/4-40 <= mouse[0] <= WIDTH/4-40+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40
#     pygame.draw.rect(window,color_light,[WIDTH/4-40,HEIGHT/2,140,40])         
#     pygame.draw.rect(window,color_dark,[WIDTH/4-40,HEIGHT/2,140,40]) 
#     window.blit(Iniciar , (WIDTH/4-10,HEIGHT/2)) 

#     # ----- Atualiza estado do jogo
#     pygame.display.update()  # Mostra o novo frame para o jogador
#     clock.tick(1000)
# # ===== Finalização =====
