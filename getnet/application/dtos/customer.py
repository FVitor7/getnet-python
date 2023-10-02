from typing import Optional, List
from pydantic import BaseModel, ValidationError, validator


class AddressSchema(BaseModel):
  street: str
  number: str
  complement: str
  district: str
  city: str
  state: str
  country: str
  postal_code: str


class CustomerSchema(BaseModel):
  seller_id: str
  customer_id: str
  first_name: str
  last_name: str
  document_type: str
  document_number: str
  birth_date: str
  phone_number: str
  celphone_number: str
  email: str
  observation: str
  status: Optional[str]
  address: AddressSchema

