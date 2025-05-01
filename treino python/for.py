# lista = [2,6,9,3,5,7,7,8,2,]
# palavra = 'boson'
# for letra in palavra:
#     print(letra)

# nome = input('digite seu nome:')
# for x in range (10):
#     print(f'{x+1} {nome}')

# range( valor_inicial, valor_ valor inicial, incremento)

# for x in range(20,1,-2):
#     print(x)

pedras = ('rubi','esmeralda','quartzo','safir','diamante','turmalina')

for pedra in  pedras:
    if pedra == 'quartzo':
        continue
    print(pedra)
