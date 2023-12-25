class Pessoa:
    """Classe que representa uma pessoa.
    Atributos:
        nome (str): nome da pessoa
        cpf (str): CPF da pessoa
        idade (int): idade da pessoa
        telefone (str): telefone da pessoa
        
    Métodos:
        str: retorna uma string com os atributos da pessoa"""
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.__cpf = cpf
        self.telefone = telefone

    def get_cpf(self):
        return self.__cpf
    
    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.__cpf}\nIdade: {self.idade}\nTelefone: {self.telefone}"

class Passageiro(Pessoa):
    """Classe que representa um passageiro. Herda de Pessoa.
    Atributos:
        nome (str): nome do passageiro
        cpf (str): CPF do passageiro
        reservas (list): lista de reservas do passageiro
        
    Métodos:
        fazerReserva: faz uma reserva para o passageiro em um voo
        cancelarReserva: cancela uma reserva do passageiro em um voo
        visualizarReservas: retorna o número de reservas do passageiro"""
    def __init__(self, nome, cpf, telefone, reservas = None):
        super().__init__(nome, cpf, telefone)
        self.__reservas = reservas if reservas != None else []
    
    def get_reservas(self):
        return self.__reservas