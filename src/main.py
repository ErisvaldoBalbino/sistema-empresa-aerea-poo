from utilities.organizadorcsv import OrganizadorCSV
from ui.menufuncionario import MenuFuncionario
from ui.menupassageiro import MenuPassageiro
from voo.passageiro import Passageiro

def main():
    organizador = OrganizadorCSV()

    print("Bem-vindo ao Sistema de Gerenciamento Aereo!")
    
    while True:
        print("\nEscolha o tipo de usuário:")
        print("1. Funcionário")
        print("2. Passageiro")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menufuncionario = MenuFuncionario(organizador)
            menufuncionario.exibir_menu()
        elif escolha == '2':
            passageiros = organizador.carregarPassageiros()
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            passageiro_encontrado = next((passageiro for passageiro in passageiros if passageiro['cpf'] == cpf), None)
            if passageiro_encontrado:
                print(f"Bem-vindo {passageiro_encontrado['nome']}!")
                menupassageiro = MenuPassageiro(organizador, passageiro_encontrado['nome'], passageiro_encontrado['cpf'], passageiro_encontrado['telefone'])
            else:
                telefone = input("Digite seu telefone: ")
                passageiro = Passageiro(nome, cpf, telefone)
                organizador.salvarPassageiro(passageiro)
                menupassageiro = MenuPassageiro(organizador, nome, cpf, telefone)
            menupassageiro.exibir_menu()
        elif escolha == '3':
            print("Obrigado por utilizar o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
