#Programa que gera aleatoriamente 7 números para jogo de bolão na Mega Sena

from random import randint
from time import sleep
print("*"*50)
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*6,"GERADOR DE NÚMEROS - MEGA SENA"," "*8,"*")
print("*"," "*13,"JOGO DE 7 NÚMEROS"," "*14,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"*50)

a=input('\nTecle enter para iniciar')
print('\n\n\nPsicografando>.>.>.\n\n\n')
sleep(1)

jogo1=[]


i=7
while len(jogo1) < i:
	n=int(randint(1,60))
	if n not in jogo1:
		jogo1.append(n)
		n=0
jogo1.sort()

sleep(0.5)
print('Primeiro jogo:',jogo1)
sleep(0.5)

print('\n\nBoa sorte')


