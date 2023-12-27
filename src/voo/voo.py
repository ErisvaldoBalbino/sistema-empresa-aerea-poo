class Voo:
    """Classe que representa um voo.
    Atributos:
        codigoVoo (str): código do voo
        tipoVoo (str): tipo do voo (nacional ou internacional)
        data (datetime): data do voo
        partida (Aeroporto): aeroporto de partida
        destino (Aeroporto): aeroporto de destino
        aviao (Aviao): avião do voo
        assentosTotais (int): número de assentos totais do voo
        reservas (list): lista de reservas do voo
        tripulacao (list): lista de tripulantes do voo
        
    Métodos:
        assentosLivres: retorna o número de assentos livres do voo
        str: retorna uma string com os atributos do voo
        
    Quando for instanciada, é recomendado que seus parametros sejam instancias das outras classes."""
    def __init__(self, codigoVoo, tipoVoo, data, partida, destino, aviao, assentosTotais, tripulacao = None, reservas = None):
        self.__codigoVoo = codigoVoo
        self.__tipoVoo = tipoVoo
        self.__data = data
        self.__partida = partida
        self.__destino = destino
        self.__aviao = aviao
        self.__assentosTotais = assentosTotais
        self.reservas = reservas if reservas != None else []
        self.__tripulacao = tripulacao if tripulacao != None else []

    def assentosLivres(self):
        return self.__assentosTotais - len(self.reservas)
    
    def get_aviao(self):
        return self.__aviao
    
    def get_assentos(self):
        return self.__assentosTotais
    
    def get_codigoVoo(self):
        return self.__codigoVoo
    
    def get_voo(self):
        return self.get_voo
    
    def get_tripulacao(self):
        return self.__tripulacao
    
    def get_tipoVoo(self):
        return self.__tipoVoo
    
    def get_data(self):
        return self.__data
    
    def get_partida(self):
        return self.__partida

    def get_destino(self):
        return self.__destino

    def __str__(self):
        return f"Voo: {self.__codigoVoo}\nTipo: {self.__tipoVoo}\nData: {self.__data}\nPartida: {self.__partida}\nDestino: {self.__destino}\nAvião: {self.__aviao}\nAssentos Totais: {self.__assentosTotais}\nAssentos Livres: {self.assentosLivres()}"        