from typing import List
from application.model.entily.produto import Produto
class Carrinho():
    def __init__(self):
        self.__produtos = List[Produto]
    
    def get_produtos(self):
        return self.__produtos
        
    def add_produto_carrinho(self,produto:Produto):
        self.__produtos.append(produto)
    
    