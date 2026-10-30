# Importa a biblioteca os para verificar e excluir arquivos
import os

# Importa a função responsável por carregar os usuários cadastrados
from cadastro import carregar_usuarios

# Importa as funções de captura e validação de fotografias
from camera import capturar_foto, validar_foto


# Função responsável por realizar o login do usuário
def fazer_login():

    print("\n=== Login de Usuário ===")

    # Solicita as credenciais para acessar o sistema
    try:

        # Recebe o e-mail e transforma em letras minúsculas
        email = input("Digite o email: ").strip().lower()

        # Recebe a senha informada
        senha = input("Digite a senha: ")

    # Trata situações em que o usuário interrompe a entrada
    except (EOFError, KeyboardInterrupt):

        print("\nLogin cancelado.")
        return None

    # Carrega a lista de usuários cadastrados no arquivo JSON
    usuarios = carregar_usuarios()["usuarios"]

    # Inicializa a variável que armazenará o usuário encontrado
    usuario_encontrado = None

    # Percorre os usuários cadastrados
    for usuario in usuarios:

        # Verifica se o e-mail e a senha correspondem
        # aos dados armazenados no cadastro
        if (
            usuario.get("email", "").strip().lower() == email
            and usuario.get("senha") == senha
        ):

            # Armazena os dados do usuário encontrado
            usuario_encontrado = usuario

            # Interrompe o loop porque o usuário já foi encontrado
            break

    # Verifica se nenhum usuário foi encontrado
    if usuario_encontrado is None:

        print("E-mail ou senha incorretos.")

        # Retorna None indicando que o login falhou
        return None

    # Informa que as credenciais foram encontradas
    print(f"\nUsuário encontrado: {usuario_encontrado['nome']}")
    print("Iniciando reconhecimento facial...")

    # Define o caminho da fotografia temporária do login
    foto_login = os.path.join("faces", "login_temp.jpg")

    # Cria a pasta faces caso ela ainda não exista
    os.makedirs("faces", exist_ok=True)

    try:

        # Abre a câmera para capturar a fotografia do usuário
        if not capturar_foto(foto_login):

            print("Login cancelado.")
            return None

        # Verifica a qualidade da fotografia capturada
        # e se existe apenas um rosto na imagem
        imagem_valida, motivo = validar_foto(foto_login)

        # Se a fotografia não for válida, impede o login
        if not imagem_valida:

            print(f"Foto recusada: {motivo}")
            return None

        # Obtém o caminho da fotografia armazenada no cadastro
        foto_cadastrada = usuario_encontrado.get("foto")

        # Verifica se a fotografia cadastrada existe
        if not foto_cadastrada or not os.path.isfile(foto_cadastrada):

            print("Foto cadastrada não encontrada.")
            return None

        try:

            # Importa o DeepFace para realizar o reconhecimento facial
            from deepface import DeepFace

            # Compara a fotografia capturada no login
            # com a fotografia armazenada no cadastro
            resultado = DeepFace.verify(
                img1_path=foto_login,
                img2_path=foto_cadastrada,
                detector_backend="opencv",
                enforce_detection=True
            )

            # Verifica se as duas fotografias pertencem à mesma pessoa
            if resultado.get("verified", False):

                # Informa que o reconhecimento facial foi realizado
                print(
                    f"\nReconhecimento facial bem-sucedido!"
                    f"\nBem-vindo, {usuario_encontrado['nome']}!"
                )

                # Retorna os dados do usuário autenticado
                # Esses dados serão utilizados no menu principal
                return usuario_encontrado

            else:

                # Informa que os rostos não correspondem
                print("Falha no reconhecimento facial.")
                print("Acesso negado.")

                # Retorna None indicando que o acesso foi negado
                return None

        except Exception as erro:

            # Exibe uma mensagem caso ocorra algum problema
            # durante o reconhecimento facial
            print(f"Erro no reconhecimento facial: {erro}")
            return None

    finally:

        # Exclui a fotografia temporária após o processo de login
        # Esse bloco é executado mesmo quando ocorre um erro
        if os.path.exists(foto_login):

            try:

                # Remove o arquivo temporário
                os.remove(foto_login)

            except OSError as erro:

                # Informa caso não seja possível excluir a fotografia
                print(f"Não foi possível excluir a foto temporária: {erro}")