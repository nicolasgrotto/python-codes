import random
from time import sleep

print('Seja muito bem-vindo ao meu jogo de Jokenpô.')
jogador = input('Escolha pedra, papel ou tesoura: ').strip().capitalize()
computador = random.choice(['Pedra', 'Papel', 'Tesoura'])
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')

if jogador == 'Pedra':
    if computador == 'Pedra':
        print(f'O jogador escolheu {jogador}\nO computador escolheu: Pedra')
        print('É um empate!')
    elif computador == 'Papel':
        print(f'O jogador escolheu {jogador}\nO computador escolheu: Papel')
        print('Você perdeu!')
    elif computador == 'Tesoura':
        print(f'O jogador escolheu {jogador}\nO computador escolheu: Tesoura')
        print('Você ganhou!')
elif jogador == 'Papel':
    if computador == 'Pedra':
        print(f'O jogador escolheu {jogador}\nO computador escolheu: Pedra')
        print('Você ganhou!')
    elif computador == 'Papel':
        print(f'O jogador escolheu {jogador}\nO computador escolheu: Papel')
        print('É um empate!')
    elif computador == 'Tesoura':
        print(f'O jogador escolheu {jogador}\nO computador escolheu: Tesoura')
        print('Você perdeu!')
elif jogador == 'Tesoura':
    if computador == 'Pedra':
        print(f'O jogador escolheu {jogador}\nO computador escolheu: Pedra')
        print('Você perdeu!')
    elif computador == 'Papel':
        print(f'O jogador escolheu {jogador}\nO computador escolheu: Papel')
        print('Você ganhou!')
    elif computador == 'Tesoura':
        print(f'O jogador escolheu {jogador}\nO computador escolheu: Tesoura')
        print('É um empate!')
else:
    print('Escolha inválida. Certifique-se de escrever "pedra", "papel" ou "tesoura" corretamente.')