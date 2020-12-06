"""Валовий дохід універмагу
"""

from data_service import get_Goods, get_Commodity_circulation

# структура рядка розрахункової таблиці
Income = {
    
    'tovarna_group_name'        : '',    # назва устаткування
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
    
    def get_tovarna_group_name(tovarna_group_code):
        """повертає назву групи по його коді


        Args:
            tovarna_group_code ([type]): код код товарної групи
        """
        
        for Good in Goods:
            if tovarna_group_code == Good[0]:
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
        
        # заповнити робочий словник значеннями 
        Income_work['year']                          = Commodity[3]
        Income_work['plan_circulation']              = Commodity[1]
        Income_work['expected_perf_circulation']     = Commodity[2]
        Income_work['tovarna_group_name']            = get_tovarna_group_name(Commodity[0])
        Income_work['discount']                      = get_discount_name(Commodity[0])
        Income_work['plan_income']                   = Income_work['plan_circulation'] * Income_work['discount']
        Income_work['expected_perf_income']          = Income_work['expected_perf_circulation'] * Income_work['discount']

        # накопичити сформований рядок
        Income_list.append(Income_work)