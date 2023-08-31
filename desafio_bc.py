import textwrap3

def menu():
    menu = """\n
    ================= MENU ===============
    [1] Criar Novo Usuário
    [2] Filtrar Usuário
    [3] Exibir Extrato
    [4] Sacar
    [5] Depositar
    [6] Sair
    => """
    return input(textwrap3.dedent(menu))


def criar_novo_usuario(usuarios):
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    
    usuarios.append({"nome": nome, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def exibir_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("===================")


def sacar(saldo, valor, extrato):
    if valor > 0 and saldo >= valor:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
    else:
        print("Saque não autorizado. Verifique o valor ou saldo.")
    return saldo, extrato


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Depósito não autorizado. Verifique o valor.")
    return saldo, extrato


def main():
    usuarios = []
    extrato = ""
    saldo = 0

    while True:
        opcao = menu()

        if opcao == "1":
            criar_novo_usuario(usuarios)

        elif opcao == "2":
            cpf = input("Informe o CPF para filtrar: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario:
                print("Usuário encontrado:")
                print(usuario)
            else:
                print("Usuário não encontrado.")

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            valor = float(input("Valor do saque: "))
            saldo, extrato = sacar(saldo, valor, extrato)

        elif opcao == "5":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")


if __name__ == "__main__":
    main()
