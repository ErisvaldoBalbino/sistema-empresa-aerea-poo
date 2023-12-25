class Reserva:
    """Classe que representa uma reserva.
    Atributos:
        passageiro (Passageiro): passageiro que fez a reserva
        voo (Voo): voo da reserva
        id (uuid): id da reserva, deve ser gerado automaticamente com a função uuid.uuid4() da biblioteca uuid"""
    def __init__(self, passageiro, voo, id = None):
        self.__passageiro = passageiro
        self.__voo = voo

    def get_passageiro(self):
        return self.__passageiro
    
    def get_voo(self):
        return self.__voo.get_codigoVoo()