# escopo global e local 

var_global = "curso complato de python"

def escreve_texto():
    global var_global
    var_global = 'banco de dados com SQL'
    var_local=" matheus silva"
    print(f'variavel global: {var_global}')
    print(f'variavel loca: {var_local}')

if __name__=='__main__':
    print(f'executar a função ecreve _texto()')
    escreve_texto()

    print('tentar acessar as variaveis diretamente')
    print(f'variavel global: {var_global}')


    