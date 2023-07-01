while True:
  print("\n" + ("=" * 30))
  print("[1] Soma")
  print("[2] Subtração")
  print("[3] Multiplicação")
  print("[4] Divisão")

  print("\nQual operação você quer fazer?")
  print("\n" + ("=" * 30))
  operacoes = ""
  while not operacoes.isnumeric():
    operacoes = input()
  operacoes = int(operacoes)
  if operacoes > 0 and operacoes < 5:
    n1 = ""
    while not n1.isnumeric():
      n1 = input("Digite o primeiro valor: ")
    n1 = float(n1)

    n2 = ""
    while not n2.isnumeric():
      n2 = input("Digite o segundo valor: ")
    n2 = float(n2)

    if operacoes == 1:
      print(f"{n1} + {n2} = {n1 + n2}")
    elif operacoes == 2:
      print(f"{n1} - {n2} = {n1 - n2}")
    elif operacoes == 3:
      print(f"{n1} * {n2} = {n1 * n2}")
    elif operacoes == 4:
      print(f"{n1} / {n2} = {n1 / n2}")
    else:
      print("Digite uma operação válida")