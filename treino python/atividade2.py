# pedir o nome do aluno
nome = input('Qual o nome do aluno: ')

#pedir as 3 notas
nota1 = float(input('Qual nota 1: '))
nota2 = float(input('qual nota 2: '))
nota3 = float(input('qual nota 3: '))

#calcular a média
media = (nota1 + nota2 + nota3) /3

#mostrar a média com 2 casa decimais 
print(f"ola, {nome}! sua média è {media:.2f}")

#verificar se passou

if media == 10:
    print('você passou com excelecnia!')
elif media >= 7:
    print("parabens você passou ")
else:
    print("que pena, voçê reprouvou")
    
          
       
    