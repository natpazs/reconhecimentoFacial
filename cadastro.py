# Importa a biblioteca json para armazenar e ler dados dos usuários
import json

# Importa a biblioteca os para manipular pastas e arquivos
import os

# Importa a biblioteca re para validar o formato do e-mail
import re

# Importa as funções responsáveis por capturar e validar fotos
from camera import capturar_foto, validar_foto


# Define o caminho do arquivo JSON que armazenará os usuários
ARQUIVO_JSON = os.path.join("database", "users.json")


# Função responsável por carregar os usuários cadastrados
def carregar_usuarios():

    # Cria a pasta database caso ela ainda não exista
    os.makedirs("database", exist_ok=True)

    # Verifica se o arquivo JSON existe
    if not os.path.exists(ARQUIVO_JSON):

        # Se não existir, retorna uma estrutura com uma lista vazia
        return {"usuarios": []}

    try:

        # Abre o arquivo JSON no modo de leitura
        # encoding="utf-8" permite trabalhar com caracteres especiais
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:

            # Converte o conteúdo JSON para um dicionário Python
            dados = json.load(arquivo)

        # Verifica se os dados possuem a estrutura esperada
        if not isinstance(dados, dict) or not isinstance(dados.get("usuarios"), list):

            # Gera um erro caso o formato esteja incorreto
            raise ValueError("Formato do arquivo de usuários inválido.")

        # Retorna os dados dos usuários
        return dados

    except (json.JSONDecodeError, OSError, ValueError) as erro:

        # Exibe uma mensagem caso ocorra algum problema na leitura
        print(f"Erro ao carregar usuários: {erro}")

        # Retorna uma lista vazia para evitar interromper o programa
        return {"usuarios": []}


# Função responsável por salvar um novo usuário no arquivo JSON
def salvar_usuario(id, nome, email, senha, foto):

    # Carrega os usuários que já estão cadastrados
    dados = carregar_usuarios()

    # Remove espaços e transforma o e-mail em letras minúsculas
    # Isso evita cadastros duplicados por diferenças de escrita
    email = email.strip().lower()

    # Percorre todos os usuários cadastrados
    for usuario in dados["usuarios"]:

        # Verifica se o e-mail informado já está sendo utilizado
        if usuario.get("email", "").strip().lower() == email:

            print("Este e-mail já está cadastrado.")

            # Retorna False indicando que o cadastro não foi realizado
            return False

    # Cria um dicionário com os dados do novo usuário
    novo_usuario = {
        "id": id,
        "nome": nome.strip(),
        "email": email,
        "senha": senha,
        "foto": foto
    }

    # Adiciona o novo usuário à lista de usuários
    dados["usuarios"].append(novo_usuario)

    try:

        # Abre o arquivo JSON no modo de escrita
        # Se não existir, será criado
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:

            # Converte os dados Python para o formato JSON
            # indent=4 organiza o conteúdo com espaçamento
            # ensure_ascii=False mantém os acentos corretamente
            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

        print("Usuário cadastrado com sucesso!")

        # Retorna True indicando que os dados foram salvos
        return True

    except OSError as erro:

        # Exibe uma mensagem caso ocorra um problema ao salvar
        print(f"Erro ao salvar usuário: {erro}")

        return False


# Função responsável por validar os dados informados no cadastro
def validar_dados(nome, email, senha):

    # Verifica se o nome foi preenchido
    if not nome.strip():
        return False, "O nome não pode ficar vazio."

    # Verifica se o nome possui pelo menos dois caracteres
    if len(nome.strip()) < 2:
        return False, "Digite um nome com pelo menos 2 caracteres."

    # Verifica se o e-mail possui um formato válido
    # A expressão regular exige texto antes e depois do @
    # e um ponto seguido pelo domínio
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()):
        return False, "Digite um e-mail válido."

    # Verifica se a senha possui pelo menos oito caracteres
    if len(senha) < 8:
        return False, "A senha deve possuir pelo menos 8 caracteres."

    # Retorna True quando todos os dados são válidos
    return True, ""


