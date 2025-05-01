from math import sqrt

class numeronegativoError(Exception):
    def __init__ (self):
        pass

if __name__=='__main__':
    try:
        num= int(input('digite um numero positovo:'))
        if num < 0 :
            raise numeronegativoError
    except numeronegativoError:
        print(f"foi forncecido um numero negativo")
    else:
        print(f' a raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print(f'\nfim do caluculo.')