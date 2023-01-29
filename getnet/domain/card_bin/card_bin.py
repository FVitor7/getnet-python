"""Implement Token Service"""
from pydantic import ValidationError
from getnet.domain.services import Service as BaseService
from getnet.infra.dtos.card_bin import CardBinResponse


class CardBinInfo(BaseService):
    """Represents the token service operations"""

    path = "/v1/cards/binlookup/"

    def binlookup(self, card_bin: str):
        self._client.request.headers = (
            {
                "Authorization": "Bearer {}".format(self._client.access_token),
            }
        )

        url = f"{self.path}{card_bin}"

        try:
            card_data = CardBinResponse(**self._get(url))
        except ValidationError as e:
            raise e.errors()

        return card_data
