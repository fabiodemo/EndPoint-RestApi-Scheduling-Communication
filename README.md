# API Communication - Desafio Tech #


## Descrição ##
O presente projeto visa atender aos requisitos do desafio Tech proposto pelo programa de Trainee Biopark.
A plataforma deverá possuir:
- Um endpoint que receba uma solicitação de agendamento de envio de comunicação.
- Outro endpoint para realização de consulta do status do agendamento de envio de comunicação.
- Deve haver também um endpoint para remoção de agendamento de envio de comunicação.
Para facilitar o uso, na presente implementação as endpoints para consulta e deletar agendamentos foram unidas em um só, de forma que após realizar a busca o agendamento possa ser conferido, e caso não seja necessário ou esteja errado possa ser deletado.


## Banco de Dados ##

Para esta implementação, é necessário criar banco de dados MySQL descrito abaixo. A tabela criada foi estabelecida de forma a dispor as informações em JSON da melhor forma possível.
```sql
CREATE DATABASE Communication;
USE Communication;

CREATE TABLE `tblCommunication` (
`Id` int NOT NULL AUTO_INCREMENT,
`Title` varchar(120) NOT NULL,
`Recipient` text,
`Description` text,
`Date` date NOT NULL,
`Time` time NOT NULL,
`Means` varchar(60),
PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```


## Requisitos ##

A API rodará em Python (versão 3.x), e como pré-requisitos para isso, será necessário instalar o arquivo "requirements.txt" através do pip, usando o seguinte comando:
```
$ pip3 install -r requirements.txt
```
Deve-se a alterar também os campos de usuário e senha deste usuário, para acessar o banco de dados, que estão contidos no script "api.py"
```python
app.config['MYSQL_DATABASE_USER'] = 'seuUsuario'
app.config['MYSQL_DATABASE_PASSWORD'] = 'suaSenha'
```


## Execução ##

Por fim, após ter seguido todos os passos acima, basta rodar o script "api.py" para executar a aplicação,.
```
$ python3 api.py
```


## Licença e Distribuição ##

Veja o arquivo [LICENSE](LICENSE) para verificar os direitos de uso e distribuição desta API (GNU GPL v3).
