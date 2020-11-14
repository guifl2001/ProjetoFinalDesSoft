from collections import namedtuple
from itertools import product
import random
import time
import math
# criando o baralho
Carta = namedtuple('Carta', ['face', 'naipe'])

faces = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
naipes = {'O', 'P', 'C', 'E'}

baralho = [Carta(face, naipe) for face, naipe in product(faces, naipes)]

# Perguntar quantas fichas o jogador quer comprar
Fichas = int(input("Quantas fichas gostaria de adquirir? "))
Preco = 10 * Fichas
print("Seu total é de R${0}!" .format(Preco))

while True:
    # Perguntar quantas fichas deseja apostar

    Aposta = int(input("Qual será sua aposta?"))
    if Aposta < 1:
        print("Não tenha medo! Hoje senti que a sorte está do seu lado.")
    elif Aposta > Fichas:
        Falta = Aposta - Fichas
        r = input("Você não tem todas essas fichas, gostaria de comprar mais {0} fichas?(s ou n) " .format(Falta))
        if r == 's':
            print('Você comprou {0} fichas! Vamos jogar!' .format(Falta))
            Fichas += Falta
            Fichas -= Aposta
        else:
            Aposta = int(input("Qual será sua aposta? "))
    else:
        print('Vamos jogar!')
        Fichas -= Aposta

    time.sleep(2)

    # embaralhando e selecionando as cartas dos jogadores
    random.shuffle(baralho)

    mao_jogador = baralho[0:2]
    mao_banco = baralho[2:4]
    print("Suas cartas são {0}" .format(mao_jogador))
    time.sleep(2)
    print("As cartas do banco são {0}" .format(mao_banco))

    # colocando os valores nas do jogador:
    if mao_jogador[0][0] == 'A':
        pont1 = 11
    elif mao_jogador[0][0] == '10' or mao_jogador[0][0] == 'J' or mao_jogador[0][0] == 'Q' or mao_jogador[0][0] == 'K':
        pont1 = 10
    elif int(mao_jogador[0][0]) < 10:
        pont1 = int(mao_jogador[0][0])

    if mao_jogador[1][0] == 'A':
        pont2 = 11
    elif mao_jogador[1][0] == '10' or mao_jogador[1][0] == 'J' or mao_jogador[1][0] == 'Q' or mao_jogador[1][0] == 'K':
        pont2 = 10
    elif int(mao_jogador[1][0]) < 10:
        pont2 = int(mao_jogador[1][0])
    jogador = pont1 + pont2
    if jogador > 21 and (mao_jogador[0][0] == 'A' or mao_jogador[1][0] == 'A'):
        jogador -= 10

    # colocando valores nas cartas do banco:
    if mao_banco[0][0] == 'A':
        pontu1 = 11
    elif mao_banco[0][0] == '10' or mao_banco[0][0] == 'J' or mao_banco[0][0] == 'Q' or mao_banco[0][0] == 'K':
        pontu1 = 10
    elif int(mao_banco[0][0]) < 10:
        pontu1 = int(mao_banco[0][0])

    if mao_banco[1][0] == 'A':
        pontu2 = 11
    elif mao_banco[1][0] == '10' or mao_banco[1][0] == 'J' or mao_banco[1][0] == 'Q' or mao_banco[1][0] == 'K':
        pontu2 = 10
    elif int(mao_banco[1][0]) < 10:
        pontu2 = int(mao_banco[1][0])
    banco = pontu1 + pontu2
    if banco > 21 and (mao_banco[0][0] == 'A' or mao_banco[1][0] == 'A'):
        banco -= 10

    # Definindo a pontuação

    # Checando o vencedor
    
    j_venceu = False
    b_venceu = False
    if jogador == 21:
        print('O jogador alcançou a pontuação desejada')
        j_venceu = True
    if jogador > 21:
        print('O jogador ultrapassou a pontuação desejada')
    if banco == 21:
        print('O banco alcançou a pontuação desejada')
        b_venceu = True
    if banco > 21:
        print('O banco ultrapassou a pontuação desejada')

    # O jogador vai comprar cartas?

    i = 0
    nao = False
    while jogador < 21 and b_venceu == False and nao == False:
        resp = input('Você tem {0} pontos. Deseja mais uma carta?' .format(jogador))
        if resp == 'sim':
            mao_jogador += baralho[i + 3]
            time.sleep(2)
            print("Sua carta é {0}" .format(mao_jogador[(i + 2)][0]))
            if mao_jogador[(i + 2)][0] == 'A' and jogador > 10:
                pont3 = 1
            if mao_jogador[(i + 2)][0] == 'A' and jogador <= 10:
                pont3 = 11
            elif mao_jogador[(i + 2)][0] == '10' or mao_jogador[(i + 2)][0] == 'J' or mao_jogador[(i + 2)][0] == 'Q' or mao_jogador[(i + 2)][0] == 'K':
                pont3 = 10
            elif int(mao_jogador[(i + 2)][0]) < 10:
                pont3 = int(mao_jogador[(i + 2)][0])
            jogador += pont3
            if jogador > 21 and (mao_jogador[0][0] == 'A' or mao_jogador[1][0] == 'A'):
                jogador -= 10
            i += 1
        else:
            nao = True
    if jogador == 21 and b_venceu == False:
        print('BlackJack!')
        j_venceu = True
    elif jogador > 21:
        print('O jogador ultrapassou a pontuação desejada')
    time.sleep(1)

    f = 0
    while banco < 16 or (banco < jogador and jogador < 21) and j_venceu == False:
        mao_banco += baralho[f + i + 3]
        time.sleep(2)
        print("A carta do banco é {0}" .format(mao_banco[(f + 2)]))
        if mao_banco[(f + 2)][0] == 'A' and banco > 10:
            pont3 = 1
        elif mao_banco[(f + 2)][0] == 'A' and banco <= 10:
            pont3 = 11
        elif mao_banco[(f + 2)][0] == '10' or mao_banco[(f + 2)][0] == 'J' or mao_banco[(f + 2)][0] == 'Q' or mao_banco[(f + 2)][0] == 'K':
            pont3 = 10
        elif int(mao_banco[(f + 2)][0]) < 10:
            pont3 = int(mao_banco[(f + 2)][0])
        banco += pont3
        if banco > 21 and (mao_banco[0][0] == 'A' or mao_banco[1][0] == 'A'):
            banco -= 10
        print("O banco tem {0} pontos" .format(banco))
        f += 1
    if banco == 21 and b_venceu == False:
        print('O banco ganhou!')
        b_venceu = True
    if banco > 21:
        print('O banco ultrapassou a pontuação desejada')
    time.sleep(1)

    # Definindo o vencedor

    time.sleep(2)
    if j_venceu == True or (jogador > banco and jogador < 21) or banco > 21:
        print('Você ganhou!!! Aqui está suas {0} fichas' .format(2 * Aposta))
        Fichas += Aposta * 2
    elif b_venceu == True or (banco >= jogador and banco < 21) or jogador > 21:
        print('Você perdeu!')
            
    #Checando se o jogador quer continuar jogando

    jogar_mais = input("Vamos mais uma?(S ou N)")
    if jogar_mais == 'N':
        print('Ok, aqui estão suas {0} fichas, obrigado por jogar!' .format(Fichas))
        break