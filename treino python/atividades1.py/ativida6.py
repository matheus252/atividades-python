# laços de Repetição 
# laço C no intervalo(1,10)  for C in range(1,10):
#     passo                      passo
# pega                       passo
# 
# laço C no intervalo(0,3)   for C in range(0,3):
#     passo                      passo
#     pula                       pula
# passo                      passo
# pega                       pega
#
# laço C no intervalor(0,3)  for C in range(0,3):
#   se moeda                   if moeda
#         PEGA
#   passo
#   pula
# passo
# pega
#
# for i in range(7, 0 , -2):
#     print(i)
# print('FIM')

# n = int(input('digite um numero:'))
# for c in range(0 , n+1):
#     print(c)
# print('FIM')

# i = int(input('inicio: '))
# f= int(input('fim: '))
# p = int(input('passo: '))
# for c in range (i, f+1, p):
#     print(c)
# print('FIM')

# for c in range(0, 4):
#     n = int(input('digite um valor: '))
# print(f'o somatorio de todos os valores foi {n}')

# exercicio 1
# from time import sleep

# for i in range(10, -1, -1):
#     sleep(1)
#     print(i)
# print('estouro')

# exercicio 2

# for i in range (0,52,2):
#     print(i, end= ' ')
# print('FIM')

# exercicio 3
# soma = 0 
# cont = 0 
# for n in range(1, 501, 2 ):
#     if n % 3 == 0:
#          cont = cont + 1
#          soma = soma + n
# print(f'a soma de todos os {cont} valores são {soma}')                          

# exercicio 4
# num= int(input('Digite um numero para fazera tabuada : '))
# for n in range (0, 11):
#     print(f'{n}  x  {num} = {num *n:2}')
    
# exercicio 5
# soma = 0 
# cont = 0
# for n in range (1, 7):
#     num= int(input('digite um numero: '))
#     if num % 2 == 0: 
#         soma += num
#         cont += 1
# print(f'Você informou {cont} a soma dos numero pares são: {soma}')

# soma= 0 
# cont= 0
# for i in range (6):
#     num= int(input('digite um numero: '))
#     if num % 2 == 1:
#         soma += num
#         cont += 1
# print(f'avocê informou {cont} a soma desses numeros são: {soma}')

# exercicio 6 
# print('='*12)
# print('10 TERMOS DE UMA PA')
# print('='*12)
# termo = int(input('Primeiro termo: '))
# razão = int (input('razão: '))
# decimo = termo + (11 - 1)* razão

# for i in range (termo, decimo , razão):
#     print(i ,end='.')
# print('ACABOU')

# exercicio 7
# num = int(input('digite um numer: '))
# tot = 0
# for c in range (1 , num, +1):
#     if num % c == 0:
#         print(c,end= ' ')
#         tot += 1 
# print(f'o numero {num} foi divisivel por {tot} vezes')
# if num % 2:
#     print(f'o {num} é um numero PRIMO')
# else:
#     print(f'o {num} não é um numero PRIMO')

# exercicio 8

# frase = str(input('digite um frase: ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range (len(junto) -1 , -1 , -1):
#     inverso += junto[letra]
# print(f'o inverso do {junto} , {inverso}')
# if inverso == junto:
#     print(' temos um pçalindromo')
# else:
#     print('a frase digitanda não é um palindromo')

#exercicio 9
# from datetime import date
# atual = date
# totmaior = 0 
# totmenor = 0
# for pess in range (1, 8 ):
#     nasc = int(input('em que ano a pessoa nasceu: '))
#     idade = atual - nasc
# if idade >= 21:
#     totmaior += 1
# else:
#     totmenor += 1
# print(f'ao todo tivemos {totmaior} pessoas maior de idade')
# print(f'ao todo tivemos {totmenor} pessoas menor de idade')

#exercicio 10
# pesomaior = 0
# pesomenor = 0
# for i in range(1, 6):
#     peso = float(input(f'Digite peso da {i} pessoa: '))
#     if i == 1:
#         pesomaior= i 
#         pesomenor= i
#     else:
#         if peso > pesomaior:
#             pesomaior = peso
#         if peso < pesomenor:
#             pesomenor = peso
# print(f'peso maior {pesomaior}Kg')
# print(f'peso menor {pesomenor}Kg')

#exercicio 11 
# soma = 0
# maisvelho = 0 
# nomevelho = ''
# tot20m= 20
# for i in range (1,5):
#     print(f'---PESSOA {i}---')
#     nome= str(input('Qual seu nome: ')).strip
#     idade= int(input('Qual sua idade: '))
#     sexo = str(input('Qual seu sexo F/M: ')).upper().strip()
#     soma += idade
#     if i == 1 and sexo in 'Mm':
#         maisvelho = idade
#         nomevelho = nome
#     if sexo in 'Mm' and idade > maisvelho:
#         maisvelho = idade
#         nomevelho = nome
#     if sexo in 'Ff' and idade <20:
#         tot20m += 1
# print(f'A média de idade das pessoa {soma /4 :.2f}')
# print(f'O homem mais velho tem {maisvelho} e se chama {nomevelho}')
# print(f'Ao todo são {tot20m} mulheres com menos de 20 anos')