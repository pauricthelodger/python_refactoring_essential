import unittest

from longmethod.src.Order import Order, OrderItem, Customer


class TestOrder(unittest.TestCase):

    def test_summarise_calculates_correct_summary_for_non_loyal_customer_under_threshold(self):
        order = Order(
            items=[
                OrderItem(10.0, 2),  # 20
                OrderItem(5.0, 2)    # 10
            ],
            customer=Customer(False)
        )

        summary = order.summarise()

        self.assertEqual(30.0, summary.subtotal)
        self.assertEqual(0.0, summary.discount)
        self.assertEqual(6.0, summary.tax)
        self.assertEqual(36.0, summary.total)

    def test_summarise_applies_loyal_customer_discount(self):
        order = Order(
            items=[OrderItem(50.0, 1)],
            customer=Customer(True)
        )

        summary = order.summarise()

        self.assertEqual(50.0, summary.subtotal)
        self.assertEqual(5.0, summary.discount)
        self.assertEqual(9.0, summary.tax)
        self.assertEqual(54.0, summary.total)

    def test_summarise_applies_bulk_discount_for_non_loyal_customer_over_threshold(self):
        order = Order(
            items=[OrderItem(120.0, 1)],
            customer=Customer(False)
        )

        summary = order.summarise()

        self.assertEqual(120.0, summary.subtotal)
        self.assertEqual(6.0, summary.discount)
        self.assertEqual(22.8, summary.tax)
        self.assertEqual(136.8, summary.total)

    # -------------------------
    # Guard conditions
    # -------------------------

    def test_summarise_raises_exception_when_items_is_none(self):
        order = Order(items=None, customer=Customer(False))

        with self.assertRaises(ValueError) as context:
            order.summarise()

        self.assertEqual("Items cannot be None", str(context.exception))

    def test_summarise_raises_exception_when_items_is_empty(self):
        order = Order(items=[], customer=Customer(False))

        with self.assertRaises(ValueError) as context:
            order.summarise()

        self.assertEqual("Order must contain items", str(context.exception))

    # -------------------------
    # Boundary test
    # -------------------------

    def test_summarise_no_discount_when_non_loyal_customer_at_threshold(self):
        order = Order(
            items=[OrderItem(100.0, 1)],
            customer=Customer(False)
        )

        summary = order.summarise()

        self.assertEqual(100.0, summary.subtotal)
        self.assertEqual(0.0, summary.discount)
        self.assertEqual(20.0, summary.tax)
        self.assertEqual(120.0, summary.total)


if __name__ == "__main__":
    unittest.main()