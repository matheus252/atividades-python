# lista: representa um sequencia de valores

# sintaxe: nome_lisata = [valores]

n1 = [5,6,7,9,0,]
n2 = [1,2,3,4]
valores = n1 + n2
# valores [0] = 9
# print(len(valores))
# print(sorted(valores, reverse= True))
# print(sum(valores))
# print(min(valores))
# print(max(valores))

# valores.append(13)
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(3,21)
# print(valores)
# print(13 in valores)

bebidas = []

for i in range(5):
    print(f'digite uma bebida favorita: ')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'\nbebida escolhidas:')
for bebida in bebidas:
    print(bebida)

print(f'\nsaude!')











