# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão inteira
# % divisão inteio
# ordem de precedência
#1 ()
#2 **
#3 *, /,//,%
#4 + , -

#pratica

# n1 = int(input('um valor: '))
# n2 = int(input('de outro valor: '))
# s = n1 + n1
# m = n1 * n2
# d = n1 / n2
# di = n1 //  n2
# e = n1 ** n2
# print(f'soma é :{s}, o produto é {m} e a divisão é {d}')
# print(f'divisão inteira {di} e pontencia {e}')

#primeiro exercicio
# n = int(input('digite um numeor: '))
# print(f' o dobro de {n} é {n * 2}')
# print(f' o triplo de {n} é {n * 3}')
# print(f' a raiz quadrada de {n} é {n**(1/2):.2f}')

#segundo exercicio
# n1= float(input('digite a nota do aluno: '))
# n2= float(input('outra a nota: '))
# print(f'a média é {n1:.1f} e {n2:.1f} é igual {(n1+n2)/2:.2f}')

#terceiro exercicio
# d = float(input('qual a distancia: '))
# cm = d * 100
# mm = d * 1000
# print(f'a medida de {d} correposnde a \n{cm}cm e \n{mm}mm')
# print(f'{d*10}dm \n{d*-10}dam \n{d*-100}hm \n{d*-1000}km')

#quarto exercicio
# n = int(input('digite o numero para ver a tabuada: '))
# print('-'*13)
# print(f' 1 x {n*1:2} \n 2 x {n*2:2} \n 3 x {n*3:2} \n 4 x {n*4:2} \n 5 x {n*5:2} \n 6 x {n*6:2} \n 7 x {n*7:2} \n 8 x {n*8:2} \n 9 x {n*9:2} \n 10 x {n*10:2}')
# print('-'*13)

#quinto exercicio
# carteira = float(input('quanto você tem na carteira R$: '))
# r= carteira / 5.75
# print(f'com R${carteira} voce pode comprar US${r:.2f}')

#sexto  exercicio
# largura= float(input('qual a largura da parede: '))
# altura = float(input('qual a altura da parede: '))
# r = largura * altura
# r1 = r / 2
# print(f'sua parede tem a dimensão de {largura} x {altura} e sua areá é de {r}m2.')
# print(f'para pinta essa parede, você precisá de {r1}L de tinta')

#sétimo exercicio
# valor = float(input('qual é o preço do produto: R$ '))
# promo= valor - (valor * 5 /100)

# print(f' O  produto que custava R${valor} com o desconto fica R${promo}')

# oitavo exercicio

# salario = float(input('Qual o salario do Funicionario: R$'))
# reajuste = salario + (salario * 15/100)
# print(f'Um funcionario que ganhava R${salario:.2f}, 15% de aumento, passa a receber R${reajuste:.2f}')

# produto = float(input('digite o preço do produto: R$'))
# desconto = produto - (produto * 5/100)
# parcelado = produto + (produto * 2/100)
# print(f'O produto custa R${produto:.2f},  se você paga avista ele vai ter um desconto e fica R${desconto:.2f}, se voce parcela vai ter um acrecimo de R${parcelado:.2f}')

# temperatura = float(input('informe a temperatura Cº: '))
# faren = (temperatura * 9/5) + 32
# print(f'temperatura em celsius é Cº{temperatura} e a temperatura de fahrenheits Fº{faren}.')

# km = float(input('quantos km foi percorrido: '))
# dia = int(input('quantos dias foi percorrido: '))
# r1 = 0.15 * km
# r2 = 60 * dia
# print(f'o valor a pagar pelo carroe é de R${r1 + r2:.2f}.')