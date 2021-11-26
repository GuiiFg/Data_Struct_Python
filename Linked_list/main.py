# Importing the struct class
from Linked_list.Linked_List import Linked_list

# Creating a Linked list
lkd_list = Linked_list()

# Inserting elements on list
for x in range(100, 200):
    lkd_list.append(x)

# Show the struct's elements 
lkd_list.print_all()

# Show the struct's size
len(lkd_list)

# Get a element by index
lkd_list.get_index(99)

# Get a lot of elements by index
lkd_list.get_indexs([1,2,3,98,99])

# Delete a element
lkd_list.delete_by_index(98)
