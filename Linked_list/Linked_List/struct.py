from .__node import Node

class Linked_list():
    """
    Linked list
    """
    def __init__(self):
        """
        Initialize the Linked list with heah = None
        so that is clear
        """
        self.__head = None
        self.__size = 0

    def __len__(self):
        """
        return the list len
        """
        return self.__size

    def append(self, elemento):
        """
        add a new element on list
        """
        pointer = self.__head
        
        if pointer != None:

            while(pointer.next):
                pointer = pointer.next

            pointer.next = Node(elemento)

        else:

            self.__head = Node(elemento)

        self.__size += 1

    def print_all(self):

        """
        Show the elements
        """

        if (self.__size > 0):

            pointer = self.__head
            
            counter = 0
            print("index - value")

            while(pointer):
                print(str(counter) + " - " + str(pointer.value))
                counter += 1
                pointer = pointer.next
            
        else:
            print("Dont have nothing here!")


    def get_index(self, index:int):
        """
        find a element
        """
        if (self.__size > 0):

            if index <= self.__size - 1:
                pointer = self.__head
                counter = 0

                while True:
                    
                    if index == counter:
                        print("index - value")
                        print(str(counter) + " - " + str(pointer.value))
                        break

                    counter += 1

                    pointer = pointer.next

            else:
                print("Index out of range!")
            
        else:
            print("Dont have nothing here!")

    def get_indexs(self, indexs:list):
        header = False

        if (self.__size > 0):

            for index in indexs:
                if index <= self.__size - 1:
                    pointer = self.__head
                    counter = 0

                    if not header:
                        print("index - value")
                        header = True

                    while True:
                        
                        if index == counter:
                            print(str(counter) + " - " + str(pointer.value))
                            break

                        counter += 1

                        pointer = pointer.next

            else:
                print("Index out of range!")
            
        else:
            print("Dont have nothing here!")

    def delete_by_index(self, index):
        """
        delete a element by index
        """
        if (self.__size > 0):

            if index <= self.__size - 1:

                pointer = self.__head
                prev = pointer
                counter = 0

                while True:
                    
                    if index == counter:
                        
                        prev.next = pointer.next

                        self.__size -= 1

                        break

                    counter += 1

                    prev = pointer
                    pointer = pointer.next

            else:
                print("Index out of range!")
            
        else:
            print("Dont have nothing here!")