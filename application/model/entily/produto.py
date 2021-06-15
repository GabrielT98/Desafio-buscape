from typing import List


class Produto():
    def __init__(self,id,name,imagens,value,installments,installmentValue):
        self.__id = id
        self.__name = name
        self.__images = imagens
        self.__value = value
        self.__installments = installments
        self.__installmentValue = installmentValue

    def get_id(self) :
        return self.__id
    def get_name(self):
        return self.__name
    def get_images(self):
        return self.__images
    def get_value(self):
        return self.__value
    def get_installments(self):
        return self.__installments
    def get_installments_value(self):
        return self.__installmentValue
