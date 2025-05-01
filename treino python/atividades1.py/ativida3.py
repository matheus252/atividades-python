# manipulando cadeias de texto
# frase = 'Curso em Video Python'
# FATIAMENTO
# print(frase[9]) * seleciona uma letra na chave 
# print(frase[9:13]) * seleciona a sequencia de letras dentro do cochetes
# print(frase[9:21:2]) * seleciona a sequencia pulando em casa em casa
# print(frase[:5]) * seleciona onde ele vai termina a seleção
# print(frase[15:]) * seleciona onde ele começa a seleção
# print(frase[9::3]) * seleciina a sequencia pulando de casa em casa

# analise
#print (len(frase)) * le quantas letras estão na string
#print(frase.count('o')) * pedindo para contar quantas letras tem na seleção
#print(frase.count('o',0,13)) * pedindo para contar e ja fatiando
#print(frase.find('deo')) * localiza onde começa a seleção que esta nos cochetes
#print(frase.find('android')) *localiz se a palavra esta na string se não estiver vai apontar como -1
#'curso' in frase * o operedor in vai dizer se existe a palavra selecionada
#print(frase.replace('python','android')) * substitui a palavra uma pela outra
#print(frase.upper()) * vai colocar as letras minuscula em maiscula
#print(frase.lowe()) * vai colocar as letras maiscula em minuscula
#print(frase.capitalize()) * vai jogar a strim toda em minuscula só as letras inicais maiuscula
#print(frase.title()) *onde estiver espaço ele vai colocar cada letra a pos espaço em maisculo
#print(frase.strip()) * remover os espaços que estão fora da strim
#print(frase.Rstrip()) * remover somente o ultimo espaço
#print(frase.Lstrip()) * remover somente o espaço a esquerda

#divisão

#frase.split() * onde estiver espaço ele vai divir as strim

#junção

#'-'.join(frase)* juntar todos os elementos da strim

# print("""frase""") * imprimi o texto todos completo

# frase= 'curso em video python'
# print()

#  exercicio 1
# nome = str(input('qual é seu nome: ')).strip()
# print('analisando seu nome...')
# a4 = nome.split()
# print(f'seu nome maisculo é {nome.upper()}')
# print(f'seu nome minusculo é {nome.lower()}')
# print(f'seu nome tem {len(nome) - nome.count(' ')} letras')
# print(f'seu primeio nome é {a4[0]} e ele tem {len(a4[0])}')

# exercico 2
# num = int(input('digite um numeoro: '))
# u = num // 1 % 10
# a = num // 10 % 10
# b = num // 100 % 10
# c = num // 1000 % 10 
# print(f'unidade: {u} \n dezena: {a} \n sentena: {b} \n milhar: {c}')

#exercicio 3
# cid = str(input('digite um nome de uma cidade: ')).strip().title()
# print(cid[0:5] == 'Santo' )

#exercicio 4
# nome = str(input('Qual seu nome: ')).strip().title()
# a= 'Silva' in nome
# print(f'Seu nome tem Silva: {a}')

#exercicio 5
# frase= str(input("Digite uma frase: ")).strip().lower()
# print(f'A letra A aparece {frase.count('a')} vezes na frase.')
# print(f'A letra A apareceu na posição {frase.find('a')+1}')
# print(f'A ultima letra A apareceu na posição {frase.rfind('a')+1}')

#exercicio 6
# nome = str(input('digite seu nome completo: ')).strip()
# a1 = nome.split()

# print(f'seu primeiro nome: {a1[0]}')
# print(f'sue ultimo nome: {a1[len(a1)-1]}')
