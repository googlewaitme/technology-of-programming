from typing import List


class Product:
    def __init__(self, name: str, cost: float, category: str):
        self.name = name
        self.start_cost = cost
        self.category = category
        self.cost = cost


class Promotion:
    '''
    Скидка на всё корзину
    '''
    def __init__(self, name: int, procent: float):
        self.name = name
        self.procent = procent

    def use(self, products: List[Product]) -> List[Product]:
        for product in products:
            product.cost = product.start_cost * self.procent


class CategoryPromotion(Promotion):
    '''
    Скидка на категорию
    '''
    def __init__(self, name: str, procent: float, category: str):
        super().__init__(name, procent)
        self.category = category

    def use(self, products: List[Product]) -> List[Product]:
        for product in products:
            if product.category == self.category:
                product.cost = product.start_cost * self.procent
        return products


class Order:
    '''
    Заказ
    '''
    def __init__(self):
        self.products = []
        self.promotions = []
        self.cost = 0

    def add_product(self, product: Product):
        self.products.append(product)
        self.calculate()

    def add_promotion(self, promotion: Promotion):
        self.promotions.append(promotion)
        self.calculate()

    def get_cost_by_category(self, category: str) -> int:
        return sum(el.cost for el in self.products if el.category == category)

    def calculate(self):
        for promo in self.promotions:
            promo.use(self.products)
        self.cost = sum(product.cost for product in self.products)

    def print_order(self):
        print('Order')
        for promo in self.promotions:
            print('promo', promo.name, "sale", promo.procent)
        for product in self.products:
            print('product', product.name, product.cost, product.category)

