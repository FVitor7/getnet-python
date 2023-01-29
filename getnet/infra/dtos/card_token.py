from typing import  List
from pydantic import BaseModel

class CardTokenResponse(BaseModel):
    number_token: str
