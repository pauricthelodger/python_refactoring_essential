import unittest

from feature_envy.src.PriceCalculator import Product, PriceCalculator


class PriceCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = PriceCalculator()

    def test_should_apply_discount_when_product_is_on_sale(self):
        product = Product(100.0, True)

        result = self.calculator.calculate_final_price(product)

        self.assertEqual(80.0, result)

    def test_should_not_apply_discount_when_product_is_not_on_sale(self):
        product = Product(100.0, False)

        result = self.calculator.calculate_final_price(product)

        self.assertEqual(100.0, result)

    def test_should_return_zero_when_price_is_zero_even_if_on_sale(self):
        product = Product(0.0, True)

        result = self.calculator.calculate_final_price(product)

        self.assertEqual(0.0, result)


if __name__ == "__main__":
    unittest.main()