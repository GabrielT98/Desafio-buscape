from typing import List
from application.model.entily.produto import Produto
import json

class ProdutoDAO():
        def __init__(self):
            produto1 = Produto(2321312, "Smartphone Apple iPhone 7 128GB", "http://thumbs.buscape.com.br/celular-e-smartphone/smartphone-apple-iphone-7-128gb_600x600-PU98460_1.jpg", 3509.10, 10, 389.90)
            produto2 = Produto(9971, "Smart TV Samsung Série 4 UN32J4300AG 32 polegadas LED Plana", "http://mthumbs.buscape.com.br/tv/smart-tv-samsung-serie-4-un32j4300ag-32-polegadas-led-plana_600x600-PU95547_1.jpg", 1139.90, 10, 134.11)
            produto3 = Produto(6717131, "Câmera Digital Canon EOS Rebel T5i 18.0 Megapixels", "http://mthumbs.buscape.com.br/camera-digital/canon-eos-rebel-t5i-18-0-megapixels_600x600-PU7bf7b_1.jpg", 1999.20, 10, 235.20)
            produto4 = Produto(6717132, "Lenovo IdeaPad 310 80UH0004BR Intel Core i7-6500U 2.5 GHz 8192 MB 1024 GB", "http://mthumbs.buscape.com.br/notebook/lenovo-ideapad-310-80uh0004br-intel-core-i7-6500u-2-5-ghz-8192-mb-1024-gb_600x600-PU98e6e_1.jpg", 2599.00, 10, 259.90)
            
            self.produtos = [produto1,produto2,produto3,produto4]
        def listar_todos_produtos(self) -> List[Produto]:
            return self.produtos


        #result = []
       # with open('buscape.json','r') as file:
        ##    produto_list = json.load(file)
#result = self.converter_dictlist_produtolist(produto_list)
      #  return result
            
  #  def converter_dictlist_produtolist(self, produto_list) -> List[Produto]:
  ###      result = []
  #      for produto_dict in produto_list:
  #          produto = Produto()
   #         produto.set_id(produto_dict['id'])
   #         produto.set_name(produto_dict['name'])
  ##          produto.addImages(produto_dict['images'])
   #         produto.set_value(produto_dict['value'])
   #         produto.set_installments(produto_dict['installments'])
   #         produto.set_installmentValue(produto_dict['installmentValue']) 
   #         result.append(produto)
   #     return result


