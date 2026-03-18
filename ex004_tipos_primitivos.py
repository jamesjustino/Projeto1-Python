print('====== Desafio 004 - Tipo primitivo =====')

'''
04) Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
possíveis sobre ele.
'''
print('Digite números para saber seu Tipo primitivo')
n1 = int(input('Primeiro numero: '))                # variável do tipo inteiro
n2 = float(input('Segundo numero: '))               # variável do tipo float (ponto flutuante)
n3 = str(input('Terceiro numero: '))                # variável do tipo string (texto)
print()

print("Primeiro numero: {}".format(type(n1)))
print("Segundo numero: {}".format(type(n2)))
print("Terceiro numero: {}".format(type(n3)))
print()

n1 = input('Digite algo pelo teclado: ')
print('O que foi digitado é do tipo:',type(n1))     # comando para saber o seu tipo primitivo
print('Ele é um Alpha?:',n1.isalpha())
print('Ele é um Numero?:',n1.isnumeric())
print('Ele é um AlfaNumero?:',n1.isalnum())
print('Só tem espaços?:',n1.isspace())
print('Está em maiusculas?:',n1.isupper())
print('Está em minusculas?:',n1.islower())
print('Está capitalizada?:',n1.istitle())
print()
