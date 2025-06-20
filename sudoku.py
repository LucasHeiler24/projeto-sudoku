soduku = []

#Essa função valida a jogada para ser entre 1 e 9
def validarJogadas(jogada):
    if(jogada < 1 or jogada > 9):
        return 0
    return 1

#Essa função valida a entrada de linhas e colunas válidas entre 1-9
def validarLinhaColuna(linha, coluna):
    if(linha < 1 or linha > 9):
        return 0
    elif(coluna < 1 or coluna > 9):
        return 0
    return 1

#Essa função verefica se o usuário insere a jogada em uma posição que já existe um número
def validarPosicao(linha, coluna):
    if(soduku[linha-1][coluna-1] > 0):
        return 0
    return 1

#Aqui eu verefico cada coluna da minha matriz
def validarColunaTabuleiro(c):
    for i in range(9):
        for j in range(i+1, 9):
            if soduku[i][c-1] == soduku[j][c-1] and soduku[i][c-1] > 0 and soduku[j][c-1] > 0:
                return 0
    return 1

#Aqui eu verefico cada linha da matriz
def validarLinhaTabuleiro(l):
    for i in range(9):
        for j in range(i+1, 9):
            if soduku[l-1][i] == soduku[l-1][j] and soduku[l-1][i] > 0 and soduku[l-1][j] > 0:
                return 0
    return 1

#Aqui eu faço os laços de repetição de cada quadrante da matriz
def validarQuadrante(linha, coluna, numUsuario):
    cont = 0
    if(coluna < 3):
        if(linha == 3):
            for i in range(linha):
                for j in range(3):
                    if soduku[i][j] == numUsuario:
                        cont += 1
        elif linha == 5:
            for i in range(3, linha+1):
                for j in range(3):
                    if soduku[i][j] == numUsuario:
                        cont += 1
        else:
            for i in range(6, linha+1):
                for j in range(3):
                    if soduku[i][j] == numUsuario:
                        cont += 1
    elif(coluna < 6):
        if(linha == 3):
            for i in range(linha):
                for j in range(3, 6):
                    if soduku[i][j] == numUsuario:
                        cont += 1
        elif linha == 5:
            for i in range(3, linha+1):
                for j in range(3, 6):
                    if soduku[i][j] == numUsuario:
                        cont += 1
        else:
            for i in range(6, linha+1):
                for j in range(3, 6):
                    if soduku[i][j] == numUsuario:
                        cont += 1
    else:
        if(linha == 8):
            for i in range(linha):
                for j in range(6, 9):
                    if soduku[i][j] == numUsuario:
                        cont += 1
        elif linha == 5:
            for i in range(3, linha+1):
                for j in range(6, 9):
                    if soduku[i][j] == numUsuario:
                        cont += 1
        else:
            for i in range(6, linha+1):
                for j in range(6, 9):
                    if soduku[i][j] == numUsuario:
                        cont += 1
    if(cont > 1):
        return 0
    return 1 

#Essa função verefica o quadrante de cada parte do tabuleiro
def validarQuadranteTabuleiro(linha, coluna, numUsuario):
    resultado = 1

    if(linha < 3):
        resultado = validarQuadrante(3, coluna, numUsuario)
    elif(linha < 5):
        resultado = validarQuadrante(5, coluna, numUsuario)
    else:
        resultado = validarQuadrante(8, coluna, numUsuario)

    return resultado


#Essa função monta o meu tabuleiro
def montaTabuleiro():
    for i in range(9):
        vetor = []
        for j in range(9):
            vetor.append(0)
        soduku.append(vetor)

#Essa função mostra o tabuleiro
def mostrarTabuleiro():
    for i in soduku:
        print(i)

#Essa função determina se ganhou
def vencerJogo():
    cont = 0
    for i in range(9):
        for j in range(9):
            if soduku[i][j] != 0:
                cont += 1
    
    if(cont == 81):
        return 1
    return 0

