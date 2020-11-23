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

# # Perguntar quantas fichas o jogador quer comprar
# Fichas = int(input("Quantas fichas gostaria de adquirir? "))
# Preco = 10 * Fichas
# print("Seu total é de R${0}!" .format(Preco))

# while True:
#     # Perguntar quantas fichas deseja apostar

#     Aposta = int(input("Qual será sua aposta?"))
#     if Aposta < 1:
#         print("Não tenha medo! Hoje senti que a sorte está do seu lado.")
#     elif Aposta > Fichas:
#         Falta = Aposta - Fichas
#         r = input("Você não tem todas essas fichas, gostaria de comprar mais {0} fichas?(s ou n) " .format(Falta))
#         if r == 's':
#             print('Você comprou {0} fichas! Vamos jogar!' .format(Falta))
#             Fichas += Falta
#             Fichas -= Aposta
#         else:
#             Aposta = int(input("Qual será sua aposta? "))
#     else:
#         print('Vamos jogar!')
#         Fichas -= Aposta

#     time.sleep(2)

#     # embaralhando e selecionando as cartas dos jogadores
#     random.shuffle(baralho)

#     mao_jogador = baralho[0:2]
#     mao_banco = baralho[2:4]
#     print("Suas cartas são {0}" .format(mao_jogador))
#     time.sleep(2)
#     print("As cartas do banco são {0}" .format(mao_banco))

#     # colocando os valores nas do jogador:
#     if mao_jogador[0][0] == 'A':
#         pont1 = 11
#     elif mao_jogador[0][0] == '10' or mao_jogador[0][0] == 'J' or mao_jogador[0][0] == 'Q' or mao_jogador[0][0] == 'K':
#         pont1 = 10
#     elif int(mao_jogador[0][0]) < 10:
#         pont1 = int(mao_jogador[0][0])

#     if mao_jogador[1][0] == 'A':
#         pont2 = 11
#     elif mao_jogador[1][0] == '10' or mao_jogador[1][0] == 'J' or mao_jogador[1][0] == 'Q' or mao_jogador[1][0] == 'K':
#         pont2 = 10
#     elif int(mao_jogador[1][0]) < 10:
#         pont2 = int(mao_jogador[1][0])
#     jogador = pont1 + pont2
#     if jogador > 21 and (mao_jogador[0][0] == 'A' or mao_jogador[1][0] == 'A'):
#         jogador -= 10

#     # colocando valores nas cartas do banco:
#     if mao_banco[0][0] == 'A':
#         pontu1 = 11
#     elif mao_banco[0][0] == '10' or mao_banco[0][0] == 'J' or mao_banco[0][0] == 'Q' or mao_banco[0][0] == 'K':
#         pontu1 = 10
#     elif int(mao_banco[0][0]) < 10:
#         pontu1 = int(mao_banco[0][0])

#     if mao_banco[1][0] == 'A':
#         pontu2 = 11
#     elif mao_banco[1][0] == '10' or mao_banco[1][0] == 'J' or mao_banco[1][0] == 'Q' or mao_banco[1][0] == 'K':
#         pontu2 = 10
#     elif int(mao_banco[1][0]) < 10:
#         pontu2 = int(mao_banco[1][0])
#     banco = pontu1 + pontu2
#     if banco > 21 and (mao_banco[0][0] == 'A' or mao_banco[1][0] == 'A'):
#         banco -= 10

#     # Definindo a pontuação

#     # Checando o vencedor
    
#     j_venceu = False
#     b_venceu = False
#     if jogador == 21:
#         print('O jogador alcançou a pontuação desejada')
#         j_venceu = True
#     if jogador > 21:
#         print('O jogador ultrapassou a pontuação desejada')
#     if banco == 21:
#         print('O banco alcançou a pontuação desejada')
#         b_venceu = True
#     if banco > 21:
#         print('O banco ultrapassou a pontuação desejada')

#     # O jogador vai comprar cartas?

#     i = 0
#     nao = False
#     while jogador < 21 and b_venceu == False and nao == False:
#         resp = input('Você tem {0} pontos. Deseja mais uma carta?' .format(jogador))
#         if resp == 'sim':
#             mao_jogador += baralho[i + 4]
#             time.sleep(2)
#             print("Sua carta é {0}" .format(mao_jogador[(i + 2)]))
#             if mao_jogador[(i + 2)] == 'A' and jogador > 10:
#                 pont = 1
#             if mao_jogador[(i + 2)] == 'A' and jogador <= 10:
#                 pont = 11
#             elif mao_jogador[(i + 2)] == '10' or mao_jogador[(i + 2)] == 'J' or mao_jogador[(i + 2)] == 'Q' or mao_jogador[(i + 2)] == 'K':
#                 pont = 10
#             elif int(mao_jogador[(i + 2)]) < 10:
#                 pont = int(mao_jogador[(i + 2)])
#             jogador += pont
#             i += 2
#         else:
#             nao = True
#     if jogador == 21 and b_venceu == False:
#         print('BlackJack!')
#         j_venceu = True
#     elif jogador > 21 and (mao_jogador[0][0] == 'A' or mao_jogador[1][0] == 'A'):
#         jogador -= 10
#     if jogador > 21:
#         print('O jogador ultrapassou a pontuação desejada')
#     time.sleep(1)

#     f = 0
#     while banco < 16 or banco < jogador and jogador < 21 and j_venceu == False:
#         mao_banco += baralho[f + i + 4]
#         time.sleep(2)
#         print("O banco tem {0} pontos. A carta do banco é {1}" .format(banco, mao_banco[(f + 2)]))
#         if mao_banco[(f + 2)] == 'A' and banco > 10:
#             pont = 1
#         elif mao_banco[(f + 2)] == 'A' and banco <= 10:
#             pont = 11
#         elif mao_banco[(f + 2)] == '10' or mao_banco[(f + 2)] == 'J' or mao_banco[(f + 2)] == 'Q' or mao_banco[(f + 2)] == 'K':
#             pont = 10
#         elif int(mao_banco[(f + 2)]) < 10:
#             pont = int(mao_banco[(f + 2)])
#         banco += pont
#         f += 2
#     if banco == 21 and b_venceu == False:
#         print('O banco ganhou!')
#         b_venceu = True
#     elif banco > 21 and (mao_banco[0][0] == 'A' or mao_banco[1][0] == 'A'):
#         banco -= 10
#     if banco > 21:
#         print('O banco ultrapassou a pontuação desejada')
#     time.sleep(1)

#     # Definindo o vencedor

#     time.sleep(2)
#     if j_venceu == True or (jogador > banco and jogador < 21) or banco > 21:
#         print('Você ganhou!!! Aqui está suas {0} fichas' .format(2 * Aposta))
#         Fichas += Aposta * 2
#     elif b_venceu == True or (banco >= jogador and banco < 21) or jogador > 21:
#         print('Você perdeu!')
            
#     #Checando se o jogador quer continuar jogando

#     jogar_mais = input("Vamos mais uma?(S ou N)")
#     if jogar_mais == 'N':
#         print('Ok, aqui estão suas {0} fichas, obrigado por jogar!' .format(Fichas))
#         break