
from Linked_list.Linked_List import Linked_list


lista_encadeada = Linked_list()

lista_encadeada.print_all()

for x in range(100, 200):
    lista_encadeada.append(x)

lista_encadeada.print_all()

len(lista_encadeada)

lista_encadeada.get_index(99)
lista_encadeada.get_indexs([1,2,3,98,99])
