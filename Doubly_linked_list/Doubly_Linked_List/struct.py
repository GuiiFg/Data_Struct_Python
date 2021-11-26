from .node import Car


class Doubly_linked_list():
    
    def __init__ (self):

        self.__head = None
        self.__foot = None

        self.__size = 0
        self.__models = []
        self.__price = 0

    def __len__ (self):
        return self.__size

    @property
    def models (self):
        return self.__models

    @property
    def price (self):
        return self.__price


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

        if element.model not in self.__models:
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

    def delete_by_licence_plate(self, licence_plate:str):
        
        if self.__size > 0:
            
            pointer = self.__head

            counter = 0

            while pointer:

                if pointer.licence_plate == licence_plate:
                    
                    prev = pointer.prev
                    next = pointer.next

                    prev.next = next
                    next.prev = prev

                    self.__size -= 1

                    break

                if counter > self.__size:
                    print("Licence plate not found")
                    break

                pointer = pointer.next
                counter += 1

        else:
            print("Dont have nothing here!")

    
