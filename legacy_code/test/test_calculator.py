from legacy_code.src.ShippingCalculator import ShippingCalculator

EXPECTED_VALUES = (
    (1001, 2.5),
    (1002, 36.8),
    (1003, 27.4),
)

def test_e2e():
    calculator = ShippingCalculator()
    for order_id, expected_value in EXPECTED_VALUES:
        returned_value = calculator.calculate_shipping(order_id)
        assert returned_value == expected_value
