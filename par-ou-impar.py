import random
vitorias = 0
print('Bem vindo ao meu jogo de par ou ímpar! ')
while True:
    escolha = int(input('Você quer par[1] ou ímpar[2]? '))
    jogador = int(input('Escolha um número de 1 a 5.'))
    if escolha == 1:
        computador = random.randint(1,5)
        print(f'Você escolheu par, e o número {jogador}.')
        print('O computador escolheu ', computador)
        if (jogador + computador) % 2 == 0:
            print(f'A soma dos números resultou em par({jogador + computador}), VOCÊ GANHOU!')
            vitorias += int(1)
        else:
            print(f'A soma dos números resultou em ímpar({jogador + computador}), Você perdeu!!')
            break
    elif escolha == 2:
        computador = random.randint(1, 5)
        print(f'Você escolheu ímpar, e o número {jogador}.')
        print('O computador escolheu ', computador)
        if (jogador + computador) % 2 != 0:
            print(f'A soma dos números resultou em ímpar({jogador + computador}), VOCÊ GANHOU!')
            vitorias += int(1)
        else:
            print(f'A soma dos números resultou em par({jogador + computador}), Você perdeu!!')
            break
print(f'Acabou o jogo, você ganhou {vitorias} vezes.')
