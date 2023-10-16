def create_usuario(db):
    print('\nInsira as informações do usuário')
    cpf = input('CPF: ')
    nomeCompleto = input('Nome completo: ')

    enderecos = []
    keyEnderecos = 0
    while(keyEnderecos != 'N'):
        print('\nDigite seu endereço: ')
        rua = input('Rua: ')
        numero = input('Número: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')

        endereco = {
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }
        enderecos.append(endereco)
        keyEnderecos = input('\nDeseja inserir mais um endereço? S/N ').upper()

    contatos = {}
    contatos["telefones"] = []
    keyTelefones = 0
    while(keyTelefones != 'N'):
        telefone = input('DDD + Telefone: ')
        contatos["telefones"].append(telefone)
        keyTelefones = input('\nDeseja cadastrar mais um telefone? S/N ').upper()

    contatos["email"] = input('Email: ')
    senha = input('Senha: ')
    favoritos = []
    compras = []

    usuario = {"cpf": cpf, "nome": nomeCompleto, "enderecos": enderecos, "contatos": contatos, "senha": senha, "favoritos": favoritos, "compras": compras}
    
    mycol = db.Usuarios
    insert = mycol.insert_one(usuario)
    print(f'\nUsuário cadastrado no id: {insert.inserted_id}')
    return

def delete_usuario(db):
    cpf = input('\nDigite o cpf do usuário que deseja excluir: ')

    myquery = {"cpf": cpf}
    mycol = db.Usuarios

    mydoc = mycol.delete_one(myquery)
    print(f'Deletando o usuário {mydoc}')
    return

def read_usuario(db):
    cpf = input('\nDigite o cpf do usuário que deseja encontrar: ')

    mycol = db.Usuarios
    usuario = {"cpf": cpf}
    mydoc = mycol.find(usuario)

    usuarios = list(mydoc)

    if not usuarios:
        print('Não foram encontrados usuários com esse CPF')
    else:
        for usuario in usuarios:
            print("\nInformações do usuário:")
            print(f"CPF: {usuario['cpf']}")
            print(f"Nome: {usuario['nome']}")

            print("Endereços:")
            for endereco in usuario['enderecos']:
                print(f"\nRua: {endereco['rua']}")
                print(f"Número: {endereco['numero']}")
                print(f"Bairro: {endereco['bairro']}")
                print(f"Cidade: {endereco['cidade']}")
                print(f"Estado: {endereco['estado']}")

            print("\nContatos:")
            print(f"Email: {usuario['contatos']['email']}")
            print("Telefones:")
            for telefone in usuario['contatos']['telefones']:
                print(telefone)

            print("\nFavoritos:")
            for favorito in usuario['favoritos']:
                print(favorito)

            print("\nCompras:")
            for compra in usuario['compras']:
                print(compra)
    
    return

def update_usuario(db):
    cpf = input('\nDigite o cpf do usuário que deseja atualizar: ')

    mycol = db.Usuarios
    usuario = {"cpf": cpf}
    mydoc = mycol.find_one(usuario)

    if(mydoc):
        print(f'Editando informações de {mydoc["nome"]}. Aperte ENTER para pular um campo')
        nomeCompleto = input('Novo nome: ')
        if len(nomeCompleto):
            mydoc["nome"] = nomeCompleto

        keyUpdateEnderecos = input('\nDeseja atualizar os endereços? S/N ').upper()
        if(keyUpdateEnderecos == 'S'):
            keyOpcaoEnderecos = 0
            while(keyOpcaoEnderecos != 'C'):
                print('1 - Adicionar um endereço')
                print('2 - Remover um endereço existente')
                keyOpcaoEnderecos = input('Escolha uma opção: (C para cancelar) ').upper()

                match keyOpcaoEnderecos:
                    case '1':
                        endereco = {
                            "rua": input('Rua: '),
                            "numero": input('Numero: '),
                            "bairro": input('Bairro: '),
                            "cidade": input('Cidade: '),
                            "estado": input('Estado: ')
                        }

                        mydoc["enderecos"].append(endereco)
                        print('Endereço adicionado!\n')
                    case '2':
                        contadorEndereco = 1
                        for endereco in mydoc["enderecos"]:
                            print(f'\nEndereço {contadorEndereco}')
                            print(f"Rua: {endereco['rua']}")
                            print(f"Número: {endereco['numero']}")
                            print(f"Bairro: {endereco['bairro']}")
                            print(f"Cidade: {endereco['cidade']}")
                            print(f"Estado: {endereco['estado']}")

                            contadorEndereco+=1
                        
                        enderecoEscolhido = input('Escolha o endereço que você deseja remover: ')
                        if enderecoEscolhido.isdigit():
                            enderecoEscolhido = int(enderecoEscolhido)
                            if enderecoEscolhido > contadorEndereco:
                                print('Endereço inválido\n')
                            else:
                                mydoc["enderecos"].pop(enderecoEscolhido - 1)
                                print('Endereço removido!\n')
                        else:
                            print('Endereço inválido\n')

        keyUpdateTelefones = input('\nDeseja atualizar os telefones? S/N ').upper()
        if(keyUpdateTelefones == 'S'):
            keyOpcaoTelefones = 0
            while(keyOpcaoTelefones != 'C'):
                print('1 - Adicionar um telefone')
                print('2 - Remover um telefone existente')
                keyOpcaoTelefones = input('Escolha uma opção: (C para cancelar) ').upper()

                match keyOpcaoTelefones:
                    case '1':
                        novoTelefone = input('Digite o novo telefone (DDD + Número): ')
                        mydoc["contatos"]["telefones"].append(novoTelefone)
                        print('Telefone adicionado!')
                    case '2':
                        contadorTelefones = 1
                        for telefone in mydoc["contatos"]["telefones"]:
                            print(f'Telefone {contadorTelefones}')
                            print(telefone)

                            contadorTelefones+=1

                        telefoneEscolhido = input('Escolha o telefone que você deseja remover: ')
                        if telefoneEscolhido.isdigit():
                            telefoneEscolhido = int(telefoneEscolhido)
                            if telefoneEscolhido > contadorTelefones:
                                print('Telefone inválido\n')
                            else:
                                mydoc["contatos"]["telefones"].pop(telefoneEscolhido - 1)
                                print('Telefone removido!\n')
                        else:
                            print('Telefone inválido\n')

        email = input('Novo email: ')
        if len(email):
            mydoc["contatos"]["email"] = email
        
        novasInformacoes = {"$set": mydoc}
        mycol.update_one(usuario, novasInformacoes)
        print('\nInformações atualizadas com sucesso!')
    else:
        print("\nNão foram encontrados usuários com esse CPF")

    return