#Essa função monta com que o usuário preenche o tabuleiro antes
def usuarioMontaTabuleiro():
    cont = 10

    print("===========HORA DE MONTAR O TABULEIRO===========\n")
    print("Você tem 10 números de 1 a 9 para colocar no tabuleiro!")
    print("Lembre-se das regras do jogo, sem numeros iguais em linhas, colunas e quadrantes!")
    print("Bom jogo...\n")

    while cont != 0:
        jogadaUsuario = int(input(f"{cont}° Número: Informe um número entre 1 e 9: ")) 

        while(validarJogadas(jogadaUsuario) == 0):
            jogadaUsuario = int(input(f"{cont}° Número: Informe um número entre 1 e 9: "))

        linha = int(input(f"{cont}° Número: Informe uma linha que deseja colocar o número: (1 até 9): "))
        coluna = int(input(f"{cont}° Número: Informe uma coluna que deseja colocar o número: (1 até 9): "))
        
        while(validarLinhaColuna(linha, coluna) == 0):
            linha = int(input(f"{cont}° Número: Informe uma linha que deseja colocar o número: (1 até 9): "))
            coluna = int(input(f"{cont}° Número: Informe uma coluna que deseja colocar o número: (1 até 9): "))


        if(validarPosicao(linha, coluna) == 0):
            print("Opss...Essa posição já existe uma jogada!")
        else:
            soduku[linha-1][coluna-1] = jogadaUsuario

            if(validarColunaTabuleiro(coluna) == 0):
                print("Opss..Esse número já existe nessa coluna!")
                soduku[linha-1][coluna-1] = 0

            elif(validarLinhaTabuleiro(linha) == 0):
                print("Opss..Esse número já existe nessa linha!")
                soduku[linha-1][coluna-1] = 0

            elif(validarQuadranteTabuleiro(linha-1, coluna-1, jogadaUsuario) == 0):
                print("Opss..Esse número já existe nesse quadrante!")
                soduku[linha-1][coluna-1] = 0
            else:
                soduku[linha-1][coluna-1] = jogadaUsuario
                print("Jogada colocada com sucesso!")
                mostrarTabuleiro()
                cont -= 1
    menu()

#Essa função abre um menu de vencedor
def menuVencedor():
    print("Deseja jogar novamente?\n")
    opUsuario = int(input("1-Jogar novamente\n2-Sair do sistema\n"))

    while(opUsuario != 2):
        match opUsuario:
            case 1:
                soduku.clear()
                montaTabuleiro()
                usuarioMontaTabuleiro()
            case 2:
                break
            case _:
                print("Informe uma opção válida!")
        
        opUsuario = int(input("1-Jogar novamente\n2-Sair do sistema\n"))

#Essa função pede pro usuário uma jogada
def inserirJogada():
    jogadaUsuario = int(input("Informe um número entre 1 e 9: ")) 

    while(validarJogadas(jogadaUsuario) == 0):
        jogadaUsuario = int(input("Informe um número entre 1 e 9: "))

    linha = int(input("Informe uma linha que deseja colocar o número: (1 até 9): "))
    coluna = int(input("Informe uma coluna que deseja colocar o número: (1 até 9): "))
    
    while(validarLinhaColuna(linha, coluna) == 0):
        linha = int(input("Informe uma linha que deseja colocar o número: (1 até 9): "))
        coluna = int(input("Informe uma coluna que deseja colocar o número: (1 até 9): "))


    if(validarPosicao(linha, coluna) == 0):
        print("Opss...Essa posição já existe uma jogada!")
        inserirJogada()
    else:
        soduku[linha-1][coluna-1] = jogadaUsuario

        if(validarColunaTabuleiro(coluna) == 0):
            print("Opss..Esse número já existe nessa coluna!")
            soduku[linha-1][coluna-1] = 0
            inserirJogada()

        if(validarLinhaTabuleiro(linha) == 0):
            print("Opss..Esse número já existe nessa linha!")
            soduku[linha-1][coluna-1] = 0
            inserirJogada()

        if(validarQuadranteTabuleiro(linha-1, coluna-1, jogadaUsuario) == 0):
            print("Opss..Esse número já existe nesse quadrante!")
            soduku[linha-1][coluna-1] = 0
            inserirJogada()

        print("Jogada colocada com sucesso!")
        mostrarTabuleiro()
        
        if vencerJogo():
            print("==============PARABÉNS VOCÊ GANHOU O JOGO===============\n")
            menuVencedor()
        menu()

#Essa função exibe um menu pro usuário
def menu():
    print("=========MENU========\n1-Inserir jogada\n2-Ver tabuleiro\n0-Sair")
    opcaoUsuario = int(input("Informe a opção: "))
    while(opcaoUsuario != 0):
        match opcaoUsuario:
            case 1:
                inserirJogada()
            case 2:
                mostrarTabuleiro()
            case _:
                print("Informe uma jogada válida!")
        opcaoUsuario = int(input("Informe a opção: "))

#Função main que apenas chama as funções do projeto
def main():
    montaTabuleiro()
    usuarioMontaTabuleiro()

main()