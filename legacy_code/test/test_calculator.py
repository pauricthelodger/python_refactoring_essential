import pytest

from legacy_code.src.ShippingCalculator import ShippingCalculator, get_order_data

EXPECTED_VALUES = (
    (1001, 2.5),
    (1002, 36.8),
    (1003, 27.4),
)

EXPECTED_RESPONSES = {
    1001: {
        "orderId": 1001,
        "shippingType": "STANDARD",
        "weightKg": 5,
        "distanceKm": 120,
        "fragile": False,
    },
    1002: {
        "orderId": 1002,
        "shippingType": "EXPRESS",
        "weightKg": 8.5,
        "distanceKm": 300,
        "fragile": True,
    },
    1003: {
        "orderId": 1003,
        "shippingType": "OVERNIGHT",
        "weightKg": 2,
        "distanceKm": 50,
        "fragile": False,
    },
    1004: {
        "orderId": 1004,
        "shippingType": "INTERNATIONAL",
        "weightKg": 2,
        "distanceKm": 50,
        "fragile": False,
    },
}


@pytest.mark.api
@pytest.mark.withoutresponses
@pytest.mark.parametrize("order_id, expected_value", EXPECTED_VALUES)
def test_e2e(order_id, expected_value):
    calculator = ShippingCalculator()
    returned_value = calculator.calculate_shipping(order_id)
    assert returned_value == expected_value


@pytest.mark.api
@pytest.mark.withoutresponses
@pytest.mark.parametrize("order_id", (1001, 1002, 1003, 1004))
def test_get_order_data(order_id):
    expected_response = EXPECTED_RESPONSES[order_id]
    data = get_order_data(order_id)
    assert data == expected_response


@pytest.mark.parametrize("order_id, expected_value", EXPECTED_VALUES)
def test_get_order_data_without_request(responses, order_id, expected_value):
    expected_response = EXPECTED_RESPONSES[order_id]
    responses.get(
        f"https://codemanship.co.uk/api/orders.php?orderId={order_id}",
        json=expected_response,
    )
    data = get_order_data(order_id)
    assert data == expected_response


@pytest.mark.parametrize("order_id, expected_value", EXPECTED_VALUES)
def test_without_request(responses, order_id, expected_value):
    expected_response = EXPECTED_RESPONSES[order_id]
    responses.get(
        f"https://codemanship.co.uk/api/orders.php?orderId={order_id}",
        json=expected_response,
    )

    calculator = ShippingCalculator()
    returned_value = calculator.calculate_shipping(order_id)
    assert returned_value == expected_value
