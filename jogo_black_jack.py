import random
jogo = True

fichas_totais = int(input('quantas fichas voce tem no total?: '))

#quanto vai apostar

quanto_vai_apostar = int(input('Quanto deseja apostar?: '))


while jogo :
    # definicao das cartas do banco e do jogador e depois suas somas
    black_jack = True
    proximas_rodadas = True
    lista_com_valores = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    lista_de_cartas = lista_com_valores*4
    a = random.choice(lista_de_cartas)
    b = random.choice(lista_de_cartas)
    lista_jogador = [a,b]
    c = random.choice(lista_de_cartas)
    d = random.choice(lista_de_cartas)
    e = random.choice(lista_de_cartas)
    f = random.choice(lista_de_cartas)
    lista_banco = [c,d]
    virada_cima = lista_banco[0]
    virada_baixo = lista_banco[1]
    soma_jogador = (lista_jogador[0] + lista_jogador[1])
    soma_banco = (lista_banco[0])

    continuar_com_carta_extra = True
    continuar = input('a soma de suas cartas eh {0}, e a do banco eh {1}.Deseja continuar jogando?s/n '.format(soma_jogador,soma_banco))




    #condicos para saber a quantidade final de fichas pos rodada
    while continuar_com_carta_extra :
        if continuar == 's' :
            lista_jogador.append(e)
            soma_jogador = lista_jogador[0] + lista_jogador[1] + lista_jogador[2]
            soma_banco = lista_banco[0] + lista_banco[1]
        else :
            continuar_com_carta_extra = False


        if soma_jogador > soma_banco  and continuar_com_carta_extra:
            fichas_totais += quanto_vai_apostar
            print('jogador ganhou e agora tem {0}'.format(fichas_totais))
            continuar_com_carta_extra = False

        elif soma_banco > soma_jogador :
            fichas_totais -= quanto_vai_apostar
            print('jogador perdeu e agora tem {0}'.format(fichas_totais))
            continuar_com_carta_extra = False

        elif soma_jogador >= 21 :
            fichas_totais -= quanto_vai_apostar
            print('jogador perdeu e agora tem {0}.a soma de sua cartar era maior ou igaula  21'.format(fichas_totais))
            continuar_com_carta_extra = False

        elif soma_banco == soma_jogador :
            fichas_totais = fichas_totais
            print('Deu empate.Jogador tem {0}'.format(fichas_totais))
            continuar_com_carta_extra = False




    if fichas_totais > 0 :
            quer_continuar = input('Deseja continuar?(sim/nao): ')
            if quer_continuar == 'sim' :
                quanto_vai_apostar = int(input('Quanto deseja apostar?(maximo possivel e de {0}): '.format(fichas_totais)))
            else :
                jogo = False
    else :
        jogo = False