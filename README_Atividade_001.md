# Explorador de Passos

Este projeto é o meu primeiro desafio do bootcamp Python Analytics da plataforma Dio. O objetivo é criar um programa simples em Python que solicita ao usuário um número e imprime a quantidade correspondente de passos que um explorador deu na floresta. O programa também lida com entradas inválidas e diferentes condições de pluralidade.

## Descrição do Código

O código solicita ao usuário que insira um número inteiro que representa a quantidade de passos que um explorador deu. Dependendo do valor inserido, o programa imprime uma mensagem diferente:

- Se o número for maior que 0, o programa imprime cada passo individualmente, usando "passo" no singular para 1 e "passos" no plural para valores maiores que 1.
- Se o número for 0, o programa imprime "Nenhum passo dado na floresta".
- Se o número for negativo, o programa imprime "Inválido".

## Como Funciona

Aqui está o código:

```python
quantidade_passos = int(input("digite um número:"))
if quantidade_passos > 0:
  for i in range(1, quantidade_passos+1, 1):
    if i == 1:
      print(f"Explorador: {i} passo")
    else:
      print(f"Explorador: {i} passos")
elif quantidade_passos == 0:
  print("Nenhum passo dado na floresta")
else: 
  print("Inválido")
```

## Entradas e Saídas
- Entrada: Um número inteiro inserido pelo usuário.
- Saída: Mensagens indicativas do número de passos dados pelo explorador, considerando a pluralidade.

## Exemplo de Uso
---
Se o usuário digitar 5, a saída será:

Explorador: 1 passo
Explorador: 2 passos
Explorador: 3 passos
Explorador: 4 passos
Explorador: 5 passos
---
Se o usuário digitar 0, a saída será:

Nenhum passo dado na floresta
---
Se o usuário digitar um número negativo, a saída será:

Inválido
---

## Licença
Este projeto não possui uma licença específica. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.

## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, por favor, envie um pull request.
