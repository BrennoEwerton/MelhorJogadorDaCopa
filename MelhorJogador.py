def menu():
    print("""
        Escolha uma opção:
            1 - Votar
            2 - Ver resultados
        """)
    opcao = int(input("Digite sua opção:"))

    #Faltando:
    #Validar se digitar algo inválido!

    return opcao
    
def lerJogadores():
    arq = open("jogadores.txt", "r", encoding="ISO-8859-1")
    conteudo = arq.read()
    listaJogadores = conteudo.split("\n")
    resultado = []
    for j in listaJogadores:
        resultado.append(j.split("#"))
    arq.close()
    return resultado

def salvarVoto(jogador):
    arq = open("votos.txt", "a", encoding="UTF-8")
    arq.writelines("#".join(jogador) + '\n')
    arq.close()

def verResultados():
    pass

def filtraJogadoresPorPais(pais, lista):
    listaFiltrados = []
    for jogador in lista:
        paisDoJogador = jogador[0]
        if paisDoJogador == pais:
            listaFiltrados.append(jogador)
    return listaFiltrados

def escolherJogador(listaJogadores):
    idsValidos = []
    for jogador in listaJogadores:
        print(jogador[1] + ". " + jogador[2])
        idsValidos.append(jogador[1])
    
    jogadorEscolhido = str(input("Informe um ID: "))
    while not (jogadorEscolhido in idsValidos):
        print("Jogador inválido")  
        jogadorEscolhido = str(input("Informe um ID: "))
    
    jogadorDados = []
    for jogador in listaJogadores:
        if jogador[1] == jogadorEscolhido:
            jogadorDados.extend(jogador)
            break
    return jogadorDados

escolha = menu()
if escolha == 1:
    lista = lerJogadores()
    pais = str(input("Informe o país desejado: "))
    jogadores = filtraJogadoresPorPais(pais, lista)
    
    jogadorEscolhido = escolherJogador(jogadores)
    salvarVoto(jogadorEscolhido)
    
    #Falta:
    #printar os jogadores filtrados
    #pedir para o usuário escolher um jogador
    #filtrar para saber se o jogador existe (no páis)
    #salvar voto
    
elif escolha == 2:
    verResultados()

