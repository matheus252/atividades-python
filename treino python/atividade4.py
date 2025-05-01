fila= []

while True:
    print('\n=== menu da fila ===')
    print('1. adicionar pessoa na fila')
    print('2. atender pessoa da fila')
    print('3. mostrar fila')
    print('4. sair')

    opcao = input('escolha uma opção:')
    if opcao == '1':
        nome = input('disgite o nome da pessoa: ')
        fila.append(nome)
        print(f'{nome} foi adicionado a fila.')
    elif opcao == '2':
        if fila:
            pessoa_atendida = fila.pop(0)
            print(f"{pessoa_atendida} foi atendida!")
        else:
            print('a fila esta vazia, ninguem para atender')

    elif opcao == '3':
        if fila:
            print('fila atual:' ,  fila)
        else:
            print(' a fila esa vazia')
    
    elif opcao == '4':
        print('saindo do programa...')
        break
    else:
        print('opção invalida , tente novamente.')



