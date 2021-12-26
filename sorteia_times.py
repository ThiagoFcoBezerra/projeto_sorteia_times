import random

class Time:
    def __init__(self, nome, quant_goleiro, quant_zagueiro, quant_meia, quant_lateral, quant_atacante ):
        self.nome = nome
        self.quant_goleiro = quant_goleiro
        self.quant_zagueiro = quant_zagueiro
        self.quant_meia = quant_meia
        self.quant_lateral = quant_lateral
        self.quant_atacante = quant_atacante
        self.goleiro = []
        self.zagueiro = []
        self.meia = []
        self.lateral = []
        self.atacante = []
        self.vaga = 0

    def __str__(self):
        return 'Isso é um objeto time'

class Jogador:
    def __init__(self, nome, posicao1, posicao2, posicao3, categoria):
        self.nome = nome
        self.posicao1 = posicao1
        self.posicao2 = posicao2
        self.posicao3 = posicao3
        self.categoria = categoria
        self.disponivel = True

    def getnome(self):
        return self.nome
    

    def __str__(self):
        return '[ O {} é {}, {} ]'.format(self.nome, self.posicao1, self.categoria)


lista_time = []
lista_de_jogadores = []

def cadastra_jogador(nome, posicao1, posicao2, posicao3, categoria):
    jogador = Jogador(nome,posicao1,posicao2,posicao3,categoria)
    lista_de_jogadores.append(jogador)

def cria_time(lista_jogadores, quant_goleiro, quant_zagueiro, quant_meia,
                quant_lateral, quant_atacante):
    lista_jogadores = lista_jogadores
    jogadores_por_time = quant_goleiro + quant_zagueiro + quant_meia + quant_lateral + quant_atacante
    quant_time = int(len(lista_jogadores)/jogadores_por_time)
    if quant_time*jogadores_por_time < len(lista_de_jogadores):
        quant_time = quant_time + 1

    #print(quant_time)

    for i in range(quant_time):
        nome = f'Time: {i+1}'
        time = Time(nome, quant_goleiro, quant_zagueiro, quant_meia,
                quant_lateral, quant_atacante)
        if i == quant_time - 1:
            time.vaga = len(lista_de_jogadores)-(quant_time-1)*jogadores_por_time
        else:
            time.vaga = jogadores_por_time
        lista_time.append(time)
        #print(f'{time.nome} tem {time.vaga}')

    return lista_time

