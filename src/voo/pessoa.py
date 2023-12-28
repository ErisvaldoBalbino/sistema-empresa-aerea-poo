class Pessoa:
    """Classe que representa uma pessoa.
    Atributos:
        nome (str): nome da pessoa
        cpf (str): CPF da pessoa
        telefone (str): telefone da pessoa
        
    Métodos:
        str: retorna uma string com os atributos da pessoa"""
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf
    
    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.__cpf}"

class Passageiro(Pessoa):
    """Classe que representa um passageiro. Herda de Pessoa.
    Atributos:
        nome (str): nome do passageiro
        cpf (str): CPF do passageiro
        telefone (str): telefone do passageiro
        reservas (list): lista de reservas do passageiro
        
    Métodos:
        get_reservas: retorna a lista de reservas do passageiro"""
    def __init__(self, nome, cpf, telefone, reservas = None):
        super().__init__(nome, cpf)
        self.telefone = telefone
        self.__reservas = reservas if reservas != None else []
    
    def get_reservas(self):
        return self.__reservas
    
class Tripulante(Pessoa):
    """Classe que representa um tripulante. Herda de Pessoa.
    Atributos:
        nome (str): nome do tripulante
        cpf (str): CPF do tripulante
        funcao (str): função do tripulante
        voo (Voo): voo associado ao tripulante
        
    Métodos:
        get_funcao: retorna a função do tripulante"""
    def __init__(self, nome, cpf, funcao, voo=None):
        super().__init__(nome, cpf)
        self.__funcao = funcao
        self.voo = voo
    
    def get_funcao(self):
        return self.__funcao
