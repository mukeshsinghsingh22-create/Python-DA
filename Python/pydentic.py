from pydantic import BaseModel, field_validator, model_validator, Field, EmailStr, HttpUrl, constr, conint, confloat, conlist
from typing import Optional, Any, List, Dict, Union, Annotated

class ProductInfo(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=15)]
    price: Annotated[float, Field(gt=0, lt=10000)]
    stock: Annotated[int, Field(ge=0, lt=10000)]
    category: Optional[str] = None
    sku: Optional[str] = None
    Email: Optional[EmailStr] = None

    @model_validator(mode="before")
    def check_name_length(values): 
        name = values.get("name")
        if name and len(name) > 15:
            raise ValueError("name must be at most 15 characters long")
        return values

    @field_validator("price")
    def price_must_be_positive(value):
        if value <= 0:
            raise ValueError("price must be a positive number")
        return value

    @field_validator("stock")
    def stock_must_be_non_negative(value):
        if value < 0:
            raise ValueError("stock cannot be negative")
        return value

    @field_validator("Email")
    def email_must_be_valid(value):
        if value and "@" not in value:
            raise ValueError("Email must be a valid email address")
        return value

def insert(state:ProductInfo):
    print(state.name)
    print(state.price)
    print(state.stock)
    print(state.category)
    print(state.sku)
    print(state.Email)  

data = {
    "name": "Sample Product",
    "price": 99.99,
    "stock": 50,
    "category": "Electronics",
    "sku": "SP-001",
    "Email": "sample@example.com"
}

obj = ProductInfo(**data)
insert(obj)




