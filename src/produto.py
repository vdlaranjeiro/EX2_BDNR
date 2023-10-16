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

    ultimoId = db.Produtos.find_one({"_id": 1}) 
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