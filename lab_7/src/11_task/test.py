import unittest

from main import *


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.order = Order()

    @classmethod
    def tearDownClass(self):
        del self.order

    def test_add_product(self):
        self.order.add_product(Product('cheese', 100, 'milk'))
        self.assertEqual(len(self.order.products), 1)

    def test_add_promotion(self):
        self.order.add_promotion(Promotion('SummerPromo20', 0.8))
        self.assertEqual(len(self.order.promotions), 1)

    def test_cost(self):
        self.assertEqual(self.order.cost, 80.0)
