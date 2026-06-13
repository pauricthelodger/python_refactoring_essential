import unittest

from long_parameter_list.src.ShippingNoteGenerator import ShippingNoteGenerator


class ShippingNoteGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.shipping_note_generator = ShippingNoteGenerator()

    def test_should_generate_shipping_note_with_all_input_fields(self):
        result = self.shipping_note_generator.generate_shipping_note(
            "Jane",
            "Doe",

            "12 Baker Street",
            "Flat 4B",
            "London",
            "NW1 6XE",
            "UK",

            "ORD-123",
            "Wireless Headphones",
            2
        )

        self.assertIn("Order: ORD-123", result)
        self.assertIn("Customer: Jane Doe", result)
        self.assertIn("Item: Wireless Headphones", result)
        self.assertIn("Quantity: 2", result)

        self.assertIn("12 Baker Street", result)
        self.assertIn("Flat 4B", result)
        self.assertIn("London", result)
        self.assertIn("NW1 6XE", result)
        self.assertIn("UK", result)

    def test_should_include_customer_full_name(self):
        result = self.shipping_note_generator.generate_shipping_note(
            "John",
            "Smith",

            "1 High Street",
            "Apt 2",
            "Manchester",
            "M1 2AB",
            "UK",

            "ORD-999",
            "Laptop",
            1
        )

        self.assertIn("Customer: John Smith", result)

    def test_should_include_order_id_and_item_details(self):
        result = self.shipping_note_generator.generate_shipping_note(
            "Alice",
            "Brown",

            "50 King Street",
            "Unit 3",
            "Birmingham",
            "B1 1AA",
            "UK",

            "ORD-555",
            "Tablet",
            5
        )

        self.assertIn("Order: ORD-555", result)
        self.assertIn("Item: Tablet", result)
        self.assertIn("Quantity: 5", result)

    def test_should_include_full_address_across_all_fields(self):
        result = self.shipping_note_generator.generate_shipping_note(
            "Emma",
            "Jones",

            "99 High Road",
            "Floor 2",
            "Leeds",
            "LS1 4AB",
            "UK",

            "ORD-777",
            "Monitor",
            3
        )

        self.assertIn("99 High Road", result)
        self.assertIn("Floor 2", result)
        self.assertIn("Leeds", result)
        self.assertIn("LS1 4AB", result)
        self.assertIn("UK", result)

    def test_should_include_quantity_correctly(self):
        result = self.shipping_note_generator.generate_shipping_note(
            "Tom",
            "White",

            "10 Market Street",
            "",
            "Liverpool",
            "L1 8JQ",
            "UK",

            "ORD-321",
            "Keyboard",
            10
        )

        self.assertIn("Quantity: 10", result)


if __name__ == "__main__":
    unittest.main()