def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)
    
if __name__ == '__name__':
    x = int(input('digite um numero inteiro positivo para calular seu fatorial'))
    try:
        res = (fatorial(x))
    except RecursionError:
        print(f'o nomero fornecido é muito grande ou nagtivo')
    else:
        print(f'o fatorial de  {x} é {res}')
    print(f'o fatorial de {x} è {res}')
    


