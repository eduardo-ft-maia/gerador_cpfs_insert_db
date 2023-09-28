import random
import pyodbc

def insert_cpf():
    connection_string = (
    "Driver={SQL Server};"
    "Server=SeuServer;" 
    "Database=SeuDB;"
    "UID=SeuLogin;"
    "PWD=SeuPassword;"
    )

    try:

        # Conecta
        conn = pyodbc.connect(connection_string)

        # Cria um cursor
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM dbo.Pessoa WHERE cpf IS NULL OR cpf = ''")
        rows_to_insert = cursor.fetchall()


        for row in rows_to_insert:
            new_cpf = gerar_cpf()
            
            # Update o CPF
            update_query = "UPDATE dbo.Pessoa SET cpf = ? WHERE id = ?"
            data_to_update = (new_cpf, row.id)  # get row por id
            cursor.execute(update_query, data_to_update)
        
        # Commit as mudanças
        conn.commit()

        print("CPFs inseridos com sucesso!")


    except pyodbc.Error as e:
        print(f"Erro: {e}")

    finally:
        # Fecha o cursor
        cursor.close()
        conn.close()


# Gera cpf aleatorio, mas valido
def gerar_cpf():
    multiplicador1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicador2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    semente = str(random.randint(100000000, 999999999))

    soma = 0
    for i in range(9):
        soma += int(semente[i]) * multiplicador1[i]

    resto = soma % 11
    if resto < 2:
        resto = 0
    else:
        resto = 11 - resto

    semente += str(resto)
    soma = 0

    for i in range(10):
        soma += int(semente[i]) * multiplicador2[i]

    resto = soma % 11

    if resto < 2:
        resto = 0
    else:
        resto = 11 - resto

    semente += str(resto)
    return semente

insert_cpf()