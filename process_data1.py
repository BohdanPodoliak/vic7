"""розрахунок заявок на товари по магазину
"""

from data_service import get_clients, get_orders

# структура рядка розрахункової таблиці
zajavka = {
    
    'oborud_name'  : '',      # назва устаткування
    'client_name'  : '',      # назва клієнта
    'order_number' : '',      # номер заказа
    'kol'          : 0,       # кількість
    'price'        : 0.0,     # ціна
    'total'        : 0.0      # сума
}

def create_zajvka_list():
    """формування списку заявок по магазину на основі вхідних файлів
    """
    
    def get_client_name(client_code):
        """повертає назву клієнта по його коду

        Args:
            client_code ([type]): код клієнта
        """
        
        for client in clients:
            if client_code == client[0]:
                return client[1]
        
        return 'назва не знайдена'
    
    zajavka_list = []
    
    orders = get_orders()
    clients = get_clients()
    
    # послідовна обробка рядків масиву 'orders`
    for order in orders:
        
        # зробити робочий словник з шаблону
        zajavka_work = zajavka.copy()
        
        # заповнити робочий словник значеннями 
        zajavka_work['oborud_name']   = order[2]
        zajavka_work['order_number']  = order[1]
        zajavka_work['kol']           = order[3]
        zajavka_work['price']         = order[4]
        zajavka_work['total']         = zajavka_work['kol']  * zajavka_work['price']
        zajavka_work['client_name']  = get_client_name(order[0])
        
        # накопичити сформований рядок
        zajavka_list.append(zajavka_work)
        
        
        
        

