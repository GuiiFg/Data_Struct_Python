from .text_color import PaintText
from .node import Node

class Tree():

    def __init__(self):

        self.__root: Node = None # nó raiz da arvore
        self.__size = 0 # quantidade de nós na arvore
        self.__deep = 0 # profundidade da arvore

    @property
    def size(self):
        return self.__size

    @property
    def deep(self):
        return self.__deep

    def InsertElement(self, node : Node,  root : Node = None, updateBalance = True):
        """
            Insere um elemento na arvore.\n
        """

        # caso não passe uma raiz, sera utilizado a raiz da arvore
        if root == None:
            root = self.__root

        # se a arvore não tem raiz, o nó será a nova raiz
        if root == None:
            self.__root = node
            self.__size += 1
        
        # Caso a arvore já possua elementos, o nó seria direcionado para esquerda(se menor) ou para direita(se maior)

        elif root.value > node.value:

            # caso não tenha elemento na esquerda, ele insere, caso tenha, usa-se recursividade com a raiz da sub-arvore para inserir o elemento
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

        # se o valor do nó já existir na arvore, ele não será inserido
        elif root.value == node.value:
            print("Already inserted!")

        # atualiza o valor de equilibrio de cada no depois de um insert
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

    def UpdateBalance(self, root : Node = None):
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

        


        

            
