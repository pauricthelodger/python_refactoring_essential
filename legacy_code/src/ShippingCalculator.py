from dataclasses import dataclass
import requests


@dataclass(frozen=True)
class Order:
    orderId: int
    shippingType: str
    weightKg: float
    distanceKm: float
    fragile: bool


def get_order_data(order_id: int) -> dict:
    url = f"https://codemanship.co.uk/api/orders.php?orderId={order_id}"

    response = requests.get(url)
    response.raise_for_status()

    return response.json()


class ShippingCalculator:

    def calculate_shipping(self, order_id: int) -> float:
        try:
            data = get_order_data(order_id)

            order = Order(
                orderId=data["orderId"],
                shippingType=data["shippingType"],
                weightKg=data["weightKg"],
                distanceKm=data["distanceKm"],
                fragile=data["fragile"]
            )

            if order.shippingType == "STANDARD":
                return order.weightKg * 0.5

            elif order.shippingType == "EXPRESS":
                return order.weightKg * 0.8 + order.distanceKm * 0.1

            elif order.shippingType == "OVERNIGHT":
                return order.weightKg * 1.2 + 25

            else:
                raise RuntimeError(f"Unknown shipping type: {order.shippingType}")

        except Exception as e:
            print(e)
            return -1.0
