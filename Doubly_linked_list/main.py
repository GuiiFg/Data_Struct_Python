# Imporst 
from Doubly_linked_list.Doubly_Linked_List import Doubly_linked_list
from Doubly_linked_list.Doubly_Linked_List import Car

# Here I use pandas to read a csv with things about cars and for each row on dataframe in a object Car
# The class Car is the node of struct
import pandas as pd

df_cars = pd.read_csv("Doubly_linked_list\cars_list.csv", ';')

# Convert rows into objects
cars_list = [Car(
    model = row.model,
    licence_plate = row.licence_plate,
    price = row.price,
    color = row.color,
    km = row.km
) for index, row in df_cars.iterrows()]

# Initilize the Doubly linked list
dl_list = Doubly_linked_list()

# Insert the cars list on struct
for car in cars_list:
    dl_list.insert_element(car)

# Show all elements, one time front to back and other time back to front
dl_list.print_front_to_back()
dl_list.print_back_to_front()

# Show price of all cars together
dl_list.price

# Show all car models on list
dl_list.models

# delete a element by licence plate
dl_list.delete_by_licence_plate("FERR4R1")

dl_list.print_front_to_back()
