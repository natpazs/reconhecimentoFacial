# Importa a função responsável pelo cadastro de novos usuários
from cadastro import cadastrar

# Importa a função responsável pelo login dos usuários
from login import fazer_login


# Função principal do sistema
def main():

    # Guarda os dados do usuário que estiver logado
    # Inicialmente, nenhum usuário está conectado
    usuario_logado = None

    # Mantém o sistema funcionando até que o usuário escolha sair
    while True:

        # MENU PARA USUÁRIO NÃO LOGADO
        if usuario_logado is None:

            # Exibe as opções disponíveis para quem ainda não entrou
            print("\n===== RECONHECIMENTO FACIAL =====")
            print("1 - Cadastro")
            print("2 - Login")
            print("3 - Sair")

            # Recebe a opção digitada pelo usuário
            # strip() remove espaços desnecessários
            opcao = input("Escolha uma opção: ").strip()

            # Se escolher 1, inicia o cadastro
            if opcao == "1":
                cadastrar()

            # Se escolher 2, inicia o processo de login
            elif opcao == "2":

                # A função retorna os dados do usuário
                # caso o login seja realizado com sucesso
                usuario_logado = fazer_login()

            # Se escolher 3, encerra o programa
            elif opcao == "3":
                print("Saindo...")
                break

            # Caso digite uma opção diferente das disponíveis
            else:
                print("Opção inválida. Digite 1, 2 ou 3.")

        # MENU PARA USUÁRIO LOGADO
        else:

            # Exibe uma mensagem de boas-vindas
            # upper() transforma o nome em letras maiúsculas
            print(f"\n===== BEM-VINDO, {usuario_logado['nome'].upper()}! =====")

            # Exibe as opções disponíveis para o usuário conectado
            print("1 - Logout")
            print("2 - Sair")

            # Recebe a opção escolhida
            opcao = input("Escolha uma opção: ").strip()

            # Se escolher 1, encerra a sessão do usuário
            if opcao == "1":

                # Define novamente como None para indicar
                # que não existe mais nenhum usuário conectado
                usuario_logado = None

                print("Logout realizado com sucesso!")

            # Se escolher 2, encerra o programa
            elif opcao == "2":

                print("Saindo...")
                break

            # Caso digite uma opção inválida
            else:
                print("Opção inválida. Digite 1 ou 2.")


# Verifica se este arquivo está sendo executado diretamente
# Se estiver, chama a função principal do sistema
if __name__ == "__main__":
    main()