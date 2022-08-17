from Three.Three_struct import Three, Node

arvore = Three()

arvore.InsertElement(Node(20))
arvore.InsertElement(Node(30))
arvore.InsertElement(Node(25))
arvore.InsertElement(Node(10))
arvore.InsertElement(Node(32))
arvore.InsertElement(Node(35))
arvore.InsertElement(Node(5))
arvore.InsertElement(Node(2))


#0              20
#0            /    \                  .
#1          10      30                .
#1         /        /  \              .
#2        5       25     32           .
#2       /                 \          .
#3      2                   35        .
#3                                    .

arvore.PrintAllElements()
