"""Implements the CardNumber entity"""
import re
from typing import Optional, Union

from getnet.infra.dtos.authentication import AuthenticationResponse
from getnet.utils import handler_request, handler_request_exception
from datetime import datetime, timedelta
from pydantic import ValidationError


class Authentication:
    client_id: Optional[Union[str, None]] = None
    client_secret: Optional[Union[str, None]] = None
    access_token: Optional[Union[str, None]] = None
    access_token_expires: Optional[Union[int, None]] = None


    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    
    def access_token_expired(self) -> bool:
        """Returns true if not have an token or is expired

        Returns:
            bool
        """
        return (
            self.access_token is None
            or self.access_token_expires < datetime.timestamp(datetime.now())
        )


    def auth(self) -> None:
        if self.access_token_expired():
            path = "/auth/oauth/v2/token"
            data = {"scope": "oob", "grant_type": "client_credentials"}

            response = self.request.post(
                self.base_url + path,
                data=data,
                auth=(self.client_id, self.client_secret),
            )

            if not response.ok:
                raise handler_request_exception(response)

            try:
                response_data = AuthenticationResponse(**response.json())
            except ValidationError as e:
                raise e.errors()

            self.access_token = response_data.access_token
            self.access_token_expires = int(
                datetime.timestamp(
                    datetime.now() + timedelta(seconds=response_data.expires_in)
                )
            )
            self.request.headers.update(
                {"Authorization": "Bearer {}".format(self.access_token)}
            )
            