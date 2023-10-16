from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from usuario import *
from vendedor import *
from produto import *

uri = "mongodb+srv://viniciuslaranjeiro:senhateste@ecommerce.wmpyahq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

global db
db = client.Ecommerce


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
                print("3 - Listar informações de um usuário")
                print("4 - Atualizar informações de um usuário")
                acao = input("Selecione uma ação. (V para voltar) ").upper()
                match acao:
                    case '1':
                        create_usuario(db)
                    case '2':
                        delete_usuario(db)
                    case '3':
                        read_usuario(db)
                    case '4':
                        update_usuario(db)

        case '2':
             while(acao != 'V'):
                print("\n --- CRUD de Vendedores ---")
                print("1 - Cadastrar um novo vendedor")
                print("2 - Excluir um vendedor")
                print("3 - Listar informações de um vendedor")
                print("4 - Atualizar informações de um vendedor")
                acao = input("Selecione uma ação. (V para voltar) ").upper()
                match acao:
                    case '1':
                        create_vendedor(db)
                    case '2':
                        delete_vendedor(db)
                    case '3':
                        read_vendedor(db)
                    case '4':
                        update_vendedor(db)
        case '3':
             while(acao != 'V'):
                print("\n --- CRUD de Produtos ---")
                print("1 - Cadastrar um novo produto")
                print("2 - Excluir um produto")
                print("3 - Listar informações de um produto")
                print("4 - Atualizar informações de um produto")
                acao = input("Selecione uma ação. (V para voltar) ").upper()
                match acao:
                    case '1':
                        create_produto(db)
                    case '2':
                        delete_vendedor(db)
                    case '3':
                        read_vendedor(db)
                    case '4':
                        update_vendedor(db)