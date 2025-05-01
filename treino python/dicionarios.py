 # dicioairos

elemento = {
    'z': 3,
    'nome': 'Lítio',
     'grupo': 'metais alcalinos',
     'densidade': 0.534
}
print(f'elemento:  {elemento['nome']}')
print(f'densidade:  {elemento['densidade']}')
print(f'odicionario possui {len(elemento)} elementos')

#atualizar uma entrada

elemento['grupo']= 'alacalinos'
print(elemento)

#adicionar um entrada
elemento ['periodo'] = 1
print(elemento)

#exlusão de itens em dicionarios

# del elemento['periodo']
# print(elemento)

# elemento.clear()
# print(elemento)

print(elemento.items())
for i in elemento.items():
    print(i)


print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f'{i} : {j}')

