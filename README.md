# Reconhecimento Facial

## Sobre o projeto

O **Reconhecimento Facial** é um sistema desenvolvido em Python que permite realizar o cadastro e o login de usuários por meio do reconhecimento facial.

O objetivo do projeto é utilizar visão computacional e inteligência artificial para identificar e verificar usuários, adicionando uma camada de autenticação por reconhecimento facial ao processo de login.

Durante o cadastro, o sistema coleta os dados do usuário e captura uma fotografia pela webcam. No login, além de conferir o e-mail e a senha, o sistema compara o rosto capturado com a imagem armazenada durante o cadastro.

## Tecnologias e bibliotecas utilizadas

- **Python:** linguagem de programação utilizada para desenvolver toda a lógica do sistema.
- **OpenCV (opencv-contrib-python):** biblioteca de visão computacional responsável por acessar a webcam, capturar imagens, exibir a câmera e salvar fotografias.
- **DeepFace:** biblioteca de reconhecimento facial que utiliza modelos de inteligência artificial para analisar rostos e verificar se duas imagens pertencem à mesma pessoa.
- **JSON:** formato utilizado para armazenar os dados dos usuários cadastrados, como nome, e-mail, senha e caminho da fotografia.
- **OS (os):** biblioteca nativa do Python utilizada para manipular arquivos e diretórios, verificar a existência de imagens e organizar os caminhos do projeto.
- **RE (re):** biblioteca nativa utilizada para validar informações, como o formato do e-mail, por meio de expressões regulares.

## Como o projeto funciona

O sistema possui duas funcionalidades principais: cadastro e login.

### 1. Cadastro de usuários

Ao selecionar a opção de cadastro, o sistema:

1. Solicita o nome, o e-mail e a senha do usuário.
2. Verifica se os dados informados são válidos.
3. Confere se já existe algum usuário cadastrado com o mesmo e-mail.
4. Abre a webcam para capturar uma fotografia do usuário.
5. Analisa a imagem para verificar se ela possui qualidade adequada e contém um rosto.
6. Compara a fotografia com as imagens dos usuários já cadastrados, evitando registros duplicados.
7. Caso todas as verificações sejam aprovadas, salva os dados no arquivo JSON e a fotografia na pasta correspondente.

### 2. Login de usuários

Ao selecionar a opção de login, o sistema:

1. Solicita o e-mail e a senha cadastrados.
2. Verifica se existe um usuário com essas informações.
3. Caso os dados estejam corretos, abre a webcam para capturar uma nova fotografia.
4. Valida a imagem capturada.
5. Utiliza o DeepFace para comparar a fotografia atual com a imagem armazenada durante o cadastro.
6. Se o reconhecimento facial for aprovado, o acesso é liberado e o sistema identifica o usuário conectado.
7. Caso alguma verificação falhe, o acesso é negado.

Após o login, o usuário pode encerrar sua sessão (logout) ou sair do sistema.

## Estrutura do projeto

```text
reconhecimentoFacial/
│
├── main.py
├── cadastro.py
├── login.py
├── camera.py
│
├── database/
│   └── users.json
│
├── faces/
│   └── usuario_<id>.jpg
│
└── venv/
```

**Descrição dos arquivos:**

- `main.py`: arquivo principal, responsável por apresentar o menu inicial e controlar a navegação entre cadastro, login e logout.
- `cadastro.py`: contém as funções responsáveis pelo cadastro, validação dos dados, verificação de e-mail e identificação de rostos duplicados.
- `login.py`: realiza a autenticação do usuário por meio do e-mail, senha e reconhecimento facial.
- `camera.py`: controla o acesso à webcam, captura as fotografias e realiza a validação das imagens.
- `database/users.json`: armazena as informações dos usuários cadastrados.
- `faces/`: armazena as fotografias utilizadas no reconhecimento facial.

## Instalação e configuração

Siga os passos abaixo para configurar o ambiente e instalar as dependências necessárias.

### 1. Clonar o repositório

```bash
git clone git@github.com:natpazs/reconhecimentoFacial.git
```

Entre na pasta do projeto:

```bash
cd reconhecimentoFacial
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Atualizar o pip

```bash
python.exe -m pip install --upgrade pip
```

### 5. Instalar o DeepFace

```bash
pip install deepface
```

### 6. Instalar o Werkzeug

```bash
python -m pip install Werkzeug --retries 10 --timeout 60
```

### 7. Remover versões anteriores do OpenCV

```bash
python -m pip uninstall -y opencv-python opencv-contrib-python opencv-python-headless opencv-contrib-python-headless
```

### 8. Instalar a versão utilizada do OpenCV

```bash
python -m pip install opencv-contrib-python==4.11.0.86
```

## Como executar o projeto

Após concluir a instalação e ativar o ambiente virtual, execute:

```bash
python main.py
```

O menu inicial será apresentado no terminal, permitindo escolher entre cadastrar um novo usuário, realizar login ou sair do sistema.

## Observações

- É necessário possuir uma webcam conectada ao computador para realizar o cadastro e o login.
- O primeiro uso do DeepFace pode levar mais tempo devido ao carregamento ou download dos modelos de reconhecimento facial.
- As pastas `database/` e `faces/` são utilizadas para armazenar os dados e as fotografias dos usuários.
- O projeto foi desenvolvido para fins educacionais e de aprendizado sobre Python, visão computacional e reconhecimento facial.