print('====== Exercício 002 - formas de print ======')

'''
02) Faça um programa para receber um nome e mostre o nome na tela e algumas mensagens para o usuário.
'''

nome = input('Qual o seu nome? ')       # variável recebe informação do teclado
print()

print('Seu nome é',nome)                # imprimindo a informação da variável
print('Prazer em te conhecer',nome)     # forma de imprimir uma variável usando a vírgula
print('Seja bem vindo ao mundo Python, {}!'.format(nome))   # outra forma de imprimir uma informação usando .format()
