#IMPORTA E INICIA BIBLIOTECA E PACOTES
import pygame
from collections import namedtuple
from itertools import product
import random
import time
import math
import copy

#INIDIALIZA PYGAME
pygame.init()

#DEFINE IS AS DIMENSOES DA JANELA DO JOGO 
WIDTH = 1400
HEIGHT = 800

#DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE
#DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE 
#DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE CARTAS##DEFINE

#C_COSTAS = CARREGAR COSTAS UNIVERSAL DE TODOS AS CARTAS
#TODAS AS CARTAS QUANDO NÃO ESTÃO SENDO MOSTRADAS CARREGAM O CARDBACK
C_costas = pygame.image.load('BARALHO/cardback.png')

#TODAS AS CARTAS DO NAIPE DE COPAS
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
#==================================================

#TODAS AS CARTAS DO NAIPE DE OURO 
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
#==================================================

#TODAS AS CARTAS DO NAIPE DE ESPADAS 
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
#==================================================

#TODAS AS CARTAS DO NAIPE DE PAUS
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
#==================================================

#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS
#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS
#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS#ACABA DE DEFNINIR AS CARTAS E IMAGEMS


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
        pontu = 11
    elif carta in Carta2:
        pontu = 2
    elif carta in Carta3:        
        pontu = 3
    elif carta in Carta4:        
        pontu = 4
    elif carta in Carta5:        
        pontu = 5
    elif carta in Carta6:        
        pontu = 6
    elif carta in Carta7:        
        pontu = 7
    elif carta in Carta8:        
        pontu = 8
    elif carta in Carta9:        
        pontu = 9
    elif carta in Carta10:
        pontu = 10
    return pontu

def embaralhar(baralho, mao):
    carta = random.choice(baralho)
    baralho.remove(carta)
    mao.append(carta)
    return carta

def inicio(baralho, mao_jogador, mao_banco):
    carta1 = embaralhar(baralho, mao_jogador)
    carta2 = embaralhar(baralho, mao_banco)
    carta3 = embaralhar(baralho, mao_jogador)
    carta4 = embaralhar(baralho, mao_banco)
    # retorna mao
    return pontuacao(carta1) + pontuacao(carta3), pontuacao(carta2) + pontuacao(carta4), carta1, carta3, carta2, carta4 
# cores
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
gray = (192,192,192)
black = (0,0,0)

# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100)


#definir variaveis
cartas = copy.copy(baralho)
mao_jogador = []
mao_banco = []
vitoria = 0
empate = 0
derrota = 0
continuar = False
Subtraiu = False
Subtraiu2 = False

########################################################################################### TELA PRINCIPAL ###########################################################################################
# TELA PRINCIPAL # # TELA PRINCIPAL # # TELA PRINCIPAL # # TELA PRINCIPAL # # TELA PRINCIPAL # # TELA PRINCIPAL # # TELA PRINCIPAL # # TELA PRINCIPAL # # TELA PRINCIPAL # # TELA PRINCIPAL # # TELA PRINCIPAL # 
########################################################################################### TELA PRINCIPAL ###########################################################################################


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BlackJack')
font = pygame.font.SysFont('Corbel',30)
jogador, banco, carta_jogador1, carta_jogador2, carta_banco1, carta_banco2 = inicio(cartas, mao_jogador, mao_banco)

#CARREGA ARQUIVO.WAV
#COLOCA O VOLUME DA MUSICO EM UM PARÂMETRO DE 0.12.
pygame.mixer.music.load('tetris_beatbox.wav.wav')
pygame.mixer.music.set_volume(0.03)
som_shuffle = pygame.mixer.Sound('card_shuffle.wav.wav')


class Tela():
    def __init__(self,cor,imagem):
        self.cor = cor
        self.imagem = imagem
    def loop(self):
        tela_inicio=False
        while(tela_inicio==False):
            window.fill(self.cor)
            titulo_na_tela = pygame.image.load(self.imagem)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tela_inicio = True
            window.blit(titulo_na_tela,(0,0))
            pygame.display.flip() 
#===TELA DE INICIO===
tela_de_inicio = Tela((0,0,0),'img/mesa_final.png').loop()

#==TELA DAS INSTRUCOES==
tela_de_instrucoes = Tela((0,0,0),'img/instrucoes_blackjack.png').loop()
class Blitador():
    def __init__(self,dicio):
        self.dicio = dicio
    def bliter(self):
        for k,v in self.dicio.items():
            window.blit(font.render(k, 1, black),v)
