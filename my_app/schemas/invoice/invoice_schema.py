"""
Module to defines the invoice schema.
"""

from pydantic import BaseModel, Field
from typing import Optional, List


class Establishment(BaseModel):
    name: str
    address: str
    phone_number: str
    email: str
    municipality_id: int


class Customer(BaseModel):
    identification: str
    dv: Optional[int]
    company: Optional[str]
    trade_name: Optional[str]
    names: Optional[str]
    address: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    legal_organization_id: int
    tribute_id: int
    identification_document_id: int
    municipality_id: Optional[int]


class WithholdingTaxes(BaseModel):
    code: str
    withholding_tax_rate: float


class Items(BaseModel):
    code_reference: str
    name: str
    quantity: int
    discount_rate: float
    price: float
    tax_rate: str
    unit_measure_id: int
    standard_code_id: int
    is_excluded: int
    tribute_id: int
    withholding_taxes: Optional[List[WithholdingTaxes]] = Field(default_factory=list)


class AllowanceCharges(BaseModel):
    concept_type: str
    is_surcharge: bool
    reason: str
    base_amount: float
    amount: float


class Invoice(BaseModel):
    document: Optional[str]
    numbering_range_id: int
    reference_code: str
    observation: str
    payment_method_code: Optional[int]
    establishment: Optional[Establishment]
    customer: Customer
    items: List[Items] = Field(default_factory=list)
    allowance_charges: List[AllowanceCharges] = Field(default_factory=list)
