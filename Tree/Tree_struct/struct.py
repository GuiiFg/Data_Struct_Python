from .node import Node

class Tree():

    def __init__(self):

        self.__root: Node = None # nó raiz da arvore
        self.__size = 0 # quantidade de nós na arvore
        self.__deep = 0 # profundidade da arvore
        self.__unbalanceNodes = []

    @property
    def size(self):
        return self.__size

    @property
    def deep(self):
        return self.__deep

    @property
    def unbalanceNodes(self) -> list:
        return self.__unbalanceNodes

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
            self.__unbalanceNodes.clear()
            self.UpdateBalance()
            print("updated balance!")

    def PrintAllElements(self, root = None, count = 0):
        if root == None:
            root = self.__root

        left = root.left.value if root.left != None else "none"
        right = root.right.value if root.right != None else "none"

        unbalance = ""
        unbalanceBool = False
        if root.balance != None:
            if abs(root.balance) > 1:
                unbalance = " | WARING" 
                unbalanceBool = True

        textPrint = "Layer: " + str(count) + f" - Balance: {root.balance} - Values: {left} <- {root.value} -> {right}" + unbalance

        if unbalanceBool:
            textPrint = '\033[1;31m' + textPrint + '\033[0;37m'

        print(textPrint)

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

        if root.balance > 1 or root.balance < -1:
            self.__unbalanceNodes.append([root, root.balance])

        if root.left != None:
            self.UpdateBalance(root.left)
        if root.right != None:
            self.UpdateBalance(root.right)

    def Equalizer(self):

        toBalance = None

        for x in self.__unbalanceNodes:
            if toBalance == None:
                toBalance = x
            else:
                toBalance = x if abs(toBalance[1]) > abs(x[1]) else toBalance

        if toBalance[1] == -2:
            self.RightRotation(toBalance[0])


    def RightRotation(self, nodeUnbalance : Node):

        nodeDad : Node = self.FindDad(nodeUnbalance)
        nodeSon : Node = nodeUnbalance.left

        nodeDad.left = nodeUnbalance.left
        nodeUnbalance.left = nodeSon.right
        nodeSon.right = nodeUnbalance

        self.UpdateBalance()

    def FindDad(self, nodeSon : Node, root : Node = None):

        root = self.__root if root == None else root

        if self.__root.value == nodeSon.value:
            return None

        if root.value < nodeSon.value:
            aux = root.right
            if aux.value == nodeSon.value:
                return root
            else:
                return self.FindDad(nodeSon, aux)

        if root.value > nodeSon.value:
            aux = root.left
            if aux.value == nodeSon.value:
                return root
            else:
                return self.FindDad(nodeSon, aux) 


        
        

        


        

            
