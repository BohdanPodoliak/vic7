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






def get_Circulations(Circulations):
    """повертає список речей 

    Returns:
      Circulations_list  : список інформації
    """
    with open ("./Data/Commodity circulation.txt") as Circulations_file:
        from_file = Circulations_file.readlines()


    Circulation_list = []

    for line in from_file:
        line_list = line.split(';')
        Circulations_list.append(line_list)


    return Circulations_list



def show_Circulations(Circulations):
    """Виводить на екран список інформації 

    Args:
        Circulations (list): список інформації
    """
    Circulations_code_from = input("З я кого коду?")
    Circulations_code_to = input("По який код?")

    count_lines = 0

    for Circulation in (Circulations):
        if Circulations_code_from <= Circulation[0] <= Circulations_code_to:
            print("Код: {:8} План: {:5} Очікуєме виконання: {:5} Рік: {:5}".format(Circulation[0], Circulation[1], Circulation[2], Circulation[3]))
            count_lines +=1

    if count_lines == 0:
        print("По вашому запиту нічого не знайдено")

Circulations = get_Circulations ()
show_Circulations (Circulations)