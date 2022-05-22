import pyodbc

dados_conexao = (
    "driver={sql server};"
    "server=DESKTOP-9A47LMA\sqlexpress;"
    "database=brk_sql;")

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")

cursor = conexao.cursor()


comando_acesso = "SELECT * FROM Usuario"
cursor = conexao.cursor()
cursor.execute(comando_acesso)
linhas= cursor.fetchall()
idlogin= linhas [0][1]
idsenha=linhas [0][5]



certificar3 = "SELECT * FROM automovel"
cursor = conexao.cursor()
cursor.execute(certificar3)
linhas= cursor.fetchall()
placa2= certificar3




contatos = {}
automovel = {}
x = 0


print ("Bem vindo ao sistema de Logistica-BRK")

while x == 0:
    acesso= int(input ("Digite a opção desejada:\n01. Acessar com cadastro\n02. Realizar novo cadastro\n03. Sair\nR:"))

    while acesso > 3 or acesso < 1:
        print("Você digitou uma opção inválida")
        acesso= int(input ("Digite a opção desejada:\n01. Acessar com cadastro\n02. Realizar novo cadastro\n03. Sair\nR:"))

    if acesso ==1:
        from getpass import getpass
        login_acesso = input("Login: ")
        senha_acesso = getpass("Senha: ")
        if login_acesso == idlogin and senha_acesso == idsenha:
            print("Acessando")
        while idlogin != login_acesso and idsenha !=senha_acesso:
            print("Login ou senha inválidos")
            acesso = int(input ("Digite a opção desejada:\n01. Acessar com cadastro\n02. Realizar novo cadastro\n03.Sair\nR:"))
            if acesso == 1:
                from getpass import getpass
                login_acesso = input ("Login: ")
                senha_acesso = getpass ("Senha: ")
            if idlogin == login_acesso and idsenha==senha_acesso:
                print ("Acessando")
                continue

    elif acesso == 2:

        print ("Criar novo cadastro.")
        while True: 
            email = input("E-mail: ")
            if email == "":
                print("Espaço vazio! Digite um email: ")
            else:
                break
      
        while True: 
            login= input ("Login de acesso: ")
            if login == "":
                print("Espaço vazio! Digite um login: ")
            else:
                break

        while True: 
            nome = input("Nome: ").strip()
            if nome == "":
                print("Espaço vazio! Digite um nome: ")
            else:
                break
        
        while True: 
            sobrenome =  input("Sobrenome: ").strip()
            if sobrenome == "":
                print("Espaço vazio! Digite um sobrenome: ")
            else:
                break
        
        while True: 
            nascimento = input ("Data de nascimento: ")
            if nascimento == "":
                print("Espaço vazio! Digite uma data de nascimento: ")
            else:
                break
        
        while True: 
            senha = input ("Senha do usuário: ")
            if senha == "":
                print("Espaço vazio! Digite uma senha: ")
            else:
                break
        
        while True: 
            senha2 = input ("Confirme sua senha: ")
            if senha2 == "":
                print("Espaço vazio! Digite a senha novamente: ")
            else:
                break
        
        
        while True: 
            telefone = input ("Telefone: ")
            if telefone == "":
                print("Espaço vazio! Digite um telefone: ")
            else:
                break

        if senha == senha2:
        
            comando = f"""INSERT INTO Usuario (id_email, id_login, nome, sobrenome, nascimento, senha, telefone)
            VALUES
                ('{email}', '{login}', '{nome}', '{sobrenome}', '{nascimento}', '{senha}', {telefone})"""
            cursor.execute(comando)
            cursor.commit()
            print ("Usuario cadastrado com sucesso.")

        else:
            print("Senhas não coincidem. Insira novamente")

            while True: 
                senha = input ("Senha do usuário: ")
                if senha == "":
                    print("Espaço vazio! Digite uma senha: ")
                else:
                    break
        
            while True: 
                senha2 = input ("Confirme a senha do usuário: ")
                if senha2 == "":
                    print("Espaço vazio! Digite a senha novamente: ")
                else:
                    print("Usuario cadastrado com sucesso.")
                    comando = f"""INSERT INTO Usuario (id_email, id_login, nome, sobrenome, nascimento, senha, telefone)
                    VALUES
                        ('{email}', '{login}', '{nome}', '{sobrenome}', '{nascimento}', '{senha}', {telefone})"""
                    cursor.execute(comando)
                    cursor.commit()
                    break
                    
            
        contatos [login.upper()] = {"nome": nome,
        "sobrenome": sobrenome,
        "e-mail": email,
        "data de nascimento": nascimento,
        "login": login,
        "telefone": telefone,

            }

    elif acesso == 3:
        cursor.close()
        conexao.close()
        print("Conexão ao MySQL foi encerrada")
        break

    print ("Seja bem vindo!")
    certificar3 = "SELECT * FROM automovel"
    cursor = conexao.cursor()
    cursor.execute(certificar3)
    linhas= cursor.fetchall()
    placa2 = certificar3

    menu = int(input ("Digite a opção desejada:\n01. Adicionar automoveis\n02. Meus automoveis\n03. Sair\nR:"))

    while menu > 3 or menu < 1:
        print("Você digitou uma opção inválida")
        menu = int(input ("Digite a opção desejada:\n01. Adicionar automoveis\n02. Meus automoveis\n03. Sair\nR:"))

    if menu == 1:

        print ("Adicionar automovel.")

        while True: 
            ano = input("Ano do automovel: ")
            if ano == "":
                print("Espaço vazio! Digite o ano do veiculo: ")
            else:
                break

        while True: 
            placa= input ("Placa do automovel: ").strip()
            if placa == "":
                print("Espaço vazio! Digite a placa do veiculo: ")
            else:
                break

        while True: 
            modelo = input("Modelo: ").strip()
            if modelo == "":
                print("Espaço vazio! Digite o modelo do veiculo: ")
            else:
                break
        
        while True: 
            cor =  input("Cor: ").strip()
            if cor == "":
                print("Espaço vazio! Digite a cor do veiculo: ")
            else:
                break

        if placa == placa2 :
            print("Placa já registrada. Insira novamente")
            while True: 
                placa= input ("Placa do automovel: ").strip()
                if placa == "":
                    print("Espaço vazio! Digite a placa do veiculo: ")
                else:
                    break
            

        else:
            comando2 = f"""INSERT INTO automovel (ano, placa, modelo, cor)
            VALUES
                ({ano}, '{placa}', '{modelo}', '{cor}')"""
            cursor.execute(certificar3)
            cursor.commit()
            print ("Automovel cadastrado com sucesso.")

        automovel [modelo.upper()] = {"ano do automovel": ano,
        "placa do automovel": placa,
        "modelo do automovel": modelo,
        "cor do automovel": cor,

            }
    elif menu ==2:
        print(automovel)

    elif menu ==3:
        cursor.close()
        conexao.close()
        print("Conexão ao MySQL foi encerrada")
        break