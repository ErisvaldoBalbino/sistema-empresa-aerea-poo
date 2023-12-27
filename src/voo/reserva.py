class Reserva:
    """Classe que representa uma reserva.
    Atributos:
        passageiro (Passageiro): passageiro que fez a reserva
        voo (Voo): voo da reserva"""
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