import random
import time

clear = lambda: print("\n"*100)


#INTERFACE DO JOGO:

def cabecalho(): #explicita a definição da função (cabecalho) naquele ponto.
	print("|======================================|")
	print("|           JOGO DA VELHA              |")
	print("|======================================|")

def placar():
	print("|               PLACAR                 |")
	print("|       ( O ) => "+str(O)+"  "+str(X)+"  <= ( X )        |")
	print("|EMPATES => "+str(empate)+"                          |")
	print("|======================================|")
	print("|Jogando =>  "+str(jogando)+"                         |")	 
	print("|======================================|")	 

def velha():
	print("|  |-----------------|                 |")
	print("|  |  "+str(V[0][0])+"  |  "+str(V[0][1])+"  |  "+str(V[0][2])+"  |")
	print("|  |-----------------|                 |")
	print("|  |  "+str(V[1][0])+"  |  "+str(V[1][1])+"  |  "+str(V[1][2])+"  |")
	print("|  |-----------------|                 |")
	print("|  |  "+str(V[2][0])+"  |  "+str(V[2][1])+"  |  "+str(V[2][2])+"  |")
	print("|  |-----------------|                 |")
	print("|--------------------------------------|")

#FUNÇÕES AUXILIARES:

def jogador(): #escolha o jogador
    return 'X' if random.randint(1,2) == 1 else 'O'

def jogou(msg): #msg é uma biblioteca de mensagem, usada para configura banco de dados e pode ser usada para bate-papo
    while True: #while = O comando faz um conjunto de instruções seja executado enquanto uma condição é atendida.
        try: #O bloco try permite testar um bloco de código quanto a erros.
            jogada = input(msg)
            return int(jogada[0])
        except: #O bloco try permite testar um bloco de código quanto a erros.
            print("Tente novamente!")

def questao(msg, erro="Digite S para sim e N para não"):
    while True:
        try:
            r = input(msg)
            if( r[0].lower() == 's'):
                return True
            elif( r[0].lower() == 'n'):
                return False
            else:
                print("erro")

        except:
            print("Tente novamente!")

#PRINCIPAIS FUNÇÕES:

def jogoGanho():
    for i in range(3):
        for j in range(3):
            if (V[0][0] == V[0][1] == V[0][2]):
                return True
            elif (V[1][0] == V[1][1] == V[1][2]):
                return True
            elif (V[2][0] == V[2][1] == V[2][2]):
                return True
            elif (V[0][0] == V[1][1] == V[2][2]):
                return True
            elif (V[0][0] == V[1][0] == V[2][0]):
                return True
            elif (V[0][1] == V[1][1] == V[2][1]):
                return True
            elif (V[0][2] == V[1][2] == V[2][2]):
                return True
            elif (V[2][0] == V[1][1] == V[0][2]):
                return True
            else:
                return False

def jogoEmpatado(): 
    for i in range(3): #range = gerando uma lista com a função #for = execulta um ciclo para execução do objeto 
        for j in range(3):
            if str(V[i][j]).isdecimal(): #O método isdecimal() retornará True se todos os caracteres forem decimais, caso contrário, False.
                return False

    return True #return = retornarmos valores por funções
    

#====================
X = 0
O = 0
empate = 0 

play = True

while play:
    jogando = jogador()
    V = [[1,2,3], [4,5,6], [7,8,9]]

    while True:        
        clear()
        cabecalho(); placar(); velha()
        jogada = jogou("| Escolha o número de acordo com a posição que você deseja: ")

        jogadaAceite = False #validação
        for i in range(3):
            for j in range(3):
                if jogada ==  V[i][j]:
                    V[i][j] = jogando
                    jogadaAceite = True

        if jogadaAceite: # verificar se jogo foi ganho ou empate
            if jogoGanho():
                print("Parabéns! " + jogando + " Ganhou!")
                if jogando == "X":
                    X += 1
                else:
                    O += 1
                time.sleep(3)
                break 
                
            if jogoEmpatado():
                print("| Jogo empatado |")
                time.sleep(3)
                empate += 1 
                break
            else:
                jogando = "X" if jogando == 'O' else 'O'
        
        else:
            print("|Tente novamente!")
            time.sleep(3)  #comando de suspensão do shell Bash. da a parada por 3s no programa

    if not questao("Deseja continuar jogando? [S/N]:  "):
        break
