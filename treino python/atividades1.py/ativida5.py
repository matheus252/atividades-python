# condições aninhadas
# siga = if
# senão = elif
# pare = else
#
# nome = str(input('qual é o seu nome: '))
# if nome == 'gustavo':
#    print('que nome bonito')
# elif nome == 'pedro' or nome == 'matheus' or nome == 'paulo':
#    print('seu nome é bem popular no Brasil')
# elif nome in 'ana claudia jessica juliana':
#    print('seu nome feminino é bem bonito ')
# else
#      print('seu nome é bem normal')
# print('tenha um bom dia')
#
# exercicio 1
# valor = float(input('Valor da casa: R$'))
# salario = float(input('qual seu salario: R$'))
# anos = float(input('quantos anos de financiamento: '))

# r1 = valor / (anos * 12)
# minimo = salario * 30 / 100
# print(f'para pagar uma casa de {valor:.2f} em {anos} anos \n a prestação será de R${r1:.2f} ')
# if r1 <= minimo:
#     print('o financiamneto pode ser concedido')
# else:
#     print('financiamento negado')

# print(f'comparando tem que paga {r1} e o minimo é de  {minimo} ')

# exercicio 2
# num = int(input('digite um numero inteiro:'))

# print('Escolha um numero na opção abaixo: \n[1] para binario \n[2] para octal \n[3] para hexadecimal ')
# opcão = int(input('sua opção foi: '))

# if opcão == 1:
#     print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
# elif opcão == 2:
#     print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
# elif opcão == 3:
#     print(f'{num} convertido pata HEXADECIMAL é igual a {hex(num)[2:]}')
# else:
#     print('não temos essa opção, tente novamente')

# exercio 3
# num = int(input('digite um numero:'))
# num2 = int(input('digite outro numero: '))

# if num > num2:
#     print('primeiro numero é MAIOR')
# elif num2 > num:
#     print('O seguno numero é MAIOR')
# else:
#     print('não exite valor maior, os dois são iguais')

# exercicio 4
# from datetime import date
# ano = date.today().year
# nascimento = int(input('qual ano você nasceu: '))

# result = ano - nascimento
# print(f'você nasceu {nascimento} e tem {result} anos ')
# if result == 18:
#     print(f'ja esta na hora de você se alistar')
# elif result > 18:
#     dados= result - 18
#     print(f'ja era para voce se alista a {dados} anos atrás')
#     anos= ano - dados
#     print(f'era para você se alistar no {anos}')
# elif result < 18:
#     dados = 18 - result
#     print(f'você não precisa se alistar ainda, falta {dados} anos')
#     anos= ano + dados
#     print(f'você vai se alistar no {anos}')

# exercicio 5

# nota1 = float(input('primeria nota:'))
# nota2 = float(input('segunda nota:'))
# result = (nota1 + nota2) / 2
# print(f'tirando {nota1} e {nota2} a média do aluno é {result}')
# if result > 7:
#     print('você esta APROVADO')
# elif result > 5 < 6.9:
#     print('você esta de RECUPERAÇÃO')
# else:
#     print('você REPROVADO')

# exercicio 6 
# from datetime import date
# ano = date.today().year
# nascimento = int(input('qual ano você nasceu: '))
# idade = ano - nascimento

# if idade <= 9:
#     print(f'atleta MIRIM com {idade} anos')
# elif idade <= 14:
#     print(f'atleta INFANTIL com {idade} anos')
# elif idade <= 19:
#     print(f'atleta JUNIOR com {idade} anos')
# elif idade <= 25:
#     print(f'atleta SÊNIOR com {idade} anos')
# else:
#     print(f'atleta MASTER com {idade} anos')

# exercicio 7
# seg1 = int(input('digite um segmento: '))
# seg2 = int(input('digite outro segmento: '))
# seg3 = int(input('digite o ultimo segmento: '))

