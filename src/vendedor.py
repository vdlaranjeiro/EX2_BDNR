def create_vendedor(db):
    print('\nInsira as informações do vendedor')
    nome = input('Nome do vendedor ou da loja: ')

    verificacaoVendedor = 0
    while(verificacaoVendedor != 1):
        pessoaFisicaOuJuridica = input('Pessoa Física ou Jurídica? F/J ').upper()
        if(pessoaFisicaOuJuridica == 'F'):
            cpf = input('CPF: ')
            cnpj = ""
            verificacaoVendedor = 1
        elif(pessoaFisicaOuJuridica == 'J'):
            cnpj = input('CNPJ: ')
            cpf = ""
            verificacaoVendedor = 1
        else:
            print('Opção inválida. Selecione F para pessoa física ou J para pessoa jurídica.')

    enderecos = []
    keyEnderecos = 0
    while(keyEnderecos != 'N'):
        print('\nDigite seu endereço: ')
        cep = input('CEP: ')
        rua = input('Rua: ')
        numero = input('Número: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')

        endereco = {
            "cep": cep,
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

    vendedor = {
        "nome": nome,
        "cpf": cpf,
        "cnpj": cnpj,
        "enderecos": enderecos,
        "contatos": contatos,
        "senha": senha
    }

    mycol = db.Vendedores
    insert = mycol.insert_one(vendedor)
    print(f'\nVendedor cadastrado no id: {insert.inserted_id}')

    return

def delete_vendedor(db):
    cpfOuCnpj = input('Digite o cpf ou cnpj do vendedor que deseja excluir: ')

    myquery = {
        "$or": [
            {"cpf": cpfOuCnpj},
            {"cnpj": cpfOuCnpj}
        ]
    }

    mycol = db.Vendedores
    mydoc = mycol.delete_one(myquery)
    print(f'Deletando o usuário {mydoc}')
    return

def read_vendedor(db):
    cpfOuCnpj = input('Digite o cpf ou cnpj do vendedor que deseja encontrar: ')

    myquery = {
        "$or": [
            {"cpf": cpfOuCnpj},
            {"cnpj": cpfOuCnpj}
        ]
    }

    mycol = db.Vendedores
    mydoc = mycol.find(myquery)

    vendedores = list(mydoc)
    if not vendedores:
        print('Não foram encontrados vendedores com essas informações')
    else:
        for vendedor in vendedores:
            print("\nInformações do vendedor:")
            if len(vendedor["cpf"]):
                print(f'CPF: {vendedor["cpf"]}')
            if len(vendedor["cnpj"]):
                print(f'CPF: {vendedor["cnpj"]}')
            print(f"Nome: {vendedor['nome']}")

            print("Endereços:")
            for endereco in vendedor['enderecos']:
                print(f"\nCEP: {endereco['cep']}")
                print(f"Rua: {endereco['rua']}")
                print(f"Número: {endereco['numero']}")
                print(f"Bairro: {endereco['bairro']}")
                print(f"Cidade: {endereco['cidade']}")
                print(f"Estado: {endereco['estado']}")

            print("\nContatos:")
            print(f"Email: {vendedor['contatos']['email']}")
            print("Telefones:")
            for telefone in vendedor['contatos']['telefones']:
                print(telefone)

            queryProdutos = {"_idVendedor": vendedor["_id"]}
            mycol = db.Produtos
            mydoc = mycol.find(queryProdutos)
            produtos = list(mydoc)

            if produtos:
                print('\nProdutos deste vendedor: ')
                for produto in produtos:
                    print(f'Código: {produto["_id"]}')
                    print(f'Nome: {produto["nome"]}')
                    print(f'Valor: {produto["valor"]}\n')
            else:
                print('\nNão há produtos cadastrados nesse vendedor')
    return

def read_all_vendedor(db):
    colecaoVendedores = db.Vendedores
    vendedores = colecaoVendedores.find({}, {'nome': 1, "cpf": 1, "cnpj": 1, "_id": 0})

    vendedores = list(vendedores)

    if not vendedores:
        print("\nNão há vendedores cadastrados.")
    else:
        print("\nVendedores:")
        for usuario in vendedores:
            if len(usuario['cpf']): print(f"\nCPF: {usuario['cpf']}")
            if len(usuario['cnpj']): print(f"\nCNPJ: {usuario['cnpj']}")
            print(f"Nome: {usuario['nome']}")
    return

def update_vendedor(db):
    cpfOuCnpj = input('Digite o cpf ou cnpj do vendedor que deseja atualizar: ')

    mycol = db.Vendedores 
    myquery = {
        "$or": [
            {"cpf": cpfOuCnpj},
            {"cnpj": cpfOuCnpj}
        ]
    }
    mydoc = mycol.find_one(myquery)

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
                            "cep": input("CEP: "),
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
                            print(f"CEP: {endereco['cep']}")
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
        mycol.update_one(myquery, novasInformacoes)
        print('\nInformações atualizadas com sucesso!')
    else:
        print("\nNão foram encontrados usuários com esse CPF")
    return