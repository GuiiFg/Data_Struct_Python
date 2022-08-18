from platform import node
from unittest import result
from xmlrpc.client import boolean
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
                node.layer = root.layer + 1
                root.left = node
                self.__size += 1
            else:
                self.InsertElement(node, root.left, False)

        elif root.value < node.value:

            if root.right == None:
                node.layer = root.layer + 1
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

        print(f"calculando de: v{root.value}/l{root.layer}")

        root.balance = self.CalculateBalance(root.left) - self.CalculateBalance(root.right)

        print('\033[1;31m' + f"result: {root.balance} = {self.CalculateBalance(root.left)} - {self.CalculateBalance(root.right)}" + '\033[0;37m')

        if root.left != None:
            self.UpdateBalance(root.left)
        if root.right != None:
            self.UpdateBalance(root.right)



    def CalculateBalance(self, root : Node, count = 0):
        
        if root == None:
            return 0

        numLeft = count
        numRight = 0

        if root.left != None:
            numLeft = self.CalculateBalance(root.left, count + 1)
        if root.right != None:
            numRight = self.CalculateBalance(root.right, count + 1)

        return numLeft + numRight




    def UpdateLayer(self, root = None, count = 0):

        root = self.__root if root == None else root

        root.layer = count

        if root.left != None:
            self.UpdateLayer(root.left, count + 1)
        if root.right != None:
            self.UpdateLayer(root.right, count + 1)

    def Equalizer(self):

        toBalance = None

        # seleciona o nó mais desbalanceado para começar o balanceamento
        for x in self.__unbalanceNodes:
            if toBalance == None:
                toBalance = x
            else:
                toBalance = x if abs(toBalance[1]) > abs(x[1]) else toBalance

        # ler __info.md para detalhes do balanceamento

        # decide qual rotacao sera usada de acordo com o desequilibrio
        if toBalance[1] == 2:
            self.RotationLL(toBalance[0])
        elif toBalance[1] == -2:
            #self.RotationRR(toBalance[0])
            pass


    def RotationLL(self, nodeUnbalance : Node):

        # Rotacao a direita peso e (left, left)

        nodeDad = None
        direction = None

        if nodeUnbalance != self.__root:
            #direction é a direção True(right) e False(left)
            nodeDad, direction = self.FindDad(nodeUnbalance)

        x = nodeUnbalance
        y = nodeUnbalance.left
        
        x.left = y.right
        y.right = x

        if nodeDad == None:
            self.__root = y
        else:
            if direction:
                nodeDad.right = y
            else:
                nodeDad.left = y

        self.UpdateBalance()

    def FindDad(self, nodeSon : Node, root : Node = None):

        root = self.__root if root == None else root

        if root.value < nodeSon.value:
            aux = root.right
            if aux.value == nodeSon.value:
                return (root, True)
            else:
                return self.FindDad(nodeSon, aux)

        if root.value > nodeSon.value:
            aux = root.left
            if aux.value == nodeSon.value:
                return (root, False)
            else:
                return self.FindDad(nodeSon, aux) 


