# palavras = ['python','é','uma','linguagem','de','programação']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

# função filter()
#sintaxe:
#filte(função, sequencia)

# def numeros_pares(n):
#     return n % 2 ==0

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_par = list(filter(numeros_pares, numeros))

# print(num_par)

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# num_impar = list(filter(lambda x: x % 2 != 0, numeros))
# print(num_impar)

# funções reduce()
# sintaxe:
# reduce(função, seuqencia, valor_inicial)

from functools import reduce

# def mult(x , y):
#     return x * y 
# numero = [1,2,3,4,5,6]

# total = reduce(mult, numero)
# print(total)

# soma cumulativa dos quadrados de valores, usando expressão lambda

numeros = [ 1,2,3,4]
# (1)

total = reduce(lambda x, y :x**2 + y**2, numeros)
print(total)

