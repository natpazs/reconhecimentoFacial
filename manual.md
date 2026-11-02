# Manual — Reconhecimento Facial

> Este manual complementa o [README](./README.md), que contém a descrição do projeto e as instruções de instalação e execução.

## 1. Usar o programa

Depois de iniciar o programa conforme as instruções do README, escolha uma opção digitando o número correspondente no terminal e pressionando Enter.

- **1 — Cadastro:** inicia o cadastro de um usuário.
- **2 — Login:** inicia o login.
- **3 — Sair:** encerra o programa.

## 2. Cadastrar um usuário

uma vez selecionada a opção de cadastro, o usuario será direcionado para o menu de cadastro.

- **nome:** nome do usuário.
- **email:** email do usuário.
- **senha:** senha do usuário.

O sistema aplica estas regras:

- O nome não pode ficar vazio e deve ter pelo menos 2 caracteres.
- O email deve ter um formato válido e ainda não pode estar cadastrado.
- O sistema não diferencia letras maiusculas de minusculas no email.
- A senha deve ter pelo menos 8 caracteres.
- O rosto não pode já estar associado a outro cadastro.

Quando a janela da câmera abrir:

- A janela deve estar selecionada.
- Pressione **barra de espaço** para capturar a foto.
- Pressione **Esc** para cancelar.

A foto pode ser recusada se estiver pequena, escura, clara ou desfocada, se não houver um rosto visível ou se aparecer mais de um rosto.

**Dicas para tentar novamente:** fique de frente para a câmera, mantenha o rosto no enquadramento, procure um local bem iluminado e evite se movimentar durante a captura.

Uma vez que o cadastro for finalizado, o usuario será direcionado para o menu inicial.

## 3. Fazer login

uma vez selecionada a opção de cadastro, o usuario será direcionado para o menu de login.

- **email:** email do usuário.
- **senha:** senha do usuário.

Se as credenciais estiverem corretas, o sistema abrirá a câmera para uma nova captura.

Quando a janela da câmera abrir:

- A janela deve estar selecionada.
- Pressione **barra de espaço** para capturar a foto.
- Pressione **Esc** para cancelar.

**Se o reconhecimento falhar:** tente novamente com o rosto visível, bem enquadrado e em boas condições de iluminação. Confira também se a foto do cadastro ainda está disponível.

Uma vez que o login for finalizado com suceesso, o usuario será direcionado para o menu da sessão.

## 4 Menu da sessão

Após um login bem-sucedido, o usuário é direcionado para o menu da sessão:

- **1 — Logout:** encerra a sessão e retorna ao menu inicial.
- **2 — Sair:** encerra o programa.

Se for digitada uma opção diferente das exibidas, o sistema informa que ela é inválida.

## 5. Problemas comuns

| Problema | O que verificar |
|---|---|
| A câmera não pode ser acessada. | Verifique se está conectada, se funciona em outro programa, se outro aplicativo não a está usando e se o sistema operacional permite seu acesso. |
| A foto foi recusada. | Confira a iluminação, a nitidez, o enquadramento e se apenas uma pessoa aparece na imagem. |
| E-mail ou senha incorretos. | Confira os dados digitados. O e-mail não diferencia maiúsculas de minúsculas; a senha deve ser informada como foi cadastrada. |
| O reconhecimento facial falhou. | Tente outra captura. Se o problema persistir, verifique se a foto cadastrada ainda existe. |
| O primeiro uso está demorando. | O README informa que a primeira execução pode demorar enquanto o DeepFace carrega ou baixa modelos. |

**[A COMPLETAR]** Testar essas orientações e acrescentar outras mensagens de erro que apareçam na versão final do programa.

## 5. Dados

Os dados dos usuários ficam em `database/users.json`, e as fotos de cadastro ficam na pasta `faces/`. Durante o login, o programa cria uma foto temporária e tenta removê-la ao final do processo.

> **Atenção:** no código atual, a senha é armazenada sem criptografia no arquivo JSON. Não use uma senha real ou reutilizada em outros serviços. As fotos faciais também são dados sensíveis; restrinja o acesso ao computador e aos arquivos do projeto.

O menu não oferece opções para recuperar senha, alterar dados ou excluir um cadastro.