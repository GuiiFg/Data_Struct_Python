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

    def InsertElement(self, node : Node,  root : Node = None, updateBalance = True):
        
        if root == None:
            root = self.__root

        if root == None:
            self.__root = node
            self.__size += 1
        
        elif root.value > node.value:

            if root.left == None:
                root.left = node
                self.__size += 1
            else:
                self.InsertElement(node, root.left, False)

        elif root.value < node.value:

            if root.right == None:
                root.right = node
                self.__size += 1
            else:
                self.InsertElement(node, root.right, False)

        elif root.value == node.value:
            print("Already inserted!")

        if updateBalance:
            print("updating balance...")
            self.UpdateBalance()
            print("updated balance!")
            


    def PrintAllElements(self, root = None, count = 0):
        if root == None:
            root = self.__root

        left = root.left.value if root.left != None else "none"
        right = root.right.value if root.right != None else "none"

        unbalance = ""
        if root.balance != None:
            unbalance = " | WARING" if abs(root.balance) > 1 else ""

        print("Layer: " + str(count) + f" - Balance: {root.balance} - Values: {left} <- {root.value} -> {right}" + unbalance)

        if root.left != None:
            self.PrintAllElements(root.left, count + 1)
        if root.right != None:
            self.PrintAllElements(root.right, count + 1)

    def UpdateBalance(self, root = None):
        if root == None:
            root = self.__root

        aux = root

        leftBalance = 0
        rightBalance = 0

        while aux.left != None:
            aux = aux.left
            leftBalance += 1

        aux = root

        while aux.right != None:
            aux = aux.right
            rightBalance += 1

        root.balance = rightBalance - leftBalance

        if root.left != None:
            self.UpdateBalance(root.left)
        if root.right != None:
            self.UpdateBalance(root.right)

        


        

            
