from main import *


order = Order()


order.add_product(Product('cheese', 100, 'milk'))
order.add_product(Product('milk', 40, 'milk'))
order.add_product(Product('red bread', 10, 'bread'))
order.add_product(Product('pizza', 600, 'meat'))
order.print_order()



order.add_promotion(Promotion('SummerPromo20', 0.8))
order.print_order()


order.add_promotion(CategoryPromotion('MilkDay', 0.9, 'milk'))
order.print_order()


print('milk category:', order.get_cost_by_category('milk'))
