print("=== SISTEMA DE CADASTRO DE ALUNOS ===")
 
alunos = {}

while True:
    nome = input("Digite o nome do aluno")
    if nome == "Fim":
        break
    try:
        nota = float(input("Digite a nota do aluno: "))
        alunos[nome] = nota
    except ValueError:
        print("Número de nota inválido.")

