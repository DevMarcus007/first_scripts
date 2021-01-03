#programa retorna a tabuada do número digitado pelo usuário

print('-'*11)
print('  Tabuada')
print('-'*11)
c=1
num=int(input('Digite o número para ver sua a tabuada: \n'))
while c <= 10:
  print(f'{c} x {num} = {c*num}')
  c+=1
print('\nFim do Programa')