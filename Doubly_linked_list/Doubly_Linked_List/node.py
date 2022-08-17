

class Car():

    def __init__(self, model, licence_plate, price, color, km):

        self.__next = None
        self.__prev = None

        self.__model = model
        self.__licence_plate = licence_plate
        self.__price = price
        self.__color = color
        self.__km = km

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @property
    def model(self):
        return self.__model

    @property
    def licence_plate(self):
        return self.__licence_plate

    @property
    def price(self):
        return self.__price

    @property
    def color(self):
        return self.__color

    @property
    def km(self):
        return self.__km

    @model.setter
    def model(self, value):
        self.__model = value

    @licence_plate.setter
    def licence_plate(self, value):
        self.__licence_plate = value

    @price.setter
    def price(self, value):
        self.__price = value

    @color.setter
    def color(self, value):
        self.__color = value

    @km.setter
    def km(self, value):
        self.__km = value

    @next.setter
    def next(self, value):
        self.__next = value

    @prev.setter
    def prev(self, value):
        self.__prev = value
