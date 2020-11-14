O presente projeto visa atender aos requisitos do desafio Tech proposto pelo programa de Trainee Biopark.

Para isso é necessário criar o banco de dados MySQL.
```sql
CREATE DATABASE Communication;
USE Communication;

CREATE TABLE `tblCommunication` (
`Id` int NOT NULL AUTO_INCREMENT,
`Title` varchar(120) NOT NULL,
`Description` text,
`Date` date NOT NULL,
`Time` time NOT NULL,
`Means` varchar(60),
PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```
