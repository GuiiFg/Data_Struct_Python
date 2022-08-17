from .node import Node

class Three():

    def __init__(self):

        self.__root: Node = None
        self.__size = 0
        self.__deep = 0

    @property
    def size(self):
        return self.__size

    @property
    def deep(self):
        return self.__deep

    def InsertElement(self, value):

        no = Node(value=value)

        if self.__root == None:
            self.__root = no
            self.__size = 1
        else:
            aux : Node = self.__root

            while True:
                if aux.value == no.value:
                    print("This value is already registred!")
                    break
                elif aux.value > no.value:

                    if aux.left == None:
                        aux.left = no
                        self.__size += 1
                        print("Element inserted!")
                        break
                    else:
                        aux = aux.left
                elif aux.value < no.value:

                    if aux.right == None:
                        aux.right = no
                        self.__size += 1
                        print("Element inserted!")
                        break
                    else:
                        aux = aux.right

            
