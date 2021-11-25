from Doubly_linked_list.Doubly_Linked_List import Doubly_linked_list
from Doubly_linked_list.Doubly_Linked_List import Car

import pandas as pd

df_cars = pd.read_csv("Doubly_linked_list\cars_list.csv", ';')

cars_list = [Car(
    model = row.model,
    licence_plate = row.licence_plate,
    price = row.price,
    color = row.color,
    km = row.km
) for index, row in df_cars.iterrows()]

dl_list = Doubly_linked_list()

for car in cars_list:
    dl_list.insert_element(car)

dl_list.print_front_to_back()
dl_list.print_back_to_front()

dl_list.price
dl_list.models