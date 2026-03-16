print('====== Exercício 002 - formas de print ======')

nome = input('Qual o seu nome? ')
print('Seu nome é',nome)

print('Prazer em te conhecer',nome)
print('Seja bem vindo ao mundo Python, {}!'.format(nome))
print()

print('====== Exercício 003 ======')
print('===== Soma entre dois números INTEIROS =====')
n1=int (input('Digite o primeiro numero: '))                # criando variável do tipo inteiro para receber dados do teclado
n2=int (input('Digite o segundo numero: '))
s=n1+n2                                                     # variável para receber a soma das variáveis

print('A soma entre ',n1,'+',n2, 'é igual:',s)              # formatação de uma string concatenada
