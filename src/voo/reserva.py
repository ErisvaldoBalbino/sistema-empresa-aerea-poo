class Reserva:
    """Classe que representa uma reserva.
    Atributos:
        passageiro (Passageiro): passageiro que fez a reserva
        voo (Voo): voo da reserva
        assento (int): assento da reserva
    
    Métodos:
        get_passageiro: retorna o passageiro da reserva
        get_voo: retorna o voo da reserva
        get_assento: retorna o assento da reserva"""
    def __init__(self, passageiro, voo, assento):
        self.__passageiro = passageiro
        self.__voo = voo
        self.__assento = assento

    def get_passageiro(self):
        return self.__passageiro
    
    def get_voo(self):
        return self.__voo.get_codigoVoo()
    
    def get_assento(self):
        return self.__assento