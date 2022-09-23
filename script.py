import random, sys
random.choice(["a", "b", "c", "d", "e"])

jogadas = ["pedra", "papel", "tesoura"]

vitorias_user = 0
vitorias_computador = 0

def jogada_ai():
    escolha = random.choice(jogadas)
    return escolha

def quem_ganha(jogador1, jogador2):
    global vitorias_user
    global vitorias_computador
    if jogador1 == "pedra" and jogador2 == "tesoura":
        vitorias_user += 1
        print(f"Jogador1 ganhou, a Pedra vence a Tesoura")
    elif jogador1 == "papel" and jogador2 == "pedra":
        vitorias_user += 1
        print(f"Jogador1 ganhou, o Papel vence a Pedra")
    elif jogador1 == "tesoura" and jogador2 == "papel":
        vitorias_user += 1
        print(f"Jogador1 ganhou, a Tesoura vence o Papel")
    elif jogador1 == "pedra" and jogador2 == "papel":
        vitorias_computador += 1
        print(f"Jogador2 ganhou, o Papel vence a Pedra")
    elif jogador1 == "papel" and jogador2 == "tesoura":
        vitorias_computador += 1
        print(f"Jogador2 ganhou, a Tesoura vence o Papel")
    elif jogador1 == "tesoura" and jogador2 == "pedra":
        vitorias_computador += 1
        print(f"Jogador2 ganhou, a Pedra vence a Tesoura")
    elif jogador1 == jogador2:
        print(f"EMPATE!")
    else:
        print("Por favor tente de novo.")
        
print("""***BEM VINDO***

        P E D R A * P A P E L * T E S O U R A
          _________________________
         |       R e g r a s:      |
         |# Pedra ganha à Tesoura. |
         |# Tesoura ganha ao Papel.|
         |# Papel ganha à Pedra.   |
         |_________________________|
                                                    Criado por:
                                                    Jorge Moreira
 
_________***BOA SORTE***_________________________________________
""")


def user_vs_computer():
    while True:
        while True:
            print(f"Jogador1:{vitorias_user} vitórias.")
            print(f"Computador:{vitorias_computador} vitorias.")
            computador = jogada_ai()
            jogador1 = input("Escreva pedra, papel, tesoura ou quit para voltar ao menu.\n")
            if jogador1 == "pedra" or jogador1 == "papel" or jogador1 == "tesoura":
                break
            elif jogador1 == "quit":
                menu()
            else:
                print("Opção Inválida. \nDigite Novamente.")
                continue
    
        print("o Computador escolheu: " + computador)
        quem_ganha(computador, jogador1)
    
        print(" *****_____ Pretende jogar novamente? _____*****")
        repeticao = input("sim ou quit? \n")
        if repeticao == "sim":
            continue
        elif repeticao == "quit":
            menu()
        
def twoplayer_mode():
    while True:
        while True:
            print(f"Jogador1:{vitorias_user} vitórias.")
            print(f"Jogador2:{vitorias_computador} vitorias.")
            print("Jogador1 por favor escolha uma das opções: ")
            jogador1 = input("Escreva pedra, papel, tesoura ou quit para voltar ao menu.\n")
            if jogador1 == "pedra" or jogador1 == "papel" or jogador1 == "tesoura":
                print(f"Jogador1 escolheu {jogador1}.")
            elif jogador1 == "quit":
                menu()
            else:
                print("Opção Inválida. \nDigite Novamente.")
                continue
            
            print("Jogador2 por favor escolha uma das opções: ")
            jogador2 = input("Escreva pedra, papel, tesoura ou quit para voltar ao menu.\n")
            if jogador2 == "pedra" or jogador2 == "papel" or jogador2 == "tesoura":
                print(f"Jogador1 escolheu {jogador2}.")
                break
            elif jogador2 == "quit":
                menu()
            else:
                print("Opção Inválida. \nDigite Novamente.")
                continue
    
        print(f"O jogador1 escolheu {jogador1} e o jogador2 escolheu {jogador2}. \n Quem ganhará?")
        quem_ganha(jogador1, jogador2)
    
        print(" *****_____ Pretende jogar novamente? _____*****")
        repeticao = input("sim ou quit? \n")
        if repeticao == "sim":
            continue
        elif repeticao == "quit":
            menu()
        
def opcao():
    print('1 - Jogar contra AI')
    print('2 - Jogar 1vs1 Casual')
    print('3 - Sair do programa')
    
def menu():
    selecionar = 0

    while selecionar != 3:
        opcao()
        selecionar = int(input('>> '))
        if selecionar == 1:
            user_vs_computer()
            
        elif selecionar == 2:
            twoplayer_mode()
            
        elif selecionar == 3:
            print('Saindo do programa')
            sys.exit()
            
        else:
            print('Opção inválida.')
        

menu()