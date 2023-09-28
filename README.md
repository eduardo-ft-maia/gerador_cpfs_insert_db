# Gerador de CPFs Aleatórios Insert no Banco de Dados

Este é um script que a gera cps aleatórios, porém válios. Isto ajudará em ambientes de teste e homologação que possuem verificação se o cpf é válido ou não.

### Ambientação

Primeiramente, instale a dependência pyodbc para que o python conecte ao banco de dados com o seguinte comando:

```bash
pip install pyodbc
```

###Forma de Uso

```bash
Apenas altere as linhas de conexão com o banco de dados para o desejado:

connection_string = (
    "Driver={SQL Server};"
    "Server=SeuServer;" 
    "Database=SeuDB;"
    "UID=SeuLogin;"
    "PWD=SeuPassword;"
    )

```

```bash
Este é um projeto criado por Eduardo Maia

https://github.com/eduardo-ft-maia