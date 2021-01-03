#Verificação da média de 4 notas, e informação sobre Aprovação do aluno. Com retorno ao início
print('*'*28)
print('CURSO SISTEMAS DE INFORMAÇÃO')
print('*'*28)
m=0
while True:
    name = (input('Nome do Aluno: '))
    c = 1
    while c <=4:
            n=float(input(f'{c}ª Nota: '))
            m=m+n
            c+=1
    med=m/4
    print(f'\nA média do Aluno {name} foi: {med:.2f}')
    if med<=4:
        print(f'\nO Aluno {name} está REPROVADO!')
    elif med>4 and med<6:
        print(f'\nO Aluno {name} está EM RECUPERAÇÃO!')
    else:
        print(f'\nO Aluno {name} está APROVADO!')
    resp=int(input('\nMais algum Aluno? [1] SIM [2] NÃO - \n'))
    m=0
    if resp==2:
        break

print('\nFim do Programa')
    