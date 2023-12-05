def Apresentacao(Nome, Ano):
  print("Olá, " + Nome + "!! Você completará ou completou " + str(2023 - Ano) + " anos em 2023")

print("Insira teu nome completo: ")
Nome = str(input())
print("Insira teu ano de nascimento entre 1922 e 1921: ")
Execute = True
while(Execute):
  try:
    Ano = int(input())
    if(Ano >= 1922 and Ano <= 2021):
      Execute = False
    else:
      print("Digite um ano válido entre 1922 e 2021")
  except:
    print("Você não digitou numero válido como ano")
Apresentacao(Nome, Ano)
