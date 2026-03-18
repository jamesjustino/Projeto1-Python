print('======== Exercício 003 - Soma entre números inteiros =======')
print()

'''
03) Faça um programa que receba dois números inteiro e mostre na tela a soma entre eles. 
'''

print('===== Soma entre dois números INTEIROS =====')

n1=int (input('Digite o primeiro numero: '))                # criando variável do tipo inteiro para receber dados do teclado
n2=int (input('Digite o segundo numero: '))

s=n1+n2                                                     # variável para receber a soma das variáveis n1 + n2
print()

print('A soma entre',n1,'e',n2, 'é igual:',s)              # formatação de uma string concatenada

print('A soma entre {} e {} é igual: {}'.format(n1,n2,s))   # outra forma de formatar usando .format()
