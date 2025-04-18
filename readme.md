# Projeto Flask de Gerenciamento de Usuários e Séries

Este projeto é uma aplicação web que permite o gerenciamento de usuários e a busca de séries através da API do The Movie Database (TMDb). O sistema armazena dados em um arquivo JSON e permite o upload de imagens.

## Estrutura do Código

O código é organizado em um Blueprint chamado `front_controller`, e dividido em várias funções que lidam com a manipulação de dados, interação com a API e gerenciamento de usuários. Abaixo estão as principais funcionalidades:

### 1. Manipulação de Arquivos

#### Funções `load_data` e `save_data`

- **`load_data()`**: Carrega os dados de usuários a partir de um arquivo JSON. Se o arquivo não existir, retorna uma lista vazia.
- **`save_data(data)`**: Salva os dados de usuários no arquivo JSON.

### 2. Interação com a API

#### Função `escolhaS`

- **Descrição**: Interage com a API do TMDb para buscar séries de acordo com o gênero selecionado.
- **Parâmetros**: `opcao` - O gênero da série (ex: 'kids', 'drama', 'comedy').
- **Retorno**: Retorna uma lista de séries e uma mensagem sobre o resultado da busca.

### 3. Gerenciamento de Usuários

#### Funções `novoUsuario` e `logandoUsuario`

- **`novoUsuario(usuario, senha)`**: Adiciona um novo usuário à lista de usuários, verificando se o usuário já existe. Retorna `True` se o cadastro for bem-sucedido e `False` caso contrário.
- **`logandoUsuario(usuario, senha)`**: Verifica se as credenciais fornecidas correspondem a um usuário existente. Retorna `True` se o login for bem-sucedido e `False` caso contrário.

### 4. Upload de Imagens

#### Funções `verificarArquivos` e `upload_imagem`

- **`verificarArquivos(imagem)`**: Verifica se o arquivo de imagem está em um dos formatos permitidos.
- **`upload_imagem(imagem)`**: Realiza o upload da imagem, garantindo que o diretório de uploads exista. Gera um nome único para a imagem e a salva no diretório especificado. Retorna o caminho relativo da imagem.

### 5. Verificação de Login

Antes de cada requisição, a função `verificar_login` é chamada para verificar se o usuário está logado. Se não estiver, a aplicação tenta recuperar o nome de usuário a partir de um cookie.

### 6. Rotas

#### Rota Principal (`/`)

- **Método:** `GET`
- **Descrição:** Renderiza a página principal da aplicação.

#### Rota de Cadastro (`/cadastro`)

- **Métodos:** `GET`, `POST`
- **Descrição:** Permite que novos usuários se cadastrem. Se o método for `POST`, o sistema tenta criar um novo usuário com as credenciais fornecidas. Se o cadastro for bem-sucedido, o usuário é redirecionado para a página de login.

#### Rota de Login (`/login`)

- **Métodos:** `GET`, `POST`
- **Descrição:** Permite que usuários existentes façam login. Se o método for `POST`, o sistema verifica as credenciais e, se forem válidas, cria uma sessão para o usuário. Há também a opção de lembrar o usuário através de um cookie.

#### Rota de Séries (`/series`)

- **Métodos:** `GET`, `POST`
- **Descrição:** Permite que usuários logados visualizem séries. Se o método for `POST`, o usuário pode selecionar um tipo de série e o sistema retorna as séries correspondentes. Se o usuário não estiver logado, ele é redirecionado para a página de login.

#### Rota de Sair (`/sair`)

- **Métodos:** `GET`, `POST`
- **Descrição:** Permite que o usuário saia da sessão. Se o método for `POST`, a sessão é encerrada e o cookie de login é removido.

## 7. Templates

A aplicação utiliza templates HTML para renderizar as páginas. O template principal é estruturado da seguinte forma:

### Estrutura do Template

- **Cabeçalho**: Inclui a configuração do Bootstrap para estilização e um título para a aplicação.
- **Navegação**: Um menu de navegação que permite ao usuário acessar as diferentes seções da aplicação (Principal, Cadastro, Login, Séries). O estado do botão de logout é dinâmico, dependendo se o usuário está logado ou não.
- **Mensagens Flash**: Exibe mensagens de feedback para o usuário, como confirmações de cadastro ou erros de login.
- **Conteúdo Dinâmico**: A seção `{% block conteudo %}` permite que diferentes páginas insiram seu conteúdo específico.
- **Rodapé**: Um rodapé simples que exibe informações sobre o projeto.

### Exemplo de Uso

O template utiliza a função `render_template()` para renderizar as páginas, passando variáveis e mensagens conforme necessário. A estrutura de controle do Jinja2 é utilizada para exibir diferentes elementos com base no estado da sessão do usuário.


## Dependências

Para executar este projeto, você precisará das seguintes dependências:

- `requests`: Para fazer requisições HTTP à API do TMDb.
- `uuid`: Para gerar nomes únicos para os arquivos de imagem.
- `Flask`
- (Outras dependências que você possa precisar)

## Configuração

Certifique-se de que o arquivo `config.py` esteja configurado corretamente com as seguintes variáveis:

- `DATA_FILE`: Caminho para o arquivo JSON onde os dados dos usuários serão armazenados.
- `UPLOAD_FOLDER`: Diretório onde as imagens serão salvas.
- `TIPOS_IMAGEM`: Lista de tipos de imagem permitidos para upload.

## Como Executar

1. Instale as dependências necessárias.
2. Configure o arquivo `config.py`.
3. Execute a aplicação Flask.