def sorteia_time(lista_de_jogadores, lista_time):
    lista = lista_de_jogadores
    
    quant_sorteado = 0
    while quant_sorteado < len(lista):
        
        for index in range(len(lista)):
            
            num_sort = random.randint(0, len(lista_time)-1)
            print(num_sort)

            # Verifica posição 1            
            match (lista[index].posicao1, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].goleiro) < lista_time[num_sort].quant_goleiro):
                case ('goleiro', True, True, True):
                    lista_time[num_sort].goleiro.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1
                
            match (lista[index].posicao1, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].zagueiro) < lista_time[num_sort].quant_zagueiro):
                case ('zagueiro', True, True, True):
                    lista_time[num_sort].zagueiro.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            match (lista[index].posicao1, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].meia) < lista_time[num_sort].quant_meia):
                case ('meia', True, True, True):        
                    lista_time[num_sort].meia.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            match (lista[index].posicao1, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].lateral) < lista_time[num_sort].quant_lateral):
                case ('lateral', True, True, True):
                    lista_time[num_sort].lateral.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            match (lista[index].posicao1, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].atacante) < lista_time[num_sort].quant_atacante):
                case ('atacante', True, True, True):
                    lista_time[num_sort].atacante.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            # Verifica posição 2
            match (lista[index].posicao2, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].goleiro) < lista_time[num_sort].quant_goleiro):
                case ('goleiro', True, True, True):
                    lista_time[num_sort].goleiro.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1
                
            match (lista[index].posicao2, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].zagueiro) < lista_time[num_sort].quant_zagueiro):
                case ('zagueiro', True, True, True):
                    lista_time[num_sort].zagueiro.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            match (lista[index].posicao2, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].meia) < lista_time[num_sort].quant_meia):
                case ('meia', True, True, True):        
                    lista_time[num_sort].meia.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            match (lista[index].posicao2, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].lateral) < lista_time[num_sort].quant_lateral):
                case ('lateral', True, True, True):
                    lista_time[num_sort].lateral.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            match (lista[index].posicao2, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].atacante) < lista_time[num_sort].quant_atacante):
                case ('atacante', True, True, True):
                    lista_time[num_sort].atacante.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            # Verifica posição 3
            match (lista[index].posicao3, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].goleiro) < lista_time[num_sort].quant_goleiro):
                case ('goleiro', True, True, True):
                    lista_time[num_sort].goleiro.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1
                
            match (lista[index].posicao3, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].zagueiro) < lista_time[num_sort].quant_zagueiro):
                case ('zagueiro', True, True, True):
                    lista_time[num_sort].zagueiro.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            match (lista[index].posicao3, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].meia) < lista_time[num_sort].quant_meia):
                case ('meia', True, True, True):        
                    lista_time[num_sort].meia.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            match (lista[index].posicao3, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].lateral) < lista_time[num_sort].quant_lateral):
                case ('lateral', True, True, True):
                    lista_time[num_sort].lateral.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            match (lista[index].posicao3, lista[index].disponivel, lista_time[num_sort].vaga > 0, len(lista_time[num_sort].atacante) < lista_time[num_sort].quant_atacante):
                case ('atacante', True, True, True):
                    lista_time[num_sort].atacante.append(lista[index])
                    lista[index].disponivel = False
                    lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                    quant_sorteado = quant_sorteado + 1

            for index_time in range(len(lista_time)-1):
                match (lista[index].posicao1, lista[index].disponivel, lista_time[index_time].vaga > 0, len(lista_time[index_time].goleiro) < lista_time[index_time].quant_goleiro):   
                    case('goleiro', True, True, True):
                        lista_time[index_time].goleiro.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[index_time].vaga = lista_time[index_time].vaga-1
                        quant_sorteado = quant_sorteado + 1

                match (lista[index].posicao1, lista[index].disponivel, lista_time[index_time].vaga > 0, len(lista_time[index_time].zagueiro) < lista_time[index_time].quant_zagueiro):   
                    case('zagueiro', True, True, True):
                        lista_time[index_time].zagueiro.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[index_time].vaga = lista_time[index_time].vaga-1
                        quant_sorteado = quant_sorteado + 1

                match (lista[index].posicao1, lista[index].disponivel, lista_time[index_time].vaga > 0, len(lista_time[index_time].lateral) < lista_time[index_time].quant_lateral):   
                    case('lateral', True, True, True):
                        lista_time[index_time].lateral.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[index_time].vaga = lista_time[index_time].vaga-1
                        quant_sorteado = quant_sorteado + 1

                match (lista[index].posicao1, lista[index].disponivel, lista_time[index_time].vaga > 0, len(lista_time[index_time].meia) < lista_time[index_time].quant_meia):   
                    case('meia', True, True, True):
                        lista_time[index_time].meia.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[index_time].vaga = lista_time[index_time].vaga-1
                        quant_sorteado = quant_sorteado + 1
            
                match (lista[index].posicao1, lista[index].disponivel, lista_time[index_time].vaga > 0, len(lista_time[index_time].atacante) < lista_time[index_time].quant_atacante):   
                    case('atacante', True, True, True):
                        lista_time[index_time].atacante.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[index_time].vaga = lista_time[index_time].vaga-1
                        quant_sorteado = quant_sorteado + 1  
            
            if lista_time[num_sort].vaga > 0:
                match (lista[index].posicao1, lista[index].disponivel):
                    case ('goleiro', True):
                        lista_time[num_sort].goleiro.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                        quant_sorteado = quant_sorteado + 1

                    case ('zagueiro', True):
                        lista_time[num_sort].zagueiro.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                        quant_sorteado = quant_sorteado + 1

                    case ('lateral', True):
                        lista_time[num_sort].lateral.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                        quant_sorteado = quant_sorteado + 1

                    case ('meia', True):
                        lista_time[num_sort].meia.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                        quant_sorteado = quant_sorteado + 1

                    case ('atacante', True):
                        lista_time[num_sort].atacante.append(lista[index])
                        lista[index].disponivel = False
                        lista_time[num_sort].vaga = lista_time[num_sort].vaga-1
                        quant_sorteado = quant_sorteado + 1
    print(quant_sorteado)
                       

