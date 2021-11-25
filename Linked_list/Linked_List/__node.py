
class Node:
    """
    Node with the used properties
    """
    def __init__(self, number):

        self.__value = number
        self.__next = None

    @property
    def value (self):
        return self.__value

    @property
    def next (self):
        return self.__next

    @value.setter
    def value (self, value):
        self.__value = value

    @next.setter
    def next (self, value):
        self.__next = value