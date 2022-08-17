class Node():

    def __init__(self, value, left = None, right = None, level = None):

        self.__value = value
        self.__left = left
        self.__right = right
        self.__level = level

    @property
    def value(self):
        return self.__value

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def level(self):
        return self.__level
