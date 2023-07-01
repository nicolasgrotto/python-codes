
print(f'{"Caixa Eletrônico":^30}')
print('=' * 30)
valor = int(input('Qual o valor que você quer retirar? '))
total = valor
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total: {totalCedula} cédulas de R${cedula}.')
            totalCedula = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break
