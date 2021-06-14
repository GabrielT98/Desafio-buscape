from typing import List


class produto():
    def __init__(self,id: int,name: str,images: List,value: float,installments: int,installmentValue: float):
        self.__id = id
        self.__name = name
        self.__images = []
        self.__value = value
        self.__installments = installments
        self.__installmentValue = installmentValue

    def get_id(self):
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

    def addImages(self,image):
        self.__images.append(image)
    
    def toDict(self):
        return {
            "id": self.get_id(),
            "name": self.get_name(),
            "images": self.get_images(),
            "price": {
                "value":self.get_value,
                "installments" : self.get_installments,
                "installmentValue" : self.get_installments_value
            }
        }
    
    

    