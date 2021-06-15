from typing import List
from application.model.entily.produto import Produto
import json

class ProdutoDAO():
        def __init__(self):
            produto1 = Produto(2321312, "Smartphone Apple iPhone 7 128GB","https://images-americanas.b2w.io/produtos/01/00/img/132248/6/132248690_1GG.jpg", 3509.10, 10, 389.90)
            produto2 = Produto(9971, "Smart TV Samsung Série 4 UN32J4300AG 32 polegadas LED Plana", "https://http2.mlstatic.com/D_NQ_NP_703823-MLB25664575985_062017-O.jpg", 1139.90, 10, 134.11)
            produto3 = Produto(6717131, "Câmera Digital Canon EOS Rebel T5i 18.0 Megapixels", "https://images2.kabum.com.br/produtos/fotos/60822/60822_1422006565_g.jpg", 1999.20, 10, 235.20)
            produto4 = Produto(6717132, "Lenovo IdeaPad 310 80UH0004BR Intel Core i7-6500U 2.5 GHz 8192 MB 1024 GB", "https://a-static.mlcdn.com.br/600x600/notebook-15-6pol-lenovo-ideapad-310-core-i7-6th-gen-8gb-ddr4-hd-1tb-geforce-920mx-win-10-home-80uh0004br-prata/wazhardwarestore/113990/32497e64c4cb8764a28f88359e2b4908.jpg", 2599.00, 10, 259.90)
              
            self.produtos = [produto1,produto2,produto3,produto4]
            self.carrinho = []

        def listar_todos_produtos(self):
            return self.produtos

        def listar_todo_carrinho(self):
            return self.carrinho
            
'''
        def listar(self):
            result = []
            with open('buscape.json','r') as file:
                produto_list = json.load(file)
                result = self.converter_dictlist_produtolist(produto_list)
            return result
        ###receber o json e instanciar todos os produtos presentes no arquivo e transforma em lista   
        def converter_dictlist_produtolist(self, arquivo) -> List[Produto]:
            result = []
            for produto_dict in produto_list:
               produto = Produto()
               produto.set_id(produto_dict['id'])
               produto.set_name(produto_dict['name'])
               produto.addImages(produto_dict['images'])
               produto.set_value(produto_dict['value'])
               produto.set_installments(produto_dict['installments'])
               produto.set_installmentValue(produto_dict['installmentValue']) 
               result.append(produto)
            return result
'''
