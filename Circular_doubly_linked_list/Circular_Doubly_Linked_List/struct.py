
from .node import Person

class Circular_Doubly_Linked_List():

    def __init__(self):

        self.__head = None

        self.__size = 0

    def __len__(self):
        return self.__size

    def insert_element(self, name, age, cpf):
        
        new_element = Person(name, age, cpf)

        if self.__head:

            pointer = self.__head

            if pointer.next != None:
                while pointer.next != self.__head:
                    pointer = pointer.next

            new_element.prev = pointer
            new_element.next = self.__head
            pointer.next = new_element
            
            
        else:

            self.__head = new_element

        self.__size += 1

    def Show_all(self, properties:list = None):

        if self.__size > 0:

            pointer = self.__head


            while True:

                if properties != None:

                    if "name" in properties:
                        print(f"Name: {pointer.name}")
                    if "age" in properties:
                        print(f"Age: {pointer.age}")
                    if "cpf" in properties:
                        print(f"Cpf: {pointer.cpf}")
                    
                else:
                    print(f"Name: {pointer.name}")

                print("\n\t---")

                pointer = pointer.next

                if pointer == self.__head or pointer == None:
                    break
            
        else:

            print("That is empty")