"""головний модуль додатку
- вивід на екран та в файл розрахунок данних 
- виводити на екран файли первинних данних
"""

import os

from process_data import create_Income_list
MAIN_MENU = \
'''
---------------- Валовий дохід універмагу ---------------

1 - Вивід заяв на екран
2 - Запис заявок в файл
3 - Вивід накладних на екран 
4 - Вивід списка клієнтів
0 - завершити роботу
_______________________________
'''

def show_Import(Import_list):
    """Виводить на екран таблицю прибутку

    Args:
        Import_list ([type]): список прибутку
    """





while True:

    os.system('cls')
    print(MAIN_MENU)
    command_number = input('Введіть номер команди')     
    

    # обробка команд користувача

    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit()  

    elif command_number == '1':
        Income_list = create_Income_list()

        show_Income(Income_list)
        input()