# Função responsável por verificar se um rosto já está cadastrado
def verificar_rosto_duplicado(foto_nova, usuarios):

    """
    Compara a foto recém-capturada com todas as fotos cadastradas.

    Retorna:
    - (True, nome): quando encontra um rosto já cadastrado.
    - (False, None): quando não encontra correspondência.
    - (None, erro): quando não consegue concluir a comparação.
    """

    # Importa o DeepFace para realizar a comparação facial
    from deepface import DeepFace

    # Percorre todos os usuários cadastrados
    for usuario in usuarios:

        # Obtém o caminho da fotografia do usuário atual
        foto_existente = usuario.get("foto")

        # Ignora usuários cuja fotografia não existe mais
        if not foto_existente or not os.path.isfile(foto_existente):
            continue

        try:

            # Compara a fotografia nova com a fotografia cadastrada
            resultado = DeepFace.verify(
                img1_path=foto_nova,
                img2_path=foto_existente,
                detector_backend="opencv",
                enforce_detection=True
            )

            # Verifica se os rostos pertencem à mesma pessoa
            if resultado.get("verified", False):

                # Retorna True e o nome do usuário encontrado
                return True, usuario.get("nome", "Usuário desconhecido")

        except Exception as erro:

            # Se ocorrer um erro na comparação,
            # informa que não foi possível concluir a verificação
            return None, str(erro)

    # Retorna False quando nenhum rosto correspondente é encontrado
    return False, None


# Função principal responsável pelo processo de cadastro
def cadastrar():

    print("\n=== Cadastro de Usuário ===")

    # Solicita os dados do usuário
    try:

        # Recebe o nome e remove espaços extras
        nome = input("Digite o nome: ").strip()

        # Recebe o e-mail e remove espaços extras
        email = input("Digite o email: ").strip()

        # Recebe a senha
        senha = input("Digite a senha: ")

    # Trata situações em que a entrada é interrompida
    except (EOFError, KeyboardInterrupt):

        print("\nCadastro cancelado.")
        return

    # Verifica se os dados informados são válidos
    valido, mensagem = validar_dados(nome, email, senha)

    # Se os dados forem inválidos, exibe o motivo e encerra o cadastro
    if not valido:
        print(mensagem)
        return

    # Carrega os usuários já cadastrados
    dados = carregar_usuarios()

    # Normaliza o e-mail para letras minúsculas
    email = email.lower()

    # Verifica novamente se o e-mail já está cadastrado
    for usuario in dados["usuarios"]:

        if usuario.get("email", "").strip().lower() == email:

            print("Este e-mail já está cadastrado.")
            return

    # Gera um novo ID com base nos usuários existentes
    # max() encontra o maior ID e soma 1
    novo_id = max(
        (usuario.get("id", 0) for usuario in dados["usuarios"]),
        default=0
    ) + 1

    # Define o caminho onde a fotografia será armazenada
    foto = os.path.join("faces", f"usuario_{novo_id}.jpg")

    print("\nPosicione seu rosto na câmera.")
    print("Apenas uma pessoa deve aparecer na imagem.")

    # Chama a função que abre a câmera e captura a fotografia
    if not capturar_foto(foto):

        print("Cadastro cancelado. Nenhuma foto foi capturada.")
        return

    # Verifica a qualidade da fotografia e a quantidade de rostos
    imagem_valida, motivo = validar_foto(foto)

    # Se a fotografia não passar na validação
    if not imagem_valida:

        print(f"Foto recusada: {motivo}")

        # Remove a fotografia inválida do computador
        if os.path.exists(foto):
            os.remove(foto)

        return

    # Inicia a verificação para descobrir se o rosto já está cadastrado
    print("\nVerificando se o rosto já possui cadastro...")

    # Compara a nova fotografia com as fotografias existentes
    duplicado, resultado = verificar_rosto_duplicado(
        foto,
        dados["usuarios"]
    )

    # Se não for possível realizar a comparação,
    # o cadastro é bloqueado por segurança
    if duplicado is None:

        print(f"Não foi possível verificar os rostos: {resultado}")
        print("Cadastro cancelado por segurança.")

        # Remove a fotografia capturada
        if os.path.exists(foto):
            os.remove(foto)

        return

    # Se o rosto já estiver cadastrado, impede um novo registro
    if duplicado:

        print("Este rosto já está cadastrado no sistema.")
        print(f"Cadastro existente: {resultado}")
        print("Não é possível cadastrar o mesmo rosto novamente.")

        # Remove a fotografia que acabou de ser capturada
        if os.path.exists(foto):
            os.remove(foto)

        return

    # Se todas as verificações forem aprovadas,
    # chama a função para salvar os dados do usuário
    sucesso = salvar_usuario(
        novo_id,
        nome,
        email,
        senha,
        foto
    )

    # Se ocorrer algum erro ao salvar os dados,
    # remove a fotografia para evitar arquivos desnecessários
    if not sucesso and os.path.exists(foto):
        os.remove(foto)