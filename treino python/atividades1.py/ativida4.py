# condições simples e compostas
# if carro. esquerdo():
#   bloco true
# else:
#   bloco false
# tempo = int(input('quantos anos tem seu carro: '))
# if tempo <=3:
#   pront('carro novo')
# else: 
#   print('carro velho')
# print('--FIM--')
# 
# tempo = int(input('quantos anos tem seu carro: '))
# print('carro novo'if tempo <= else 'carro velho')
# print('--FIM--')
#
# nome = str(input('qual seu nome: '))
# if nome == 'gustavo':
#     print('que nome lindo você tem ')
# else:
#     print('seu nome é tão normal')
# print(f'bom dia {nome}')
# n1 = float(input('digite a primeira nota: '))
# n2 = float(input('digite a segunda nota: '))
# m = (n1 + n2)/2
# print(f'a sua média foi {m:.1f}')

# if m >= 6.0:
#     print('se sua média foi boa! PARABENS')
# else:
#     print('sua média foi ruim! ESTUDE MAIS')
#
# exercicio 1
# from random import randint
# from time import sleep
# compu = randint(0, 5)
# print('-=-=-=-'*10)
# print('vou pensar em um numero entre 0 e 5. Tente adivinhar...')
# print('-=-=-=-'*10)
# n1 = int(input('Em qual numero eu pensei: '))
# print('PROCESSANDO...')
# sleep(3)
# if n1 == compu:
#     print('parabens você conseguiu me vencer')
# else:
#     print(f'ganhei, eu pensei no numero {compu} não em {n1}')
#
# exercicio 2
# velocidade = float(input('Qual sua velocidade: '))
# multa = (velocidade - 80 ) * 7
# if velocidade >= 80:
#     print (f'você está em alta velocidade, você foi multado no valor de R${multa}')
# else:
#     print('parabens continue dirigindo com atenção')
# exercicio 3
#
# num = int(input('Me diga um número qualquer: '))
# result = num % 2
# if result == 0:
#     print('PAR')
# else:
#     print('IMPAR')
#
# exercicio 3

# distancia = float(input('Qual é a distancia da viagem: '))
# print(f'você vai começar a viagem de {distancia}Km')

# if distancia <= 200:
#     print(f'O valor da sua viagem é R${distancia * 0.50}')
# else:
#     print(f'O valor da sua viagem R${distancia * 0.45}')
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
# print(f'O valor da sua viagem vai ser R${preço}')

# exercicio 4 
# n1 = int(input('digite um numero:'))
# n2 = int(input('digite outro numero:'))
# n3 = int(input('digite ultimo numero:'))
# menor = n1
# if n2<n1 and n2<n3:
#     menor = n2
# if n3<n1 and n3<n2:
#     menor = n3
# print(f'O menor valor digitado foi {menor}')
# maior = n1
# if n2>n1 and n2>n3:
#     maior = n2
# if n3>n1 and n2>n3:
#     maior = n3
# print(f'O maior valor {maior}')

# exercicio 5


# salario = float(input('Qual seu salario: R$ '))

# if salario <= 1250:
#     valor = salario + (salario * 15/100)
#     print(f'Quem ganhava R${salario} seu salario R${valor}')
# else:
#     print(f'Quem ganhava R${salario} seu salario R${salario + (salario * 10/100)}')

# exercicio 6
# r1 = float(input('digite um segmento:'))
# r2 = float(input('digite mais um segmento:'))
# r3 = float(input('digite ultimo segmento:'))
# if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
#     print(' os segmentos acima PODEM FORMA  triangulo')
# else:
#     print('Os seguimentos acima não pode fecha rum trinagulo')
