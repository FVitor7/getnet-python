from typing import Optional
from pydantic import BaseModel

class CardVerificationResponse(BaseModel):
    status: str
    verification_id: str
    authorization_code: str
    transaction_id: Optional[str]
