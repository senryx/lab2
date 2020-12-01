class Product:
    def __init__(self, id,  price, delivery, description):
        self.__id = id
        self.__price = price
        self.__delivery = delivery
        self.__description = description

    def set_id(self, id):
        self.__id = id

    def set_price(self, price):
        self.__price = price

    def set_delivery(self, delivery):
        self.__delivery = delivery

    def set_description(self, description):
        self.__description = description

    def get_id(self):
        return self.__id

    def get_price(self):
        return self.__price

    def get_delivery(self):
        return self.__delivery

    def get_description(self):
        return self.__description

    def get_product(self):
        print(
            f"price: {self.__price}\ndelivery: {self.__delivery}\namount: {self.__description}"
        )

class ProductList(list):
    """Список, специализированный для хранения объектов класса Product."""
    def getByID(self, id):
        for item in self:
            if item.get_id() == id:
                return item
            else:
                return None
