lista= []

while True:
    qunatidade_pessoa = int(input('quantas pessoas vai cadastrar: '))
    for i in range(qunatidade_pessoa):
        nome = input('qual os nomes para cadastrar: ')
        lista.append(nome)

        verificar_nome = input('digite um nome para verificar:')

    if lista == nome:
        print(f'{verificar_nome} liberado')
    else:
        (f'{verificar_nome} não se encaixa na lista')

