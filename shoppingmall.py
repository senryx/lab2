from client import Client, ClientList
from product import Product, ProductList
from orders import Orders, OrdersList

import os.path
import json

class Shoppingmall:
    """Класс агрегирует в себе список клиентов, продуктов и заказов."""
    def __init__(self, file_name=""):
        self.__clients = ClientList()
        self.__products = ProductList()
        self.__orderses = OrdersList()

        if file_name != "":
            self.read(file_name)

    def read(self, file_name):
        with open(file_name) as file_input:
            data = json.load(file_input)

        for item in data["client"]:
            client = Client(item["id"], item["name"], item["address"],
                          item["phonenumber"])
            self.__clients.append(client)

        for item in data["product"]:
            product = Product(item["id"], item["price"],
                       item["delivery"], item["description"])
            self.__products.append(product)

        for item in data["orders"]:
            orderses = []
            for id in item["orderses"]:
                orderses.append(self.__orderses.getByID(id))

            orders = Orders(item["id"], item["client"], item["product"], item["amount"], item["date"],
                        orders)
            self.__orderses.append(orders)

    def write(self, file_name):
        if not os.path.exists(file_name):
            data = {}
        else:
            with open(file_name) as file_input:
                data = json.load(file_input)

        data["client"] = []
        for item in self.__clients:
            client= {
                "id": item.getID(),
                "name": item.get_name(),
                "address": item.get_address(),
                "phonenumber": item.get_phonenumber(),
            }
            data["client"].append(client)

        data["product"] = []
        for item in self.__products:
            product = {
                "id": item.getID(),
                "get_delivery": item.get_delivery(),
                "description": item.get_description(),
                "contract_value": item.getContractValue()
            }
            data["product"].append(product)

        data["orders"] = []
        for item in self.__orderses:
            orderses = {
                "id": item.getID(),
                "name": item.get_client_name(),
                "product": item.get_product(),
                "amount": item.get_amount(),
                "date": item.get_date(),
                "amount": [orders.getID() for orders in item.getOrders()]
            }
            data["orderses"].append(orderses)

        with open(file_name, "w") as file_output:
            json.dump(data, file_output)

    def print(self):
        print("===Клиенты===")
        for item in self.__clients:
            print(item, "\n")

        print("===Продукты===")
        for item in self.__products:
            print(item, "\n")

        print("===Заказы===")
        for item in self.__orderses:
            print(item, "\n")
