# Lista para armazenar os itens
itens = []

# Exibe a lista de itens
# declaração de uma variável i para não da erro
i = 0 
# para essa variável, ele exibe o contador, range que fará o processo 3 vezes
for i in range(3): 
  # ele pede para o usuário digitar o item
  item = input(f"digite o item {i+1}: ")
  #esse item é adicionado a uma lista que já foi previamente declarada 
  itens.append(item)
  #esse processo irá acontecer pois o mesmo está dentro do loop 
  #após o programa executar 3x o código termina 

#com base dos valores digitados e que estão armazenados na lista  
for item in itens: 
    print(f"-{itens}")
    # vai exibir cada valor item que foi armazenado 
