
# Devolutiva formativa — Atividade 02 da SA

**Estudante:** Ewaldo da Silva Ritzmann Neto  
**Turma:** Rio Negrinho — Manhã  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** Portal Hospitalar — Área do Paciente  
**Atividade:** Interface funcional  
**Arquivos analisados:** `aplicativo/codigo/app.py`, templates HTML e `static/style.css`

## O que você já conseguiu desenvolver

Ewaldo, seu projeto utiliza **Flask para conectar uma aplicação Python a uma interface web**.

A organização dos diretórios e a utilização dos recursos do framework são pontos positivos importantes.

Pontos positivos identificados:

- Criou uma aplicação utilizando `Flask`.
- Organizou o código Python separadamente dos templates HTML.
- Utilizou `render_template()` para apresentar páginas.
- Criou rotas para login e dashboard.
- Aplicou métodos HTTP `GET` e `POST`.
- Utilizou `request.form` para receber dados de formulários.
- Aplicou `redirect()` e `url_for()` para controlar a navegação.
- Desenvolveu arquivos específicos de login e painel do paciente.
- Separou as regras visuais no arquivo `style.css`.
- Organizou a interface com campos, seções, cartões e tabelas.

A estrutura demonstra compreensão inicial da comunicação entre navegador e aplicação Flask.

## Evolução da Situação de Aprendizagem

O repositório apresenta uma aplicação com duas telas relacionadas ao contexto hospitalar:

- **Login:** formulário para entrada do usuário.
- **Dashboard:** estrutura visual para apresentar informações de pacientes, consultas, exames e medicamentos.

Isso representa uma evolução importante para a construção de uma interface web.

## O que precisa ser corrigido

### 1. Implementar a verificação do login

Atualmente, a rota de login recebe os dados e redireciona para o dashboard sem verificar as informações.

**Como melhorar:** criar uma validação inicial com usuários fictícios para diferenciar credenciais válidas e inválidas. Apresentar uma mensagem quando a entrada não for aceita.

### 2. Evitar encaminhar dados sensíveis pela URL

O código envia os dados recebidos do formulário para `url_for()` durante o redirecionamento.

Isso pode incluir informações que não deveriam aparecer no endereço do navegador.

**Como melhorar:** não transportar senhas ou outros dados sensíveis em parâmetros de URL. Utilizar o redirecionamento apenas após concluir a verificação e adotar um mecanismo apropriado de sessão.

### 3. Preencher as informações do dashboard

O HTML possui elementos destinados a nome, idade, consultas e resultados, mas ainda não há processamento no backend para preencher essas informações.

**Como melhorar:** utilizar inicialmente dados fictícios fornecidos pelo Flask ao template e exibi-los por meio do Jinja2.

### 4. Concluir o comportamento da rota do dashboard

O tratamento de `POST` nessa rota possui apenas `pass`.

**Como melhorar:** implementar uma ação correspondente ou retirar o método `POST` enquanto a página utilizar apenas `GET`.

## Oportunidades de melhoria

### 5. Modularizar as funcionalidades

A organização de templates e arquivos estáticos já é positiva.

**Como melhorar:** conforme o sistema crescer, separar rotas, serviços e regras de pacientes em funções ou módulos específicos.

### 6. Melhorar a documentação do código

**Como melhorar:** adicionar docstrings às funções `login()` e `dashboard()`, explicando o objetivo de cada rota, os métodos aceitos e o comportamento esperado.

### 7. Preparar configurações adequadas

O Flask é iniciado com `debug=True`, recurso útil durante o desenvolvimento local.

**Como melhorar:** desativar a depuração em ambientes publicados e documentar as dependências do projeto.

### 8. Melhorar a consistência da interface

**Como melhorar:** padronizar o idioma das páginas, revisar rótulos e adicionar mensagens visíveis para entradas inválidas.

## Testes recomendados

1. Executar o Flask e acessar a rota `/Login`.
2. Conferir o carregamento do CSS.
3. Enviar um formulário com campos preenchidos.
4. Testar um login inválido.
5. Confirmar que senhas não aparecem na URL.
6. Acessar o dashboard e conferir os dados fictícios.
7. Verificar o comportamento ao acessar diretamente `/Dashboard`.
8. Testar as páginas em diferentes tamanhos de tela.

## Prioridades para a próxima versão

1. **Implementar a verificação das credenciais.**
2. **Não encaminhar senhas na URL.**
3. **Apresentar informações dinâmicas no dashboard.**
4. **Finalizar ou remover o tratamento de POST não implementado.**
5. **Documentar as rotas e os procedimentos de execução.**

## Mensagem final

Ewaldo, seu trabalho demonstra uma base importante no desenvolvimento de aplicações web com Flask.

Você já utiliza rotas, templates, formulários e organização de arquivos de forma coerente.

O próximo passo é ampliar a lógica por trás das páginas, permitindo que o login valide informações e que o dashboard apresente dados fornecidos pelo Python.
