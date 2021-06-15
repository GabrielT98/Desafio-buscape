from typing import List


from application.model.entily.carrinho import Carrinho
from application.model.entily.produto import Produto
class CarrinhoDAO():
    def __init__(self):

        self.produtos_carrinho = []

    def adicionar_produto_carrinho(self,Produto):
        self.produtos_carrinho.append(Produto)

    def remover_produto_carrinho(self,Produto):
        self.produtos_carrinho   
    def listar_carrinho(self) ->List[Carrinho]:
            return self.__produtos_carrinho
            