#Calcula a quantidade de dias de vida a menos o fumante já acumula

print("|-----------------------------------|")
print("| EXPECTATIVA DE DIMINUIÇÃO DE VIDA |")
print("|-----------------------------------|")
name=input("\nInforme seu nome: ")
age=int(input("\nInforme sua idade: "))
time=int(input("\nÉ fumante há quanto tempo (em anos):  "))
qtd=int(input("\nFuma quantos cigarros por dia: "))
print("\nCalculando...")
totcig = (time*365)*qtd
timelife = float((totcig*10)/1440)
print(f'\n{name}, este é seu diagnóstico:')
print(f'\nVocê ja fumou {totcig} cigarros até hoje...')
print(f'\nE por conta disso já perdeu {timelife:.2f} dias de vida.\n\n')
print("          |--------|")
print("          | R.I.P. |")
print("          |--------|")