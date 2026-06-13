from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    price: float
    on_sale: bool

    def get_price(self) -> float:
        return self.price

    def is_on_sale(self) -> bool:
        return self.on_sale


class PriceCalculator:
    def calculate_final_price(self, product: Product) -> float:
        price = product.get_price()

        if product.is_on_sale():
            price *= 0.8

        return price