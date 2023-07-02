import random
tentativas = int(0)
escolha = int(0)
pc = random.randint(0, 10)
while escolha != pc:
    escolha = int(input('Tente adivinhar o número, de 0 a 10. '))
    tentativas += 1
print(f'Parabéns, você terminou o jogo! Você levou {tentativas} para terminá-lo.')