class Veiculo:
    def movimentar(self):
        print(f'sou um veiculo e me desloco')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante 
        self.__modelo = modelo
        self.__num_registro = None

    #setter
    def set_num_resgistro(self, registro):
        self.__num_registro = registro

    # Getter 
    def fet_fabr_model(self):
        print(f'modelo: {self.__modelo}, fabricante {self.__fabricante}.\n')
    
    def get_num_registro(self):
        return self.__num__registro
    
class carro(Veiculo):
    # metodo __init__ sera herdado
    def movimentar(self):
        print(f'sou um carro e ando pelas ruas')

class motocilcleta(Veiculo):
    def movimentar(self):
        print(f'corro muito')

class aviao(Veiculo):
    def __init__(self, fabricante , modelo , categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)
    
    def get_categoria(self):
        return self.__cat
    
    def moveimentar(self):
        print(f'eu vou alto')


if __name__ == '__mais__':
    # meu_veiculo = Veiculo('GM', 'cadilac  ecalade')
    # meu_veiculo.movimentar()
    # meu_veiculo.get_fabr_modelo
    # meu_veiculo.get_num_registro(490321-1)
    # print(f'registro: {meu_veiculo.get_num_registro()}\n')

    # meu_carro = carro('Volkswagem', 'polo')
    # meu_carro.movimentar()
    # meu_carro.movimentar()

    # seu_carro = carro('audi', 'as sportback')
    # seu_carro.movimentar()
    # meu_carro.get_faber_modelo()

    # moto = motocilcleta("harley-davison", 'nightster speacial')
    # moto.movimentar():
    # moto.get_fabr_modelo()

    meu_aviao = aviao('boing', '747', 'comercial')
    meu_aviao.movimentar()
    meu_aviao.get__fabr_modelo()
    meu_aviao.get_categoria()
    print(f'categoria:{meu_aviao.get_categoria()}')

