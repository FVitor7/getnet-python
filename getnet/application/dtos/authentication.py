from typing import Optional
from pydantic import BaseModel, ValidationError, validator


class AuthenticationRequest(BaseModel):
  client_id: str
  client_secret: str


class AuthenticationResponse(BaseModel):
    access_token: Optional[str]
    expires_in: Optional[int]
