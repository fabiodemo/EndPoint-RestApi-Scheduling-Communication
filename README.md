# API Communication - Desafio Tech #
### Autor: Fábio Demo da Rosa ###

## Descrição ##
O presente projeto visa atender aos requisitos do desafio Tech proposto pelo programa de Trainee Biopark.
A plataforma deverá possuir:
- Um endpoint que receba uma solicitação de agendamento de envio de comunicação.
- Outro endpoint para realização de consulta do status do agendamento de envio de comunicação.
- Deve haver também um endpoint para remoção de agendamento de envio de comunicação.
Para facilitar o uso, na presente implementação as endpoints para consulta e deletar agendamentos foram unidas em um só, de forma que após realizar a busca o agendamento possa ser conferido, e caso não seja necessário ou esteja errado possa ser deletado.
A API foi desenvolvida em Python (versão 3.8.5), devido ao maior conhecimento da linguagem e sua fácil aplicação do Flask-Restful. Além das diversas possibilidades que esta linguagem de alto nível oferece.

## Requisitos ##

Como pré-requisitos para rodar, será necessário instalar o arquivo "requirements.txt" através do pip3, usando o seguinte comando:
```
$ pip3 install -r requirements.txt
```
Deve-se a alterar também os campos de usuário e senha de acesso ao banco de dados, que estão contidos no script "api.py", para que o script tenha acesso ao banco de dados e salve as alterações feitas na endpoint.
```python
app.config['MYSQL_DATABASE_USER'] = 'seuUsuario'
app.config['MYSQL_DATABASE_PASSWORD'] = 'suaSenha'
```
### Banco de Dados ###

Para esta implementação, é necessário criar o banco de dados MySQL descrito abaixo. A tabela criada foi estabelecida de forma a dispor as informações em JSON da melhor forma possível. Observação: a data do banco de dados está em formato (yyyy-mm-dd), enquanto a data das requisições está em formato (mm-dd-yyy).
```sql
CREATE DATABASE Communication;
USE Communication;

CREATE TABLE `tblCommunication` (
`Id` int NOT NULL AUTO_INCREMENT,
`Title` varchar(120) NOT NULL,
`Recipient` text NOT NULL,
`Description` text,
`Date` date NOT NULL,
`Time` time NOT NULL,
`Means` varchar(60),
PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```


## Execução ##

Por fim, após ter seguido todos os passos acima, basta rodar o script "api.py" para executar a aplicação,.
```
$ python3 api.py
```
### Testes ###
Para realizar testes, basta aceder aos endereços:
- http://127.0.0.1:8080/CreateEvent (para criar um agendamento de envio de comunicação);
- http://127.0.0.1:8080/GetEvent (para realizar uma consulta de agendamento de envio de comunicação).

Um outra alternativa para realizar os testes, pode ser através do Client URL (Curl). Para isso, basta acessar o arquivo Curl, o qual possui algumas requisições HTTP pré-preenchidas, e para executá-las basta copiar cada parágrafo contido no arquivo [Curl.txt](curl.txt).


## Licença e Distribuição ##

Veja o arquivo [LICENSE](LICENSE) para verificar os direitos de uso e distribuição desta API (GNU GPL v3).
