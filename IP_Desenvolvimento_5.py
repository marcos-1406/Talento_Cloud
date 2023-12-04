def Calculador(Num1, Num2, Op):
  if(Op == 1):
    print(f"{Num1} + {Num2} = {Num1 + Num2}")
  elif(Op == 2):
    print(f"{Num1} - {Num2} = {Num1 - Num2}")
  elif(Op == 3):
    print(f"{Num1} * {Num2} = {Num1 * Num2}")
  elif(Op == 4):
    print(f"{Num1} / {Num2} = {Num1 / Num2}")

Exec = True
while(Exec):
  print("Códigos para Operação:\n1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair")
  Op = int(input("Digite o código da operação: "))
  if(Op == 0):
    Exec = False
  elif(Op < 0  or Op > 4):
    Op = int(input("Digite Novamente "))
  else:
    Num1 = float(input("Digite o primeiro numero: "))
    Num2 = float(input("Digite o segundo numero: "))
    Calculador(Num1, Num2, Op)