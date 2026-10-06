from cadastro import carregar_usuarios
from camera import capturar_foto
from deepface import DeepFace
import os

def fazer_login():
    print("=== Login de Usuário ===")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    usuarios = carregar_usuarios()["usuarios"]

    usuario_encontrado = None
    
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        print(f"Bem-vindo, {usuario_encontrado['nome']}!")
        print("Iniciando reconhecimento facial...")

        foto_login = "faces/login_temp.jpg"

        ft_login = capturar_foto(foto_login)

        if ft_login:
            resultado = DeepFace.verify(foto_login, usuario_encontrado["foto"])

            if resultado["verified"]:
                print(f"Reconhecimento facial bem-sucedido! Bem-vindo, {usuario_encontrado['nome']}!")
            else:
                print("Falha no reconhecimento facial. Acesso negado.")

            os.remove(foto_login)

    if usuario_encontrado is None:
        print("Usuário não encontrado.")
        