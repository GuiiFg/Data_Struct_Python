# Importing the struct class
from Linked_list.Linked_List import Linked_list

# Creating a Linked list
lista_encadeada = Linked_list()

# Inserting elements on list
for x in range(100, 200):
    lista_encadeada.append(x)

# Show the struct's elements 
lista_encadeada.print_all()

# Show the struct's size
len(lista_encadeada)

# Get a element by index
lista_encadeada.get_index(99)

# Get a lot of elements by index
lista_encadeada.get_indexs([1,2,3,98,99])
