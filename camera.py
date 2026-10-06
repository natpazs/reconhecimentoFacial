import cv2

def capturar_foto(caminho):

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Não foi possível acessar a câmera")
        return False
    
    while True:

        ret, frame = cap.read()
        
        if not ret:
            print("Falha ao capturar o vídeo")
            break

        cv2.imshow("Camera - Cadastro", frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):  # Pressione a barra de espaço para capturar a foto
            cv2.imwrite(caminho, frame)
            cap.release()
            cv2.destroyAllWindows()
            return True


        elif cv2.waitKey(1) & 0xFF == 27:  # Pressione ESC para sair sem capturar
            print("Captura cancelada.")
            cap.release()
            cv2.destroyAllWindows()
            return False