import json
import os
import cv2
from camera import capturar_foto

ARQUIVO_JSON = "database/users.json"


def carregar_usuarios():
    if not os.path.exists(ARQUIVO_JSON):
        return {"usuarios": []}

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_usuario(id, nome, email, senha, foto):
    dados = carregar_usuarios()

    novo_usuario = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senha,
        "foto": foto
    }

    dados["usuarios"].append(novo_usuario)

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print("Usuário cadastrado com sucesso!")


def cadastrar():
    print("=== Cadastro de Usuário ===")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    dados = carregar_usuarios()


    novo_id = len(dados["usuarios"]) + 1

    foto = f"faces/usuario_{novo_id}.jpg"

    ft_usuario = capturar_foto(foto)

    if ft_usuario:
        salvar_usuario(novo_id, nome, email, senha, foto)
    else:
        print("Cadastro cancelado. Nenhuma foto foi capturada.")

