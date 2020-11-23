# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from collections import namedtuple
from itertools import product
import random
import time
import math

pygame.init()
WIDTH = 600
HEIGHT = 600
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Black Jack')

# ----- Inicia estruturas de dados
game = True

#Arquivos de som
pygame.mixer.music.load('tetris_beatbox.wav.wav')
pygame.mixer.music.set_volume(0.2)
som_shuffle = pygame.mixer.Sound('card_shuffle.wav.wav')

#carta de costas
C_costas = pygame.image.load('BARALHO/carta_de_costas.PNG').convert()

baralho = []

#cartas de copas
D_C = pygame.image.load('pasta_de_cartas/2_de_copas.PNG').convert()
baralho.append(D_C)
T_C = pygame.image.load('pasta_de_cartas/3_de_copas.PNG').convert()
baralho.append(T_C)
Q_C = pygame.image.load('pasta_de_cartas/4_de_copas.PNG').convert()
baralho.append(Q_C)
C_C = pygame.image.load('pasta_de_cartas/5_de_copas.PNG').convert()
baralho.append(C_C)
S_C = pygame.image.load('pasta_de_cartas/6_de_copas.PNG').convert()
baralho.append(S_C)
s_C = pygame.image.load('pasta_de_cartas/7_de_copas.PNG').convert()
baralho.append(s_C)
O_C = pygame.image.load('pasta_de_cartas/8_de_copas.PNG').convert()
baralho.append(O_C)
N_C = pygame.image.load('pasta_de_cartas/9_de_copas.PNG').convert()
baralho.append(N_C)
X_C = pygame.image.load('pasta_de_cartas/10_de_copas.PNG').convert()
baralho.append(X_C)
K_C = pygame.image.load('pasta_de_cartas/Rei_de_copas.PNG').convert()
baralho.append(K_C)
R_C = pygame.image.load('pasta_de_cartas/Rainha_de_copas.PNG').convert()
baralho.append(R_C)
V_C = pygame.image.load('pasta_de_cartas/Valete_de_copas.PNG').convert()
baralho.append(V_C)
A_C = pygame.image.load('pasta_de_cartas/As_de_copas.PNG').convert()
baralho.append(A_C)

#carta de ouro
D_O = pygame.image.load('pasta_de_cartas/2_de_ouro.PNG').convert()
baralho.append(D_O)
T_O = pygame.image.load('pasta_de_cartas/3_de_ouro.PNG').convert()
baralho.append(T_O)
Q_O = pygame.image.load('pasta_de_cartas/4_de_ouro.PNG').convert()
baralho.append(Q_O)
C_O = pygame.image.load('pasta_de_cartas/5_de_ouro.PNG').convert()
baralho.append(C_O)
S_O = pygame.image.load('pasta_de_cartas/6_de_ouro.PNG').convert()
baralho.append(S_O)
s_O = pygame.image.load('pasta_de_cartas/7_de_ouro.PNG').convert()
baralho.append(s_O)
O_O = pygame.image.load('pasta_de_cartas/8_de_ouro.PNG').convert()
baralho.append(O_O)
N_O = pygame.image.load('pasta_de_cartas/9_de_ouro.PNG').convert()
baralho.append(N_O)
X_O = pygame.image.load('pasta_de_cartas/10_de_ouro.PNG').convert()
baralho.append(X_O)
K_O = pygame.image.load('pasta_de_cartas/Rei_de_ouro.PNG').convert()
baralho.append(K_O)
R_O = pygame.image.load('pasta_de_cartas/Rainha_de_ouro.PNG').convert()
baralho.append(R_O)
V_O = pygame.image.load('pasta_de_cartas/Valete_de_ouro.PNG').convert()
baralho.append(V_O)
A_O = pygame.image.load('pasta_de_cartas/As_de_ouro.PNG').convert()
baralho.append(A_O)

