quantidade_passos = int(input("digite um número:"))
if quantidade_passos > 0:
  for i in range(1, quantidade_passos+1, 1):
    if i == 1:
      print(f" Explorador: {i} passo")
    else:
      print(f" Explorador: {i} passos")
elif quantidade_passos == 0:
  print("Nenhum passo dado na floresta")
else: 
  print("Inválido")