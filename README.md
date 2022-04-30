```bash
  _    _ _______ _______ _____     _____ ______ _______      ________ _____  
 | |  | |__   __|__   __|  __ \   / ____|  ____|  __ \ \    / /  ____|  __ \ 
 | |__| |  | |     | |  | |__) | | (___ | |__  | |__) \ \  / /| |__  | |__) |
 |  __  |  | |     | |  |  ___/   \___ \|  __| |  _  / \ \/ / |  __| |  _  / 
 | |  | |  | |     | |  | |       ____) | |____| | \ \  \  /  | |____| | \ \ 
 |_|  |_|  |_|     |_|  |_|      |_____/|______|_|  \_\  \/   |______|_|  \_\
```
### CE5320 - TÓPICOS AVANÇADOS DE REDES DE COMPUTADORES - CENTRO UNIVERSITÁRIO FEI
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Javascript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)
***

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="https://github.com/akajhon/HTTP_Sockets_Server/edit/main/README.md#1-introdu%C3%A7%C3%A3o-">Introdução</a>
    </li>
    <li>
      <a href="https://github.com/akajhon/HTTP_Sockets_Server/edit/main/README.md#2-rodando-localmente-">Rodando Localmente</a>
    </li>
    <li>
      <a href="https://github.com/akajhon/HTTP_Sockets_Server/edit/main/README.md#2-requisi%C3%A7%C3%A3o-via-linha-de-comando-">Requisição via linha de comando</a>
    </li>
    <li>
      <a href="https://github.com/akajhon/HTTP_Sockets_Server/edit/main/README.md#4-requisi%C3%A7%C3%A3o-via-cliente-web-">Requisição via cliente Web</a>
    </li>
    <li>
      <a href="https://github.com/akajhon/HTTP_Sockets_Server/edit/main/README.md#5-error-codes-">Códigos de Erro</a>
    </li>
    <li>
      <a href="https://github.com/akajhon/HTTP_Sockets_Server/edit/main/README.md#6-autores-">Autores</a>
    </li>
  </ol>
</details>

***

## 1. Introdução 📘
O projeto tem por objetivo a implementação de um servidor HTTP 1.1, capaz de
interpretar alguns comandos HTTP recebidos através de solicitações de navegadores e
solicitações via linha de comando. O servidor deve ser capaz de responder a essas
solicitações corretamente.

Os comandos implementados foram: GET, POST, PUT e DELETE. Durante a
implementação destes métodos, a RFC do protocolo HTTP 1.1 foi utilizada como base para
esclarecimentos. A linguagem Python foi utilizada para a implementação, valendo apenas do
módulo “sockets”.

Para a página HTML responsável pelas requisições, criou-se um livro de receitas,
onde é possível a Criação, Alteração, Deleção e Substituição de arquivos que serão criados
através das respectivas requisições no servidor recém-criado.

***

## 2. Rodando localmente 🏠

Clone o projeto

```bash
  git clone https://github.com/akajhon/HTTP_Sockets_Server
```

Entre no diretório do projeto

```bash
  cd HTTP_Sockets_Server
```

Inicie o servidor

```bash
  phyton3 servidorHTTP.py
```

Para acessar as páginas, basta digitar em seu navegador a seguinte URL: 

```bash
  http://localhost:8000/
```
ou através da linha de comando: 

```bash
  telnet localhost 8000
```

***

## 3. Requisição via linha de comando 👨‍💻

Para realizar uma requisição via linha de comando, deve-se usar o comando: `telnet localhost 8000`.

<p align="center">
  <img src="https://github.com/akajhon/HTTP_Sockets_Server/blob/main/images/cmd_client_post.png" alt="501" width="450" height="300"/>  <img src="https://github.com/akajhon/HTTP_Sockets_Server/blob/main/images/cmd_server_post.png" alt="501" width="450" height="300"/>
</p>

- [x] GET

Para executar uma requisição do tipo **GET**, deve-se executar o comando: `GET/index.html HTTP/1.1`. O servidor retornará o HTML da página requisitada no segundo parâmetro da requisição.Além disso, pode-se requisitar qualquer uma das páginas HTML existentes no servidor: put.html, post.html e delete.html . Caso o arquivo HTML não esteja presente no servidor, este retornará o conteúdo HTML da página **404 - File not Found**.

- [x] POST

Para executar uma requisição do tipo **POST**, deve-se executar o comando: `POST/arquivo.txt HTTP/1.1 {“key”: “receita”}`. Neste comando, o nome do arquivo que deseja ser alterado deverá ser passado como segundo parâmetro da requisição e o conteúdo do arquivo deve ser passado como um JSON ao fim da requisição. Este conteúdo será adicionado ao conteúdo existente no arrquivo(append). 

Caso o arquivo não exista no servidor, este será criado contendo o conteúdo passado no JSON (Apenas o texto após os “:”). Se a requisição for realizada contendo um conteúdo do JSON vazio, como por exemplo: `POST /arquivo.txt HTTP/1.1 {“key”: “”}` , o servidor retornará o conteúdo
HTML da página de erro **400 - Bad Request**.

- [x] PUT

Para executar uma requisição do tipo **PUT**, deve-se executar o comando: `PUT/arquivo.txt HTTP/1.1 {“key”: “receita”}` . Neste comando, o nome do arquivo que desejaser sobrescrito deverá ser passado como segundo parâmetro da requisição e o conteúdo a serescrito deve ser passado como um JSON ao fim da requisição. 

