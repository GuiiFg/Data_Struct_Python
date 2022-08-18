from Tree.Tree_struct import Tree, Node

arvore = Tree()

arvore.InsertElement(Node(20))
arvore.InsertElement(Node(30))
arvore.InsertElement(Node(25))
arvore.InsertElement(Node(10))
arvore.InsertElement(Node(32))
arvore.InsertElement(Node(35))
arvore.InsertElement(Node(5))
arvore.InsertElement(Node(2))


#0              20                    .  Gera uma arvore inicialmente 
#0            /    \                  . desbalanceada! O proprio ins_
#1          10      30                . ert gera o equilibrio de cada
#1         /        /  \              . nó na  arvore! Está  é apenas
#2        5       25     32           . uma  representação  da arvore
#2       /                 \          . montada pelo codigo!
#3      2                   35        .
#3                                    .

arvore.PrintAllElements()
arvore.unbalanceNodes
arvore.unbalanceNodes[0][0].layer
arvore.Equalizer()

#0               20                    .
#0            /      \                  .
#1          5        30                .
#1         /  \      /  \              .
#2        2   10    25   32           .
#2                         \          .
#3                          35        .
#3                                    .

arvore.PrintAllElements()

