from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Customer:
    loyal: bool

    def is_loyal(self) -> bool:
        return self.loyal


@dataclass(frozen=True)
class OrderItem:
    price: float
    quantity: float


@dataclass(frozen=True)
class OrderSummary:
    subtotal: float
    discount: float
    tax: float
    total: float


class Order:
    def __init__(self, items: List[OrderItem], customer: Customer):
        self.items = items
        self.customer = customer

    def summarise(self) -> OrderSummary:
        # Validation
        if self.items is None:
            raise ValueError("Items cannot be None")
        if len(self.items) == 0:
            raise ValueError("Order must contain items")

        # Subtotal calculation
        subtotal = sum(item.price * item.quantity for item in self.items)

        # Discount rules
        discount = 0.0
        if self.customer.is_loyal():
            discount = subtotal * 0.10
        elif subtotal > 100:
            discount = subtotal * 0.05

        # Tax calculation
        taxable_amount = subtotal - discount
        tax = taxable_amount * 0.20

        # Total calculation
        total = taxable_amount + tax

        return OrderSummary(subtotal, discount, tax, total)