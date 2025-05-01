# simples,  composto, encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input('digite a primeira nota :'))
n2 = float(input('digite a segunda nota:'))
 
# calcular a média aritmética das notas
media = (n1 + n2) /2 

if (media >= 7): 
    print("resultado: aprovado!")
    print("parabens")
elif (media  >= 5):
    print('você esta de recuperção')
else:
    print('aluno reprovado...')

print('sua media é {}' .format(media))

#if = simples= resultaod exato exemplo passou 
#elif = cadeado = para masis de dois tipo de resultado exemplo passou, não passou, recuperção 
#else = composto = doi tipos de resultados exemplo passou e não passou
