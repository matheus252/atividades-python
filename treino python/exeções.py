# exceção é um objeto que representa um erro ocorreu ao executar o programa.
# blocos try ... except

def div(k, j ):
    return round(k / j, 2)

if __name__=='__main__':
    while True:
        try:
            n1 = int(input('digite um numero: '))
            n2 = int(input('digite um numero: '))
            break
        except ValueError:
            print(f'ocorreu um erro ao ler o valor . tente novamente.')

    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'não é possivel dividir por zero!')
    except:
        print(f'ocorreu um erro deconhecido...')
    else:
        print(f'resultado: {r}')        
    finally:
        print(f'\nFim do calculo')