import random

print("Bem-vindo ao pedra, papel e tesoura!")
jogando = True
while jogando:
    escolhas = ['Pedra', 'Papel', 'Tesoura']
    escolha_jogador = input("Faça sua escolha: Use 'Sair' para encerrar. \n")
    if escolha_jogador.capitalize() == 'Sair':
        print("Até a próxima!")
        jogando = False
        break
    
    if escolha_jogador.capitalize() not in escolhas and escolha_jogador.capitalize() != 'Sair':
        print("Opção inválida. Tente novamente.")
    
    escolha_computador = random.choice(escolhas)
    print(f"O computador escolheu {escolha_computador}.")
    if escolha_jogador.capitalize() == escolha_computador:
        print("Empate!")
    elif(escolha_jogador.capitalize() == 'Pedra' and escolha_computador == 'Tesoura') or \
        (escolha_jogador.capitalize() == 'Papel' and escolha_computador == 'Pedra') or \
        (escolha_jogador.capitalize() == 'Tesoura' and escolha_computador == 'Papel'):
        print("Você venceu!")
    else:
        print("Que pena... Você perdeu.")