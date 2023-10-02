from typing import Optional, List
from pydantic import BaseModel, ValidationError, validator


class CardBin(BaseModel):
  country: Optional[str]
  country_code: Optional[str]
  brand_code: Optional[str]
  product: Optional[str]
  brazilian_issued: Optional[str]
  bin: Optional[int]
  country_code_iso: Optional[str]
  type: Optional[str]
  brand: Optional[str]
  issuer: Optional[str]


class CardBinResponse(BaseModel):
    results: List[CardBin]
    status: str = "OK"
