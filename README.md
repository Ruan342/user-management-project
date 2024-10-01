
# User Management Project

Este projeto é uma aplicação para gerenciar usuários, com Flask no back-end, MongoDB como banco de dados e Vue.js no front-end.

## Funcionalidades

- CRUD de usuários
- Visualização de usuários
- Edição e exclusão de usuários

## Como rodar o projeto

### Back-end (Flask)

1. Instale as dependências do Python listadas no arquivo `requirements.txt` (opcional):
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o servidor Flask:
   ```bash
   python app.py
   ```

3. Execute o script para importar o JSON para o MongoDB:
   ```bash
   python parser.py
   ```

### Front-end (Vue.js)

1. Navegue até a pasta `client`:
   ```bash
   cd client
   ```

2. Instale as dependências do Node.js:
   ```bash
   npm install
   ```

3. Execute o servidor de desenvolvimento:
   ```bash
   npm run serve
   ```

## Estrutura do Projeto

- **app.py**: Back-end (Flask)
- **mongodb.py**: Conexão com MongoDB
- **parser.py**: Script para importar o JSON
- **client/**: Código do front-end (Vue.js)
- **udata.json**: Arquivo JSON com os dados dos usuários

