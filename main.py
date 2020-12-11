"""головний модуль додатку
- вивід на екран та в файл розрахунок данних 
- виводити на екран файли первинних данних
"""


from process_data import create_Income_list
from data_service import get_Commodity_circulation, get_Goods, show_Commodity_circulation, show_Goods
import os

MAIN_MENU = \
"""
---------------- Валовий прибуток універмагу ---------------

1 - Вивід прибутку на екран
2 - Запис прибутку в файл
3 - Вивід товарообігу на екран 
4 - Вивід довідника товарних груп
0 - завершити роботу
_______________________________
"""

TITLE = "Валовий прибуток універмагу на поточний рік"
HEADER = \
'''
===========================================================================================================================================
|     Назва       |    Рік    |  План товарообігу  |  Виконання товарообігу  |  Торгова скидка  |  План доходу  |      Виконання доходу   |             
===========================================================================================================================================
'''
FOOTER = \
'''
===========================================================================================================================================
'''

STOP_MASSAGE = "Нажміть будь-яку клавішу для продовження"

def show_Income(Income_list):
    """виводить сформовану статистику прибутку на екран у вигляді таблиці

    Args:
        Income_list ([type]): список прибутку
    """

    print(f'\n\n{TITLE:^120}')
    print(HEADER)

    for Income in Income_list:
        print(f"{Income['Nazva']:20}",
              f"{Income['year']:25}",
              f"{Income['plan_circulation']}",
              f"{Income['expected_perf_circulation']:>14}",
              f"{float(Income['discount']):>20}",
              f"{float(Income['plan_income']):>20.1f}",
              f"{float(Income['expected_perf_income']):22.1f}"
              ) 
    
    
    print(FOOTER)


def write_Income(Income_list):
    """пише список прибутку у файл

    Args:
        Income_list ([type]): список прибутку
    """

    with open('./Data/Income.txt', "w", encoding='utf-8') as Income_file:
        for Income in Income_list:
            line = \
                str(Income['Nazva']) + ';' +                      \
                str(Income['year']) + ';' +                       \
                str(Income['plan_circulation']) + ';' +           \
                str(Income['expected_perf_circulation']) + ';' +  \
                str(Income['discount']) + '; ' +                   \
                str(Income['plan_income']) + '; ' +                \
                str(Income['expected_perf_income']) + '\n' 

            Income_file.write(line)   

        print("Файл прибутку сформовано ...")


while True:

    os.system('clear')
    print (MAIN_MENU)
    command_number = input('Введіть номер команди: ')     
    

    # обробка команд користувача
    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)  

    elif command_number == '1':
        Income_list = create_Income_list()
        show_Income(create_Income_list())
        input(STOP_MASSAGE)

    elif command_number == '2':
        Income_list = create_Income_list()
        write_Income(Income_list)
        input(STOP_MASSAGE)

    elif command_number == '3':
        show_Commodity_circulation(get_Commodity_circulation())
        input(STOP_MASSAGE)

    elif command_number == '4':
        show_Goods(get_Goods())
        input(STOP_MASSAGE)

    else:
        print("невірний номер команди ...")
        input(STOP_MASSAGE)

