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


# Perguntar quantos jogadores vão jogar

j = int(input('Quantos jogadores vão jogar?'))
i = 0

# Perguntar quantas fichas cada jogador quer comprar
Fichas = [0] * j
Preco = [0] * j

while i < j:
    Fichas[i] = int(input("Quantas fichas o jogador {0} gostaria de adquirir? " .format(i + 1)))
    Preco[i] = 10 * Fichas[i]
    print("Seu total é de R${0}!" .format(Preco[i]))
    i += 1

while True:
    # Perguntar quantas fichas deseja apostar
    z = 0
    Aposta = [0] * j
    Falta = [0] * j
    while z < j: 
        Aposta[z] = int(input("Qual será a aposta do jogador {0}? " .format(z + 1)))
        if Aposta[z] < 1:
            print("Não tenha medo! Hoje senti que a sorte está do seu lado.")
        elif Aposta[z] > Fichas[z]:
            Falta[z] = Aposta[z] - Fichas[z]
            r = input("Você não tem todas essas fichas, gostaria de comprar mais {0} fichas?(s ou n) " .format(Falta[z]))
            if r == 's':
                print('Você comprou {0} fichas! Vamos jogar!' .format(Falta[z]))
                Fichas[z] += Falta[z]
                Fichas[z] -= Aposta[z]
            else:
                Aposta[z] = int(input("Qual será sua aposta? "))
        else:
            Fichas[z] -= Aposta[z]

        time.sleep(2)
        z += 1

    # Perguntar em quem deseja apostar
    Apostado = [0] * j
    a = 0
    while a < j:
        Apostado[a] = input("Em quem o jogador {0} deseja apostar?(jogador, banco ou empate) " .format(a + 1))
        a += 1

    # embaralhando e selecionando as cartas dos jogadores
    random.shuffle(baralho)

    mao_banco = baralho[(j + 1) * 2:(j+1) * 2 + 2]
    maos_jogadores = [0] * j
    m = 0 
    while m < j:
        maos_jogadores[m] = baralho[m * 2:m * 2 + 2]
        print("As cartas do jogador {0} são {1}" .format((m+1),maos_jogadores[m]))
        m += 1
    time.sleep(2)
    print("As cartas do banco são {0}" .format(mao_banco))

    # colocando os valores nas do jogador:

    v = 0
    jogador = [0] * j
    while v < j:
        if maos_jogadores[v][0][0] == 'A':
            pont1 = 1
        elif maos_jogadores[v][0][0] == '10' or maos_jogadores[v][0][0] == 'J' or maos_jogadores[v][0][0] == 'Q' or maos_jogadores[v][0][0] == 'K':
            pont1 = 0
        elif int(maos_jogadores[v][0][0]) < 10:
            pont1 = int(maos_jogadores[v][0][0])

        if maos_jogadores[v][1][0] == 'A':
            pont2 = 1
        elif maos_jogadores[v][1][0] == '10' or maos_jogadores[v][1][0] == 'J' or maos_jogadores[v][1][0] == 'Q' or maos_jogadores[v][1][0] == 'K':
            pont2 = 0
        elif int(maos_jogadores[v][1][0]) < 10:
            pont2 = int(maos_jogadores[v][1][0])
        jogador[v] = pont1 + pont2
        v += 1

    # colocando valores nas cartas do banco:
    if mao_banco[0][0] == 'A':
        pontu1 = 1
    elif mao_banco[0][0] == '10' or mao_banco[0][0] == 'J' or mao_banco[0][0] == 'Q' or mao_banco[0][0] == 'K':
        pontu1 = 0
    elif int(mao_banco[0][0]) < 10:
        pontu1 = int(mao_banco[0][0])

    if mao_banco[1][0] == 'A':
        pontu2 = 1
    elif mao_banco[1][0] == '10' or mao_banco[1][0] == 'J' or mao_banco[1][0] == 'Q' or mao_banco[1][0] == 'K':
        pontu2 = 0
    elif int(mao_banco[1][0]) < 10:
        pontu2 = int(mao_banco[1][0])
    banco = pontu1 + pontu2

    # Definindo a pontuação

    # Checando o vencedor
    
    f = 0
    j_venceu = [False] * j
    b_venceu = False
    while f < j:
        if jogador[f] >= 10:
            jogador[f] -= 10
        if jogador[f] == 9 or jogador[f] == 8:
            print('O jogador {0} alcançou a pontuação desejada' .format(f + 1))
            j_venceu[f] = True
        f += 1
    if banco >= 10:
        banco -= 10
    if banco == 9 or banco == 8:
        print('O banco alcançou a pontuação desejada')
        b_venceu = True

    # Caso os valores estejam abaixo de 6

    s = 0
    vencedor = False
    terceira_carta = False
    while s < j:
        if jogador[s] < 6 and b_venceu == False and vencedor == False:
            print('Você tem {0} pontos. Vamos lhe dar mais uma carta!' .format(jogador[s]))
            terceira_carta = True
            maos_jogadores[s] += baralho[(j + s + 2) * 2]
            time.sleep(2)
            print("Sua carta é {0}" .format(maos_jogadores[s][2]))
            if maos_jogadores[s][2][0] == 'A':
                pont3 = 1
            elif maos_jogadores[s][2][0] == '10' or maos_jogadores[s][2][0] == 'J' or maos_jogadores[s][2][0] == 'Q' or maos_jogadores[s][2][0] == 'K':
                pont3 = 0
            elif int(maos_jogadores[s][2][0]) < 10:
                pont3 = int(maos_jogadores[s][2][0])
            jogador[s] += pont3
        if jogador[s] == 9 or jogador[s] == 8 and j_venceu[s] == False:
            print('O jogador {0} alcançou a pontuação desejada' .format(s + 1))
            j_venceu[s] = True
            vencedor = True
        elif jogador[s] >= 10:
                jogador[s] -= 10
        time.sleep(1)
        print("O jogador {0} tem {1} pontos" .format(s + 1, jogador[s]))
        s += 1

    if banco < 6 and vencedor != True and terceira_carta != True:
        q = 0
        if banco < 4 and maos_jogadores[q] != 8:
            print('O banco tem {0} pontos. Vamos comprar mais uma carta!' .format(banco))
            mao_banco += baralho[j * 2 + 3]
            time.sleep(2)
            print("A carta do banco é {0}" .format(mao_banco[2]))
            q += 1
        elif banco == 4 and maos_jogadores[q] > 1 and maos_jogadores[q] < 8:
            print('O banco tem {0} pontos. Vamos comprar mais uma carta!' .format(banco))
            mao_banco += baralho[j * 2 + 3]
            time.sleep(2)
            print("A carta do banco é {0}" .format(mao_banco[2]))
            q += 1
        elif banco == 5 and maos_jogadores[q] > 3 and maos_jogadores[q] < 8:
            print('O banco tem {0} pontos. Vamos comprar mais uma carta!' .format(banco))
            mao_banco += baralho[j * 2 + 3]
            time.sleep(2)
            print("A carta do banco é {0}" .format(mao_banco[2]))
            q += 1
        elif banco == 6 and maos_jogadores[q] == 6 or maos_jogadores[q] == 7:
            print('O banco tem {0} pontos. Vamos comprar mais uma carta!' .format(banco))
            mao_banco += baralho[j * 2 + 3]
            time.sleep(2)
            print("A carta do banco é {0}" .format(mao_banco[2]))
            q += 1
        if mao_banco[2][0] == 'A':
            pont3 = 1
        elif mao_banco[2][0] == '10' or mao_banco[2][0] == 'J' or mao_banco[2][0] == 'Q' or mao_banco[2][0] == 'K':
            pont3 = 0
        elif int(mao_banco[2][0]) < 10:
            pont3 = int(mao_banco[2][0])
        banco += pont3
    elif banco < 6 and vencedor != True and terceira_carta == True:
        print('O banco tem {0} pontos. Vamos comprar mais uma carta!' .format(banco))
        mao_banco += baralho[j * 2 + 3]
        time.sleep(2)
        print("A carta do banco é {0}" .format(mao_banco[2]))
        if mao_banco[2][0] == 'A':
            pont3 = 1
        elif mao_banco[2][0] == '10' or mao_banco[2][0] == 'J' or mao_banco[2][0] == 'Q' or mao_banco[2][0] == 'K':
            pont3 = 0
        elif int(mao_banco[2][0]) < 10:
            pont3 = int(mao_banco[2][0])
        banco += pont3
    if banco == 9 or banco == 8 and b_venceu == False:
        print('O banco alcançou a pontuação desejada')
        b_venceu = True
    if banco >= 10:
        banco -= 10
    time.sleep(1)
    print("O banco tem {0} pontos" .format(banco))

    # Definindo o vencedor

    t = 0
    time.sleep(2)
    while t < j:
        if jogador[t] == 9 and banco != 9 or jogador[t] > banco:
            if Apostado[t] == 'jogador':
                print('O jogador {0} ganhou!!!' .format(t + 1))
                if baralho == baralho1:
                    Fichas[t] += math.floor(Aposta[t] * 1.9871)
                else:
                    Fichas[t] += math.floor(Aposta[t] * 1.9876)
            else:
                print("O jogador {0} perdeu! Deveria ter apostado em si mesmo hein?" .format(t + 1))
        elif jogador[t] == banco:
            if Apostado[t] == 'empate':
                print('O jogador {0} ganhou!!!' .format(t + 1))
                if baralho == baralho1:
                    Fichas[t] += math.floor(Aposta[t] * 1.8425)
                elif baralho == baralho6:
                    Fichas[t] += math.floor(Aposta[t] * 1.8556)
                else:
                    Fichas[t] += math.floor(Aposta[t] * 1.8564)
            else:
                print('O jogador {0} perdeu! O jogo empatou.' .format(t + 1))
        elif banco == 9 and jogador[t] != 9 or banco > jogador[t]:
            if Apostado[t] == 'banco':
                print('O jogador {0} ganhou!!!' .format(t + 1))
                if baralho == baralho1:
                    Fichas[t] += math.floor(Aposta[t] * 0.95 * 1.9899)
                else:
                    Fichas[t] += math.floor(Aposta[t] * 0.95 * 1.9894)
            else:
                print("O jogador {0} perdeu! A casa sempre sai vencendo." .format(t + 1))
        t += 1
    
    #Checando se o jogador quer continuar jogando

    jogar_mais = input("Vamos mais uma?(S ou N)")
    if jogar_mais == 'N':
        v = 0
        while v < j:
            print('Ok, aqui estão suas {0} fichas jogador {1}, obrigado por jogar!' .format(Fichas[v], v + 1))
            v += 1
        break

