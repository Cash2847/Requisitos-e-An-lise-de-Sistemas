MAX = 100

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

funcionarios = []
total = 0

def adicionarFuncionario():
    global total
    if total >= MAX:
        print("Limite atingido!")
        return
    nome = input("Nome: ").strip()
    cargo = input("Cargo: ").strip()
    salario = float(input("Salário: "))
    funcionarios.append(Funcionario(nome, cargo, salario))
    total += 1
    print("Funcionário cadastrado!")

def listarFuncionarios():
    if total == 0:
        print("Nenhum funcionário cadastrado.")
        return
    print("\nLista de funcionários:")
    for i, f in enumerate(funcionarios, 1):
        print(f"{i}) {f.nome} - {f.cargo} - R$ {f.salario:.2f}")

def buscarFuncionario():
    nomeBusca = input("Nome do funcionário: ").strip()
    for f in funcionarios:
        if f.nome == nomeBusca:
            print(f"Cargo: {f.cargo} | Salário: R$ {f.salario:.2f}")
            return
    print("Funcionário não encontrado.")

def main():
    while True:
        print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
        print("1 - Adicionar funcionário")
        print("2 - Listar funcionários")
        print("3 - Buscar funcionário")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            adicionarFuncionario()
        elif opcao == '2':
            listarFuncionarios()
        elif opcao == '3':
            buscarFuncionario()
        elif opcao == '0':
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()