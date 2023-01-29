from getnet.domain.cards import Card as BaseCard


class Card(BaseCard):
    def __init__(self, **kwargs):
        kwargs.update({"customer_id": "", "cardholder_identification": None})

        super(Card, self).__init__(**kwargs)

    def _as_dict(self):
        data = super(Card, self)._as_dict()
        data.pop("customer_id")
        data.pop("verify_card")
        data.pop("cardholder_identification")

        return data
