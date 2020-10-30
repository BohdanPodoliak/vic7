"""модуль призначено для роботи з файлами вхдних даних  
""" 

def get_Goods():
    """повертає список речей 

    Returns:
      Goods_list  : список товарів
    """
    
    from_file = [
     "1000;Тканини;4",
     "2000;Одяг та білизна;7,5",
     "3000;Взуття;7,5",
     "4000;Трикотаж;7,5",
     "5000;Галантерея;9,5"
    ]

    Goods_list = []

    for line in from_file:
        line_list = line.split(';')
        Goods_list.append(line_list)


    return Goods_list

Goods = get_Goods()

for c in Goods:
    print(c)
