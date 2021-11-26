
class Person():

    def __init__(self, name, age, cpf):

        self.__next = None
        self.__prev = None

        self.__name = name
        self.__age = age
        self.__cpf = cpf


    @property
    def next (self):
        return self.__next

    @next.setter
    def next (self, value):
        self.__next = value
        
    @property
    def prev (self):
        return self.__prev

    @prev.setter
    def prev (self, value):
        self.__prev = value
        
    @property
    def name (self):
        return self.__name

    @name.setter
    def name (self, value):
        self.__name = value
        
    @property
    def age (self):
        return self.__age

    @age.setter
    def age (self, value):
        self.__age = value
        
    @property
    def cpf (self):
        return self.__cpf

    @cpf.setter
    def cpf (self, value):
        self.__cpf = value
        
