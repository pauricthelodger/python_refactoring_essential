import pytest

from legacy_code.src.ShippingCalculator import ShippingCalculator

EXPECTED_VALUES = (
    (1001, 2.5),
    (1002, 36.8),
    (1003, 27.4),
)

@pytest.mark.parametrize("order_id, expected_value", EXPECTED_VALUES)
def test_e2e(order_id, expected_value):
    calculator = ShippingCalculator()
    returned_value = calculator.calculate_shipping(order_id)
    assert returned_value == expected_value
