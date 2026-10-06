from cadastro import cadastrar
from login import fazer_login

while True:
    print("\n===== RECONHECIMENTO FACIAL =====")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar()

    elif opcao == 2:
        fazer_login()  

    elif opcao == 3:
        print("Saindo...")
        break

    else:
        print("Opção inválida.")