#carta de espadas
D_E = pygame.image.load('pasta_de_cartas/2_de_espadas.PNG').convert()
baralho.append(D_E)
T_E = pygame.image.load('pasta_de_cartas/3_de_espadas.PNG').convert()
baralho.append(T_E)
Q_E = pygame.image.load('pasta_de_cartas/4_de_espadas.PNG').convert()
baralho.append(Q_E)
C_E = pygame.image.load('pasta_de_cartas/5_de_espadas.PNG').convert()
baralho.append(C_E)
S_E = pygame.image.load('pasta_de_cartas/6_de_espadas.PNG').convert()
baralho.append(S_E)
s_E = pygame.image.load('pasta_de_cartas/7_de_espadas.PNG').convert()
baralho.append(s_E)
O_E = pygame.image.load('pasta_de_cartas/8_de_espadas.PNG').convert()
baralho.append(O_E)
N_E = pygame.image.load('pasta_de_cartas/9_de_espadas.PNG').convert()
baralho.append(N_E)
X_E = pygame.image.load('pasta_de_cartas/10_de_espadas.PNG').convert()
baralho.append(X_E)
K_E = pygame.image.load('pasta_de_cartas/Rei_de_espadas.PNG').convert()
baralho.append(K_E)
R_E = pygame.image.load('pasta_de_cartas/Rainha_de_espadas.PNG').convert()
baralho.append(R_E)
V_E = pygame.image.load('pasta_de_cartas/Valete_de_espadas.PNG').convert()
baralho.append(V_E)
A_E = pygame.image.load('pasta_de_cartas/A_de_espadas.PNG').convert()
baralho.append(A_E)

#carta de paus
D_P = pygame.image.load('pasta_de_cartas/2_de_paus.PNG').convert()
baralho.append(D_P)
T_P = pygame.image.load('pasta_de_cartas/3_de_paus.PNG').convert()
baralho.append(T_P)
Q_P = pygame.image.load('pasta_de_cartas/4_de_paus.PNG').convert()
baralho.append(Q_P)
C_P = pygame.image.load('pasta_de_cartas/5_de_paus.PNG').convert()
baralho.append(C_P)
S_P = pygame.image.load('pasta_de_cartas/6_de_paus.PNG').convert()
baralho.append(S_P)
s_P = pygame.image.load('pasta_de_cartas/7_de_paus.PNG').convert()
baralho.append(s_P)
O_P = pygame.image.load('pasta_de_cartas/8_de_paus.PNG').convert()
baralho.append(O_P)
N_P = pygame.image.load('pasta_de_cartas/9_de_paus.PNG').convert()
baralho.append(N_P)
X_P = pygame.image.load('pasta_de_cartas/10_de_paus.PNG').convert()
baralho.append(X_P)
K_P = pygame.image.load('pasta_de_cartas/Rei_de_paus.PNG').convert()
baralho.append(K_P)
R_P = pygame.image.load('pasta_de_cartas/Rainha_de_paus.PNG').convert()
baralho.append(R_P)
V_P = pygame.image.load('pasta_de_cartas/Valete_de_paus.PNG').convert()
baralho.append(V_P)
A_P = pygame.image.load('pasta_de_cartas/As_de_paus (2).PNG').convert()
baralho.append(A_P)

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
def pontuacao(carta, pontu):
    if carta in CartaA:
        pontu += 11
    elif carta in Carta2:
        pontu += 2
    elif carta in Carta3:
        pontu += 3
    elif carta in Carta4:
        pontu += 4
    elif carta in Carta5:
        pontu += 5
    elif carta in Carta6:
        pontu += 6
    elif carta in Carta7:
        pontu += 7
    elif carta in Carta8:
        pontu += 8
    elif carta in Carta9:
        pontu += 9
    elif carta in Carta10:
        pontu += 10
    return pontu

def embaralhar(baralho, mao):
    carta = random.choice(baralho)
    baralho.remove(carta)
    mao.append(carta)
    return carta

