import random

# print('print gerar nmero aleatorio entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'numero grande: {n}'

# valor = random.random()
# print(f'numero gerado: {round(valor * 10, 2)}')


# valor= random.uniform(1,10)
# print(f'numeor: {round(valor, 4)}')

l = [2,4,6,9,10,53,25,67,85,8,7,90]
# n = random.choice(l)
# print(f'numero escolhido: {n}')

# n = random.sample(l,3)
# print(f'numero esolhidos:{n}')

#embaralhar
print(f'exibir a lista original: {l}')
print(f'embaralhar a lista e exibi-la:')
n = random.shuffle(l)
print(l)




