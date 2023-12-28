# Sistema de Gerenciamento Aereo
Um sistema simples que simula uma empresa aerea, e possui os pilares de POO (Programação Orientada a Objetos).

## Estrutura do repositório:

1. **Classes principais:**
    - [voo.py](https://github.com/ErisvaldoJ/sistema-empresa-aerea-poo/blob/main/src/voo/voo.py): A base do sistema, representa um voo.
    - [reserva.py](https://github.com/ErisvaldoJ/sistema-empresa-aerea-poo/blob/main/src/voo/reserva.py): Possui as definições para a reserva.
    - [pessoa.py](https://github.com/ErisvaldoJ/sistema-empresa-aerea-poo/blob/main/src/voo/pessoa.py): Define a classe Pessoa, que serve de base para Passageiro e Tripulante.
  
2. **Manipulação dos arquivos CSV:**
   - [organizadorcsv.py](https://github.com/ErisvaldoJ/sistema-empresa-aerea-poo/blob/main/src/utilities/organizadorcsv.py): Aqui estão todos os métodos que manipulam os arquivos csv.
  
3. **Inteface do usuário:**
   - [menufuncionario.py](https://github.com/ErisvaldoJ/sistema-empresa-aerea-poo/blob/main/src/ui/menufuncionario.py): Gerencia a interface do usuário que é um funcionário, tem todas as funcionalidades possíveis.
   - [menupassageiro.py](https://github.com/ErisvaldoJ/sistema-empresa-aerea-poo/blob/main/src/ui/menupassageiro.py): Gerencia a interface do usuário que é um passageiro, possui menos funcionalidades.
  
4. **Entrada:**
   - [main.py](https://github.com/ErisvaldoJ/sistema-empresa-aerea-poo/blob/main/src/main.py): A entrada do sistema, onde é possível escolher o tipo de usuário e interagir com o sistema.

## Instalando e executando do sistema usando o git

*Método recomendado*

### **1. Clone o repositório**
Comece clonando o repositório para a sua máquina:
```
git clone https://github.com/ErisvaldoJ/sistema-empresa-aerea-poo.git
```
Após clonar use o comando cd para ir a pasta do sistema
```
cd sistema-empresa-aerea-poo
```

### **2. Crie um ambiente virtual**

Para criar o ambiente virtual se certifique de estar na pasta do sistema e executar esses comandos:
```
python -m venv venv
```
Verifique se a pasta "venv" foi criada, se sim execute o próximo comando para iniciar o ambiente virtual:
```
.\venv\Scripts\activate
```
Se tudo deu certo, `(venv)` aparecerá no seu terminal ou prompt de comando.

### **3. Execute o sistema**
O último passo é iniciar o sistema, você pode fazer isso usando esse comando:
```
python src/main.py
```

### **4. Desative o ambiente virtual**
Se não deseja mais utilizar o sistema, lembre-se de desativar o ambiente virtual:
```
deactivate
```

## Instalando e executando o sistema diretamente

*Método não recomendado*

### **1. Baixe o arquivo zip**
Na página principal do repositório, clique no botão escrito "Code" e vá em "Download ZIP"

### **2. Extraia o arquivo**
Após baixar, extraia o arquivo com nome "sistema-empresa-aerea-poo-main"

### **3. Execute o sistema**
Acesse o arquivo extraido e execute o `main.py`

## To-do

- [ ] Implementar autenticação para o funcionário
- [ ] Adicionar aeroportos e companhias
- [ ] Melhorar o sistema de reservas