# textos
Blackjack = font.render('BlackJack!' , True , white)
#TEXTO DE FINAL DE RODADA
Gameover = font.render('Acabou a rodada' , True , white)
#TEXTO INICIO DA RADADA
Reiniciar = font.render('Nova rodada' , True , white)
#TEXTO PARA AVISAR SE JOGAR VENCEU OU PERDEU
Vitoria = font.render('Você ganhou!', True, white)
Derrota = font.render('Você perdeu!', True,white)

#Montar tela
background = pygame.Surface(window.get_size())
background = background.convert()
background.fill((80, 150, 15))
compra = pygame.draw.rect(background, color_dark, (20, HEIGHT - 40, 130, 40))
continua = pygame.draw.rect(background, color_dark, (240, HEIGHT - 40, 130, 40))

# ===== Loop principal DO blackjack=====
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
    vitoria_txt = 'Vitórias:' + str(vitoria)
    empate_txt = 'Empates: ' + str(empate)
    derrota_txt = 'Derrotas: ' + str(derrota)
    Pontu_jogador = 'cartas Jogador: ' + str(jogador)
    if gameover or continuar:
        Pontu_banco = 'Cartas Banco: ' + str(banco)
    elif gameover == False or continuar == False:
        Pontu_banco = 'Cartas Banco: ' + str(banco - pontuacao(carta_banco2))

    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or continuar) and compra.collidepoint(pygame.mouse.get_pos()):
            #da carta ao jogador se ele nao quebra as regras do blackjack
            carta = embaralhar(cartas, mao_jogador)
            jogador += pontuacao(carta)
            print('Jogador: {}' .format(jogador))
            if jogador > 21 and (carta_jogador1 in CartaA or carta_jogador2 in CartaA) and Subtraiu == False:
                jogador -= 10
                Subtraiu = True
            if jogador > 21 and carta in CartaA:
                jogador -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and continua.collidepoint(pygame.mouse.get_pos()):
            continuar = True
            while banco <= jogador and banco < 17:    
                carta = embaralhar(cartas, mao_banco)
                banco += pontuacao(carta)
                print('Banco: {}' .format(banco))
                if banco > 21 and (carta_banco1 in CartaA or carta_banco2 in CartaA) and Subtraiu2 == False:
                    banco -= 10
                    Subtraiu2 = True
                if banco > 21 and carta in CartaA:
                    banco -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or continuar) and reiniciarb.collidepoint(pygame.mouse.get_pos()):
            if jogador == banco:
                empate += 1
            elif jogador > 21:
                derrota += 1
            elif jogador == 21 or (banco < jogador and jogador <= 21) or banco > 21:
                vitoria += 1
            else:
                derrota += 1
            gameover = False
            continuar = False
            Subtraiu = False
            Subtraiu2 = False
            cartas = copy.copy(baralho)
            mao_jogador = []
            mao_banco = []
            jogador, banco, carta_jogador1, carta_jogador2, carta_banco1, carta_banco2 = inicio(cartas, mao_jogador, mao_banco)
            reiniciarb = pygame.draw.rect(background, (80, 150, 15), (WIDTH/2, HEIGHT/2 + 10, 180, 26))
    window.blit(background, (0, 0))
    dicionario = {vitoria_txt:(WIDTH - 150, HEIGHT - 90),empate_txt:(WIDTH - 150, HEIGHT - 70),derrota_txt:(WIDTH - 150,HEIGHT - 50),Pontu_jogador:(735, HEIGHT - 90),Pontu_banco:(735, 40),"Comprar":(25, HEIGHT - 40),"Continuar":(240, HEIGHT - 40)}
    Blitador(dicionario).bliter()

    # mostrar carta do banco
    for card in mao_banco:
        x = 10 + mao_banco.index(card) * 110
        window.blit(card, (x, 20))
    window.blit(C_costas, (120, 20))

    # mostrar carta do jogador
    for card in mao_jogador:
        x = 10 + mao_jogador.index(card) * 110
        window.blit(card, (x, HEIGHT - 200))

    # Mostrar segunda carta do banco e perguntar do reinicio
    if gameover or continuar:
        window.blit(Gameover, ((WIDTH/2), (HEIGHT/2) - 30))
        reiniciarb = pygame.draw.rect(background, gray, (WIDTH/2, HEIGHT/2 + 10, 180, 26))
        window.blit(Reiniciar, (WIDTH/2 + 10, HEIGHT/2 + 10))
        window.blit(mao_banco[1], (120, 20))
            
    pygame.display.update()


