from pprint import pprint
from pydantic import BaseModel, EmailStr

# before run this script run this command
# uv add pydantic[email]

# Create a simple model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
# Create a nested model with Built-in validatior for email format
class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr # Built-in validator for email format
    address: list[Address] # List of nested Address models

# Valid data with nested structure
user_data = {
    "id": 2 ,
    "name": "Areeba Zafar",
    'email': "areebazafar@gmail.com",
    "address": [
        {"street": "123 street - PCHS", "city": "Karachi", "zip_code": "00345"},
        {"street": "942 street - Shah Faisal", "city": "Karachi", "zip_code": "00345"}
    ]
}   

user = UserWithAddress.model_validate(user_data)

print(user.model_dump())
print("\n\n")
pprint(user.model_dump()) # prints in pretty print (pprint)