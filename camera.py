# Importa a biblioteca OpenCV, utilizada para acessar a câmera
# e realizar operações com imagens
import cv2

# Importa a biblioteca os, utilizada para manipular pastas e arquivos
import os


# Função responsável por abrir a câmera e capturar uma fotografia
# O parâmetro caminho indica onde a imagem será salva
def capturar_foto(caminho):

    # Obtém o nome da pasta onde a foto será armazenada
    pasta = os.path.dirname(caminho)

    # Verifica se foi informada uma pasta
    if pasta:

        # Cria a pasta caso ela ainda não exista
        # exist_ok=True evita erro se a pasta já estiver criada
        os.makedirs(pasta, exist_ok=True)

    # Inicializa a webcam
    # O número 0 representa a câmera principal do computador
    cap = cv2.VideoCapture(0)

    # Verifica se a câmera foi aberta corretamente
    if not cap.isOpened():

        print("Não foi possível acessar a câmera.")

        # Libera o recurso da câmera
        cap.release()

        # Retorna False indicando que não foi possível capturar
        return False

    # Variável que indica se a foto foi capturada
    # Inicialmente, nenhuma imagem foi registrada
    capturada = False

    try:

        # Mantém a câmera funcionando continuamente
        while True:

            # Captura uma imagem da webcam
            # ret indica se a captura foi realizada
            # frame contém a imagem capturada
            ret, frame = cap.read()

            # Verifica se a imagem foi recebida corretamente
            if not ret or frame is None:

                print("Falha ao capturar o vídeo.")
                break

            # Exibe a imagem da webcam com as instruções
            cv2.imshow("Camera", frame)

            # Verifica qual tecla foi pressionada
            # waitKey(1) aguarda 1 milissegundo
            # & 0xFF permite identificar corretamente a tecla
            tecla = cv2.waitKey(1) & 0xFF

            # ESPAÇO: captura e salva a fotografia
            if tecla == ord(" "):

                # Salva a imagem no caminho informado
                # imwrite() retorna True se conseguir salvar
                if cv2.imwrite(caminho, frame):

                    # Indica que a captura foi realizada
                    capturada = True

                else:

                    print("Não foi possível salvar a imagem.")

                # Encerra o loop após a tentativa de captura
                break

            # ESC: cancela a captura da fotografia
            elif tecla == 27:

                print("Captura cancelada.")
                break

    finally:

        # Libera a câmera para que outros programas possam utilizá-la
        cap.release()

        # Fecha todas as janelas abertas pelo OpenCV
        cv2.destroyAllWindows()

    # Retorna True se a foto foi salva e False caso contrário
    return capturada


# Função responsável por verificar se uma fotografia possui
# qualidade suficiente para ser utilizada no reconhecimento facial
def validar_foto(caminho):

    # Abre a imagem armazenada no caminho informado
    imagem = cv2.imread(caminho)

    # Verifica se a imagem foi carregada corretamente
    if imagem is None:
        return False, "Não foi possível abrir a imagem."

    # Obtém a altura e a largura da imagem
    altura, largura = imagem.shape[:2]

    # Verifica se a resolução da imagem é suficiente
    if largura < 200 or altura < 200:
        return False, "Imagem muito pequena."

    # Converte a imagem colorida para escala de cinza
    # Isso facilita os cálculos de brilho e nitidez
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Calcula o brilho médio da imagem
    # Valores muito baixos indicam uma imagem escura
    brilho = float(cinza.mean())

    # Calcula a nitidez da imagem utilizando o Laplaciano
    # Valores baixos podem indicar que a imagem está desfocada
    nitidez = float(
        cv2.Laplacian(cinza, cv2.CV_64F).var()
    )

    # Verifica se a imagem está muito escura
    if brilho < 40:
        return False, "Imagem muito escura."

    # Verifica se a imagem está muito clara
    if brilho > 220:
        return False, "Imagem muito clara."

    # Verifica se a imagem está desfocada
    if nitidez < 40:
        return False, "Imagem desfocada."

    try:

        # Importa o DeepFace, biblioteca utilizada
        # para detectar e reconhecer rostos
        from deepface import DeepFace

        # Detecta os rostos presentes na imagem
        rostos = DeepFace.extract_faces(
            img_path=caminho,
            detector_backend="opencv",
            enforce_detection=True,
            align=True
        )

        # Verifica se nenhum rosto foi encontrado
        if len(rostos) == 0:
            return False, "Nenhum rosto encontrado."

        # Impede imagens que contenham mais de um rosto
        if len(rostos) > 1:
            return False, "Mais de um rosto encontrado. Apenas uma pessoa pode aparecer."

    except Exception as erro:

        # Retorna uma mensagem caso ocorra algum erro
        # durante a análise da imagem
        return False, f"Erro ao analisar a imagem: {erro}"

    # Se todas as verificações forem aprovadas,
    # retorna True indicando que a imagem é válida
    return True, "Imagem válida."