def create_produto(db):
    print('\nInsira as informações do produto')
    nome = input('Nome: ')
    descricao = input('Descrição: ')

    validacaoValor = 0
    while(validacaoValor != 1):
        valor = input('Valor: ')
        try:
            valor = float(valor)
            validacaoValor = 1
        except ValueError:
            print('Insira um valor válido')
    
    validacaoQuantidade = 0
    while(validacaoQuantidade != 1):
        quantidade = input('Quantidade disponível: ')
        if(quantidade.isnumeric()):
            quantidade = int(quantidade)
            validacaoQuantidade = 1
        else:
            print('Insira um valor válido')
    
    verificacaoVendedor = 0
    while(verificacaoVendedor != 1):
        cpfOuCnpj = input('\nDigite o cpf ou cnpj do vendedor: ')
        colunaVendedores = db.Vendedores 
        myquery = {
            "$or": [
                {"cpf": cpfOuCnpj},
                {"cnpj": cpfOuCnpj}
            ]
        }
        vendedor = colunaVendedores.find_one(myquery)
        if(vendedor):
            verificacaoVendedor = 1
        else:
            print('Não foram encontrados vendedores com essas informações')

    ultimoId = db.Produtos.find_one(sort=[("_id", -1)]) 
    if not(ultimoId):
        produto = {
            "_id": 1,
            "_idVendedor": vendedor["_id"],
            "nome": nome,
            "descricao": descricao,
            "valor": valor,
            "quantidade": quantidade
        }

        insert = db.Produtos.insert_one(produto)
        print(f'\nProduto cadastrado no id: {insert.inserted_id}')
    else:
        produto = {
            "_id": ultimoId["_id"] + 1,
            "_idVendedor": vendedor["_id"],
            "nome": nome,
            "descricao": descricao,
            "valor": valor,
            "quantidade": quantidade
        }

        insert = db.Produtos.insert_one(produto)
        print(f'\nProduto cadastrado no id: {insert.inserted_id}')

    return

def delete_produto(db):
    idProduto = int(input('\nDigite o código do produto que deseja excluir: '))

    myquery = {"_id": idProduto}
    mycol = db.Produtos

    mydoc = mycol.delete_one(myquery)
    print(f'Deletando o produto {mydoc}')
    return

def read_produto(db):
    idProduto = int(input('\nDigite o código do produto que deseja encontrar: '))

    myquery = {"_id": idProduto}
    mycol = db.Produtos

    mydoc = mycol.find_one(myquery)

    if not (mydoc):
        print('Não foram encontrados produtos com esse código.')
    else:
        print("\nInformações do produto:")
        print(f'Código: {mydoc["_id"]}')
        print(f'Nome: {mydoc["nome"]}')
        print(f'Descrição: {mydoc["descricao"]}')
        print(f'Valor: {mydoc["valor"]}')
        print(f'Quantidade disponível: {mydoc["quantidade"]}')
    
    return

def update_produto(db):
    idProduto = int(input('\nDigite o código do produto que deseja atualizar: '))

    myquery = {"_id": idProduto}
    mycol = db.Produtos

    mydoc = mycol.find_one(myquery)

    if not(mydoc):
        print('Não foram encontrados produtos com esse código')
    else:
        print(f'Editando informações do produto {mydoc["_id"]} - {mydoc["nome"]}. Aperte ENTER para pular um campo')
        nome = input('Nome: ')
        if len(nome):
            mydoc["nome"] = nome
        
        descricao = input('Descrição: ')
        if len(descricao):
            mydoc["descricao"] = descricao
        
        valor = input('Valor: ')
        if len(valor):
            validacaoValor = 0
            while(validacaoValor != 1):
                try:
                    mydoc["valor"] = float(valor)
                    validacaoValor = 1
                except ValueError:
                    valor = input('Insira um valor válido: ')
        quantidade = input('Quantidade: ')
        if len(quantidade):
            validacaoQuantidade = 0
            while(validacaoQuantidade != 1):
                if(quantidade.isnumeric()):
                    mydoc["quantidade"] = int(quantidade)
                    validacaoQuantidade = 1
                else:
                    quantidade = input('Insira uma quantidade válida: ')

        novasInformacoes = {"$set": mydoc}
        mycol.update_one(myquery, novasInformacoes)
        print('\nInformações atualizadas com sucesso!')

    return