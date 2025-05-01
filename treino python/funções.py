# Funções
# Modularização, Reuso de código, Ligibilidade

# def mensagem():
#     print('boson treinamentos e tecnilogia')
#     print('curso completo de pyth')

# mensagem()

# função com argumento
# def mult(x, y):
#     return x * y


# a = 5
# b = 8
# c = mult (a, b)

# print(f'o produto de {a} e {b} é {c}')

# def quadrado (val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados

# def contar(caracter, num=11)
#           for i in range(num=11):
#                print(caractere)



x= 5 
y= 6
z= 3

def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c

if __name__ =='__main__':
    res = soma_mult (x, y, z)
    print(res)
    