def inicio(baralho, mao):
    # adiciona carta 1
    carta1 = random.choice(baralho)
    baralho.remove(carta1)
    mao.append(carta1)
    # adiciona carta 2
    carta2 = random.choice(baralho)
    baralho.remove(carta2)
    mao.append(carta2)
    # retorna mao
    return mao
# colors 
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
gray = (192,192,192)


display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35)

# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100)

#montar tela
background = pygame.Surface(window.get_size())
background = background.convert()
background.fill((80, 150, 15))
comprar = pygame.draw.rect(background, gray, (10, 445, 75, 25))
continuar = pygame.draw.rect(background, gray, (95, 445, 75, 25))

# textos
Quit = smallfont.render('quit' , True , white)
Hit = smallfont.render('Hit' , True , white)
Blackjack = smallfont.render('BlackJack' , True , white)
Comprar = smallfont.render('Comprar' , True , white)
Continuar = smallfont.render('Continuar' , True , white)
Gameover = smallfont.render('Gameover' , True , white)
Reiniciar = smallfont.render('Reiniciar' , True , white)


# text surface object 
textRect = Blackjack.get_rect()  
  
# set the center of the rectangular object. 
textRect.center = (WIDTH // 2, HEIGHT // 4)

#definir variaveis
mao_jogador = []
mao_banco = []
jogador = 0
banco = 0

# ===== Loop principal =====
pygame.mixer.music.play(loops =- 1)
while game:
    inicio(baralho, mao_jogador)
    inicio(baralho, mao_banco)
    pontuacao(mao_jogador[0], jogador)
    pontuacao(mao_jogador[1], jogador)
    pontuacao(mao_banco[0], banco)
    pontuacao(mao_banco[1], banco)
    #se o jogo acabou
    gameover = True if jogador >= 21 else False
    if jogador == 21:
        gameover = True
    elif banco == 21:
        gameover = True
    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not (Gameover or Continuar) and comprar.collidepoint(pygame.mouse.get_pos()):
            #gives player a card if they don't break blackjack rules
            carta = embaralhar(baralho, mao_jogador)
            jogador += pontuacao(carta, jogador)
            print('User: %i' % jogador)
            while jogador > 21 and carta.first == 'A':
                jogador -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN and not Gameover and continuar.collidepoint(pygame.mouse.get_pos()):
            Continuar = True
            while banco <= jogador and banco < 17:
                carta = embaralhar(baralho, mao_banco)
                banco += pontuacao(carta, jogador)
                print('Dealer: %i' % banco)
                while banco > 21 and carta.first == 'A':
                    banco -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN and (Gameover or Continuar) and reiniciar.collidepoint(pygame.mouse.get_pos()):
            if jogador == banco:
                pass
            elif jogador <= 21 and banco < jogador or banco > 21:
                vitoria += 1
            else:
                derrota += 1
            Gameover = False
            Continuar = False
            mao_jogador = []
            mao_banco = []
            mao_jogador = inicio(baralho, mao_jogador)
            mao_banco = inicio(baralho, mao_banco)
            jogador += pontuacao(mao_jogador[0], jogador)
            jogador += pontuacao(mao_jogador[1], jogador)
            banco += pontuacao(mao_banco[0], banco)
            banco += pontuacao(mao_banco[1], banco)
            reiniciar = pygame.draw.rect(background, (80, 150, 15), (270, 225, 75, 25))

    window.blit(background, (0, 0))
    window.blit(Comprar, (39, 448))
    window.blit(Continuar, (116, 448))

    for card in mao_banco:
        x = 10 + mao_banco.index(card) * 110
        window.blit(card, (x, 10))
    window.blit(C_costas, (120, 10))

    #displays player's cards
    for card in mao_jogador:
        x = 10 + mao_jogador.index(card) * 110
        window.blit(card, (x, 295))

    #when game is over, draws restart button and text, and shows the dealer's second card
    if Gameover or Continuar:
        window.blit(Gameover, (270, 200))
        Reiniciar = pygame.draw.rect(background, gray, (270, 225, 75, 25))
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