# if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
#     print('os segmentos acima PODEM FORMAR um triângulo',end='')
#     if seg1 == seg2 == seg3:
#         print('EQUILATERO')
#     elif seg1 != seg2 != seg3 != seg1:
#         print('ESCALENO')
#     else:
#         print('ISÓSCELES')
# else:
#     print('Os segmentos acima NÃO PODE FORMA UM TRINGULO')

# exercicio 8
# kg = float(input('qual seu peso: Kg'))
# altura = float(input('qual sua altura:'))
# imc = kg / (altura * altura)
# print(f'seu imc è {imc:.2f}')
# if imc <= 18.5:
#     print('abaixo do peso')
# elif imc <= 25:
#     print('peso ideal')
# elif imc <= 30:
#     print('esta com sobrepeso')
# elif imc <= 40:
#     print(' obesidade')
# else:
#     print('obesidade morbida')

#exercicio 9 
# print('====== IPER LOJA ======')
# produto = float(input('qual o valor do produto: R$ '))
# print('FORMAS DE PAGAMENTO')
# print('''
# [1] á vista dinheiro/cheque
# [2] á vista no cartão
# [3] em até 2x no cartão
# [4] 3x ou mais no cartão ''')
# formas = int(input('qual a forma de pagamento: '))
# if formas == 1:
#     desconto = produto - (produto * 10/100)
#     print(f'o valor que o senhor ia pagar é de R${produto:.2f}\nmas no a vista fica R${desconto:.2f}')
# elif formas == 2 :
#        desconto1= produto - (produto * 5/100)
#        print(f'o valor que o senhor ia pagar é de r${produto:.2f}\nmas o o avista no cartão fica R${desconto1:.2f}')
# elif formas == 3:
#     parcela = produto / 2
#     print(f'parcelando no cartão em 2x o valor vai ficar R${parcela:.2f}\nsua compra mantem no R${produto:.2f}')
# elif formas == 4:
#      juros= produto + (produto * 20/100)
#      totalpac = int(input('quantas parcelas: '))
#      parcela = juros / totalpac
#      print(f'sua compra vai parcelada em {totalpac}x de R${parcela:.2f} JUROS')
#      print(f'sua compra de R${produto:.2f} vai ficar R${juros:.2f}')
# else:
#     total = 0
#     print('OPÇÃO IVALIDA de pagamento, tente novamente')

# exercicio 10
# from random import randint
# from time import sleep
# itens = ('pedra','papel','tesoura')
# comput = randint(0 , 2)
# print(''' suas opções
# [1] pedra
# [2] papel
# [3] tesoura''')
# joga= int(input('qual sua jogada: '))

# print('JO')
# sleep(1)
# print('KEN')
# sleep(1)
# print('PO!!!')
# sleep(1)
# print('-='*11)

# print(f'computador jogou {itens[comput]}')
# print(f'jogador jogou {itens[joga]}')
# print('-='*11)
# if comput == 0:
#     if joga == 0:
#         print(' vai ser considerado EMPATE')
#     elif joga == 1:
#         print(' vai ser considerado JOGADOR GANHOU')
#     elif joga == 2:
#         print(' vai ser considerado COMPUTADOR GANHOU')
#     else:
#         print('jogada invalida, tente novamente')
# elif comput == 1:
#     if joga == 0:
#         print('vai ser considerado COMPUTADOR GANHOU')
#     elif joga == 1:
#         print('vai ser considerado EMPATE')
#     elif joga == 2:
#         print('vai ser considerado JOGADOR GANHOU')
#     else:
#         print('jogada invaida, tente novamente')
# elif comput == 2:
#     if joga == 0:
#         print('vai ser considerado que JOGADOR GANHOU')
#     elif joga == 1:
#         print('vai ser considerado COMPUTADOR GANHOU')
#     elif joga == 2:
#         print('vai ser considerado EMPATE')
#     else:
#         ('jogada invalida, tente novamente')

# num = int(input('digite um numero: '))
# num1 = int(input(' digite um numero: '))
# soma = num + num1
# print(f'{soma}')

