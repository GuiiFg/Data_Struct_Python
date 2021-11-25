from .node import Car


class Doubly_linked_list():
    
    def __init__ (self):

        self.__head = None
        self.__foot = None

        self.__size = 0
        self.__models = []
        self.__price = 0

    @property
    def size (self):
        return self.__size

    @size.setter
    def size (self, value):
        self.__size = value

    @property
    def models (self):
        return self.__models

    @models.setter
    def models (self, value):
        self.__models = value

    @property
    def price (self):
        return self.__price

    @price.setter
    def price (self, value):
        self.__price = value


    def insert_element(self, element:Car):

        pointer = self.__head

        if pointer != None:
            
            while (pointer.next):
                pointer = pointer.next
            
            element.prev = pointer
            pointer.next = element
            self.__foot = element

        else: 

            self.__head = element

        self.__size += 1
        self.__price += element.price
        self.__models.append(element.model)


    def print_front_to_back(self):
        
        if self.__size > 0:
            
            pointer = self.__head

            while pointer:

                print("\n")
                print(f"Model: {pointer.model}")
                print(f"Color: {pointer.color}")
                print(f"Licence plate: {pointer.licence_plate}")
                print(f"Km: {pointer.km}")
                print(f"Price: {pointer.price}")

                pointer = pointer.next

        else:
            print("Dont have nothing here!")

    def print_back_to_front(self):
        
        if self.__size > 0:
            
            pointer = self.__foot

            while pointer:

                print("\n")
                print(f"Model: {pointer.model}")
                print(f"Color: {pointer.color}")
                print(f"Licence plate: {pointer.licence_plate}")
                print(f"Km: {pointer.km}")
                print(f"Price: {pointer.price}")

                pointer = pointer.prev

        else:
            print("Dont have nothing here!")
