O presente projeto visa atender aos requisitos do desafio lógico proposto pelo programa de Trainee Biopark.

```sql
Para isso é necessário criar o banco de dados MySQL.
CREATE TABLE `tblCommunication` (
`Id` int(11) NOT NULL AUTO_INCREMENT,
`Title` varchar(45) NOT NULL,
`Date` date NOT NULL,
`Time` varchar(45) NOT NULL,
`Description` TEXT,
`Means` varchar(45),
PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```
