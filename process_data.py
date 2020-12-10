"""Валовий дохід універмагу
"""

from data_service import get_Goods, get_Commodity_circulation

# структура рядка розрахункової таблиці
Income = {
    
    'Nazva'                     : '',    # назва устаткування
    'year'                      : 0,     # назва клієнта
    'plan_circulation'          : 0.0,   # номер заказа
    'expected_perf_circulation' : 0,     # кількість
    'discount'                  : 0.0,   # ціна
    'plan_income'               : 0.0,   # сума
    'expected_perf_income'      : 0.0    # Очікуване вик. (Валовий дохід) 
}

def create_Income_list():
    """form a list
    """
    
    def get_Nazva_name(Nazva_code):
        """повертає назву групи по його коді


        Args:
            Nazva_code ([type]): код код товарної групи
        """
        
        for Good in Goods:
            if Nazva_code == Good[0]:
                return Good[1]
        
        return 'назва не знайдена'
    
    def get_discount_name(discount_code):
        """повертає скидку по коді

        Args:
            discount_code ([type]): код товарної скидки
            """

        for Good in Goods:
            if discount_code == Good[0]:
                return Good[2]    

        return 'назва не знайдена'        
      


    Income_list = []
    
    Goods = get_Goods()
    Commodity_circulation = get_Commodity_circulation()
    
    # послідовна обробка рядків масиву 'Commodity_cirulation`
    for Commodity in Commodity_circulation:
        
        # зробити робочий словник з шаблону
        Income_work = Income.copy()

        x = int(Income_work['plan_circulation'])
        y = int(Income_work['discount'])
        z = int(Income_work['expected_perf_circulation'])

        Income_work['Nazva']                     = get_Nazva_name(Commodity[0])
        Income_work['year']                      = Commodity[3]
        Income_work['plan_circulation']          = Commodity[1]
        Income_work['expected_perf_circulation'] = Commodity[2]
        Income_work['discount']                  = get_discount_name(Commodity[0])
        Income_work['plan_income']               = x * y
        Income_work['expected_perf_income']      = z * y

        Income_list.append(Income_work)