Caso o arquivo não exista no servidor, este será criado contendo o conteúdo passado no JSON (Apenas o texto após os “:”). Se a requisição for realizada contendo um conteúdo do JSON vazio, como por exemplo:        `PUT /arquivo.txt HTTP/1.1 {“key”: “”}` , o servidor retornará o conteúdo HTML da página de erro **400 - Bad Request**.

- [x] DELETE

Para executar uma requisição do tipo **DELETE**, deve-se executar o comando: `DELETE /arquivo.txt HTTP/1.1`. Neste comando, o nome do arquivo que deseja ser deletado do servidor deverá ser passado como segundo parâmetro da requisição. Caso o arquivo não exista no servidor, este retornará o conteúdo HTML da página de erro **404 - File not Found**.

***

## 4. Requisição via cliente Web 💻

Para acessar as paǵinas HTML, utilize a url: `http://localhost:8000/` .

- [x] GET

Para executar uma requisição do tipo **GET**, deve-se executar o comando: `http://localhost:8000/`. Ao acessá-la. O servidor retornará a página “index.html” devido à requisição GET realizada pelo navegador. A partir desta página é possível testar as outras requisições através dos respectivos botões presentes.

Caso o arquivo HTML solicitado na URL não esteja presente no servidor, este retornará a página de erro **404 - File not Found** .

<p align="center">
  <img src="https://github.com/akajhon/HTTP_Sockets_Server/blob/main/images/web_index.png" alt="501" width="600"/>
</p>

- [x] POST

Para executar uma requisição do tipo **POST**,
deve-se acessar a URL `http://localhost:8080/post.html`. Nesta página, o nome do arquivo que deseja ser alterado deverá ser escrito em "Nome da Receita:" e o conteúdo do arquivo deve ser passado em "Descrição:". Após o preenchimento de ambas caixas de entrada e pressionamento do botão "Alterar Receita!", o arquivo será enviado ao servidor. Se o arquivo não existir no servidor, este será criado contendo o conteúdo passado nas caixas de entrada da página. 

Caso o campo da descrição esteja vazio, o servidor retornará a página de erro **400 - Bad Request** .

<p align="center">
  <img src="https://github.com/akajhon/HTTP_Sockets_Server/blob/main/images/web_post.png" alt="501" width="600"/>
</p>

- [x] PUT

Para executar uma requisição do tipo **PUT**, deve-se acessar a URL `http://localhost:8080/put.html` . Nesta página, o nome do arquivo que deseja ser
sobrescrito deverá ser escrito em "Nome da Receita:" e o conteúdo do arquivo deve ser passado em "Descrição:". Após o preenchimento de ambas caixas de entrada e pressionado o botão "Adicionar Receita!", o arquivo será enviado ao servidor.

Caso o arquivo não exista no servidor, este será criado contendo o conteúdo passado nas caixas de entrada da página. Se o campo da descrição estiver vazio, o servidor retornará a página de erro **400 - Bad Request**.

<p align="center">
  <img src="https://github.com/akajhon/HTTP_Sockets_Server/blob/main/images/web_put.png" alt="501" width="600"/>
</p>

- [x] DELETE

Para executar uma requisição do tipo **DELETE**, deve se acessar a URL `http://localhost:8080/delete.html`. Nesta página, o nome do arquivo que será deletado do servidor deverá ser passado na caixa de entrada presente na página. Caso o arquivo não exista no servidor, este retornará a página de erro **404 - File not Found** .

<p align="center">
  <img src="https://github.com/akajhon/HTTP_Sockets_Server/blob/main/images/web_delete.png" alt="501" width="600"/>
</p>

***

## 5. Códigos de Erro ❌

- [x] Erro 501 - Not implemented 

Caso alguma outra requisição além das especificadas acima seja realizada pelo cliente, o servidor retornará a página de erro **501 - Not Implemented**, pois nenhum outro método além dos descritos foi implementado no servidor.

<p align="center">
  <img src="https://github.com/akajhon/HTTP_Sockets_Server/blob/main/images/501.png" alt="501" width="600"/>
</p>

- [x] Erro 400 - Bad Request

Caso haja algum problema com a requisição ou o conteúdo do campo da descrição do arquivo esteja vazio - `POST /arquivo.txt HTTP/1.1 {“key”: “”}`, este erro será retornado ao cliente.

<p align="center">
  <img src="https://github.com/akajhon/HTTP_Sockets_Server/blob/main/images/400.png" alt="400" width="600"/>
</p>

- [x] Erro 404 - File not Found 

Caso algum dos arquivos requisitados não esteja presente dentro do servidor, este erro será retornado ao cliente.

<p align="center">
  <img src="https://github.com/akajhon/HTTP_Sockets_Server/blob/main/images/404.png" alt="404" width="600"/>
</p>

***

## 6. Autores 🤖

| <img src="https://avatars.githubusercontent.com/u/62662399?v=4" alt="Murilo" width="150"/> | <img src="https://avatars.githubusercontent.com/u/69048604?v=4" alt="Joao" width="150"/> | <img src="https://avatars.githubusercontent.com/u/65295232?v=4" alt="Vitor" width="150"/> | <img src="https://avatars.githubusercontent.com/u/4358822?v=4" alt="Guilherme" width="150"/> |
|:-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [Murilo Gomes Munhoz](https://github.com/MuriloGomesMunhoz)                                 | [João Pedro Rosa Cezarino](https://github.com/akajhon)                                      | [Vitor Martins Oliveira](https://github.com/vihmar)                                         | [Guilherme Brigagão Cabelo](https://github.com/rmgg)                                       |
| R.A: 22.120.035-5                                                                           | R.A: 22.120.021-5                                                                           | R.A: 22.120.067-8                                                                           | R.A: 22.120.071-0                                                                          |
