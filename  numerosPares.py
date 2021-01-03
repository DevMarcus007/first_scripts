#Lista os números para, de forma regressiva, a contar do numero digitado pelo usuário - Sem usar IF

print('Listagem de numeros PARES')
c=2
n=(int(input('\nDigite um número para ver todos os PARES de 1 até ele:\n')))
while c < n+1:
  print(f'{c}  ',end='')
  c +=2