from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from usuario import *
from vendedor import *
from produto import *

uri = "mongodb+srv://<username>:<password>@ecommerce.wmpyahq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

global db
db = client.EX2


opcao = 0
while(opcao != 'S'):
    print("\n1 - CRUD de Usuários")
    print("2 - CRUD de Vendedores")
    print("3 - CRUD de Produtos")
    opcao = input("Selecione uma opção. (S para sair) ").upper()

    acao = 0
    match opcao:
        case '1':
            while(acao != 'V'):
                print("\n --- CRUD de Usuários ---")
                print("1 - Cadastrar um novo usuário")
                print("2 - Excluir um usuário")
                print("3 - Listar todos os usuários")
                print("4 - Listar informações de um usuário")
                print("5 - Atualizar informações de um usuário")
                print("6 - Realizar uma compra")
                acao = input("Selecione uma ação. (V para voltar) ").upper()
                match acao:
                    case '1':
                        create_usuario(db)
                    case '2':
                        delete_usuario(db)
                    case '3':
                        read_all_usuario(db)
                    case '4':
                        read_usuario(db)
                    case '5':
                        update_usuario(db)
                    case '6':
                        compra_usuario(db)

        case '2':
             while(acao != 'V'):
                print("\n --- CRUD de Vendedores ---")
                print("1 - Cadastrar um novo vendedor")
                print("2 - Excluir um vendedor")
                print("3 - Listar todos os vendedores")
                print("4 - Listar informações de um vendedor")
                print("5 - Atualizar informações de um vendedor")
                acao = input("Selecione uma ação. (V para voltar) ").upper()
                match acao:
                    case '1':
                        create_vendedor(db)
                    case '2':
                        delete_vendedor(db)
                    case '3':
                        read_all_vendedor(db)
                    case '4':
                        read_vendedor(db)
                    case '5':
                        update_vendedor(db)
        case '3':
             while(acao != 'V'):
                print("\n --- CRUD de Produtos ---")
                print("1 - Cadastrar um novo produto")
                print("2 - Excluir um produto")
                print("3 - Listar todos os produtos")
                print("4 - Listar informações de um produto")
                print("5 - Atualizar informações de um produto")
                acao = input("Selecione uma ação. (V para voltar) ").upper()
                match acao:
                    case '1':
                        create_produto(db)
                    case '2':
                        delete_produto(db)
                    case '3':
                        read_all_produto(db)
                    case '4':
                        read_produto(db)
                    case '5':
                        update_produto(db)