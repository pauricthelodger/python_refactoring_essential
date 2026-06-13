class ShippingNoteGenerator:

    def generate_shipping_note(
        self,
        customer_first_name,
        customer_last_name,

        address_line1,
        address_line2,
        city,
        postcode,
        country,

        order_id,
        item_description,
        quantity
    ):
        full_name = customer_first_name + " " + customer_last_name

        address = address_line1 + ", " + (
            address_line2 + ", " if address_line2 is not None else ""
        ) + city + ", " + postcode + ", " + country

        return (
            "SHIPPING NOTE\n"
            f"Order: {order_id}\n"
            f"Customer: {full_name}\n"
            f"Ship To: {address}\n"
            f"Item: {item_description}\n"
            f"Quantity: {quantity}"
        )