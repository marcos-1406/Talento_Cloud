while(1):
  A = float(input("Digite o Primeiro numero: "))
  B = float(input("Digite o Segundo numero: "))
  C = int(input("Digite a operação: "))

  if(C == 1):
    print(f"{A} + {B} = {A + B}")
  elif(C == 2):
    print(f"{A} - {B} = {A - B}")
  elif(C == 3):
    print(f"{A} + {B} = {A * B}")
  elif(C == 4):
    print(f"{A} + {B} = {A / B}")
  else:
    print("Retorno 0")