# recursividade

#formula geral para o fatorial:
#fatorial(num)= 1 ,se num = 0 ou se num = 1 'caso base'
# fatorial (num) * fatorial(num 1), para num >1 'caso recursivo'
# 4! = 4 * fatoriaal(3) - 4 * 3 * fatorial(2) =4 * 3 * 2 * fatorial(1)=
# 4! = 4 * 3 * 2 * 1 = 24

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
    