cadastra_jogador('thiago', 'zagueiro', 'meia', 'lateral', 'craque')
cadastra_jogador('thiago1', 'atacante', 'zagueiro', 'meia', 'craque')
cadastra_jogador('thiago2', 'lateral', 'atacante', 'zagueiro', 'craque')
cadastra_jogador('thiago4', 'meia', 'lateral', 'atacante', 'craque')
cadastra_jogador('thiago5', 'zagueiro', 'meia', 'lateral', 'craque')
cadastra_jogador('thiago6', 'atacante', 'zagueiro', 'meia', 'craque')
cadastra_jogador('thiago7', 'goleiro', 'atacante', 'zagueiro', 'craque')
cadastra_jogador('thiago8', 'meia', 'lateral', 'atacante', 'craque')
cadastra_jogador('thiago9', 'zagueiro', 'meia', 'lateral', 'craque')
cadastra_jogador('thiago10', 'atacante', 'zagueiro', 'meia', 'craque')
cadastra_jogador('thiago11', 'lateral', 'atacante', 'zagueiro', 'craque')
cadastra_jogador('thiago12', 'meia', 'lateral', 'atacante', 'craque')
cadastra_jogador('thiago13', 'zagueiro', 'meia', 'lateral', 'craque')
cadastra_jogador('thiago14', 'atacante', 'zagueiro', 'meia', 'craque')
cadastra_jogador('thiago15', 'goleiro', 'atacante', 'zagueiro', 'craque')
cadastra_jogador('thiago16', 'meia', 'lateral', 'atacante', 'craque')
cadastra_jogador('thiago17', 'zagueiro', 'meia', 'lateral', 'craque')
cadastra_jogador('thiago18', 'atacante', 'zagueiro', 'meia', 'craque')
cadastra_jogador('thiago19', 'lateral', 'atacante', 'zagueiro', 'craque')
cadastra_jogador('thiago20', 'meia', 'lateral', 'atacante', 'craque')
cadastra_jogador('thiago21', 'zagueiro', 'meia', 'lateral', 'craque')
cadastra_jogador('thiago22', 'atacante', 'zagueiro', 'meia', 'craque')
cadastra_jogador('thiago23', 'lateral', 'atacante', 'zagueiro', 'craque')
cadastra_jogador('thiago24', 'meia', 'lateral', 'atacante', 'craque')
cadastra_jogador('thiago25', 'goleiro', 'meia', 'lateral', 'craque')
cadastra_jogador('thiago26', 'atacante', 'zagueiro', 'meia', 'craque')
cadastra_jogador('thiago27', 'lateral', 'atacante', 'zagueiro', 'craque')
cadastra_jogador('thiago28', 'meia', 'lateral', 'atacante', 'craque')


lista_time = cria_time(lista_de_jogadores,0,1,2,2,1)

sorteia_time(lista_de_jogadores, lista_time)

for time in lista_time:
    print(time.nome)
    for goleiro in time.goleiro:
        print(f'goleiro :{goleiro}')
    for zagueiro in time.zagueiro:
        print(f'zagueiro:{zagueiro}')
    for meia in time.meia:
        print(f'meia    :{meia}')
    for lateral in time.lateral:
        print(f'lateral :{lateral}')
    for atacante in time.atacante:
        print(f'atacante:{atacante}')