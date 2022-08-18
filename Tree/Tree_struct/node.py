class Node():

    def __init__(self, value, left = None, right = None, layer = None, balance = None):

        """
            value    # valor para posicionamento na arvore\n
            left     # elemento que está a sua esquerda\n
            right    # elemento que está a sua direita\n
            layer    # nivel que o nó esta situado na arvore\n
            balance  # equilibrio atual do nó
        """

        self.__value = value 
        self.__left = left
        self.__right = right
        self.__layer = layer
        self.__balance = balance

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value

    @property
    def layer(self):
        return self.__layer

    @layer.setter
    def layer(self, value):
        self.__layer = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

