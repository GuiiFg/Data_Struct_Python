from Circular_doubly_linked_list.Circular_Doubly_Linked_List import *

import pandas as pd


df_peaple = pd.read_csv("Circular_doubly_linked_list\data_peaple.csv", ";", encoding="utf-8")

cdl_list = Circular_Doubly_Linked_List()

for index, row in df_peaple.iterrows():
    cdl_list.insert_element(row.first_name, row.age, row.cpf)

cdl_list.Show_all()

cdl_list.Show_all(["name", "age", "cpf"])