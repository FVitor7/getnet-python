PRODUCT_TYPES = (
    "cash_carry",
    "digital_content",
    "digital_goods",
    "digital_physical",
    "gift_card",
    "physical_goods",
    "renew_subs",
    "shareware",
    "service",
)


class Order:
    order_id: str
    sales_tax: int
    product_type: str

    def __init__(self, order_id: str, sales_tax: int, product_type: str):
        if len(order_id) > 36:
            raise TypeError("The order_id must have bellow of 32 characters")

        if product_type and product_type not in PRODUCT_TYPES:
            raise TypeError("The product_type is invalid")

        self.order_id = order_id
        if sales_tax:
            self.sales_tax = sales_tax
        if product_type:
            self.product_type = product_type

    def as_dict(self):
        return self.__dict__.copy()
