"""модуль призначено для роботи з файлами вхідних даних  
""" 

def get_Goods():
    """повертає список речей 

    Returns:
      Goods_list  : список товарів
    """
    with open ("./Data/Goods.txt") as Goods_file:
        from_file = Goods_file.readlines()


    Goods_list = []

    for line in from_file:
        line_list = line.split(';')
        Goods_list.append(line_list)


    return Goods_list



def show_Goods(Goods):
    """Виводить на екран список речей 

    Args:
        Goods (list): список речей
    """
    Goods_code_from = input("З я кого коду?")
    Goods_code_to = input("По який код?")

    count_lines = 0

    for Good in (Goods):
        if Goods_code_from <= Good[0] <= Goods_code_to:
            print("Код: {:8} Найменування: {:20} Торгова знижка: {:5}".format(Good[0], Good[1], Good[2]))
            count_lines +=1
        

    if count_lines == 0:
        print("По вашому запиту нічого не знайдено")

Goods = get_Goods()
show_Goods(Goods)







def get_Commodity_circulation():
    """повертає список речей 

    Returns:
      Commodity_circulation_list  : список інформації
    """
    with open ("./Data/Commodity circulation.txt") as Commodity_circulation_file:
        from_file = Commodity_circulation_file.readlines()


    Commodity_circulation_list = []

    for line in from_file:
        line_list = line.split(';')
        Commodity_circulation_list.append(line_list)


    return Commodity_circulation_list



def show_Commodity_circulation(Commodity_circulation):
    """Виводить на екран список інформації 

    Args:
        Commodity_circulation(list): список інформації
    """
    Commodity_circulation_code_from = input("З я кого коду?")
    Commodity_circulation_code_to = input("По який код?")

    count_lines = 0

    for Circulation in (Commodity_circulation):
        if Commodity_circulation_code_from <= Circulation[0] <= Commodity_circulation_code_to:
            print("Код: {:10} План: {:10} Очікуєме виконання: {:10} Рік: {:10}" .format(Circulation[0], Circulation[1], Circulation[2], Circulation[3]))
            count_lines +=1

    if count_lines == 0:
        print("По вашому запиту нічого не знайдено")

Commodity_circulation = get_Commodity_circulation ()
show_Commodity_circulation (Commodity_circulation)