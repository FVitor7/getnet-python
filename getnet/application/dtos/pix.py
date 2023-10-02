from typing import Optional, List
from pydantic import BaseModel, ValidationError, validator


class AdditionalData(BaseModel):
  creation_date_qrcode: Optional[str]
  expiration_date_qrcode: Optional[str]
  psp_code: Optional[str]
  qr_code: Optional[str]
  transaction_id: Optional[str]