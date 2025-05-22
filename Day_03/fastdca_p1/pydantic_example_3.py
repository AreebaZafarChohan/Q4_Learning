from pprint import pprint
from pydantic import BaseModel, EmailStr, field_validator , ValidationError

# validator is a old way in new way Pydantic v2 style we'll wrote field_validator

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
    addresses: list[Address] # List of nested Address models
    
    @field_validator("name")
    def name_validation(cls, value):
        
        if not value.strip():
            raise ValueError("Name cannot be empty")
        
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters long")
        
        if not value[0].isupper():
            raise ValueError("Name must start with capital letter")
        
        return value

print("\n-------------------------------------------------\n")     
            

# Valid data with nested structure and try except to handle error
try:
    user_data = UserWithAddress(
        id=3,
        name="Areeba zafar",
        email="areebazafar@gmail.com",
        addresses=[
            {"street": "123 street - PCHS", "city": "Karachi", "zip_code": "00345"},
            {"street": "942 street - Shah Faisal", "city": "Karachi", "zip_code": "00345"}
        ], # type: ignore
    )
    print(user_data.model_dump())
    
except ValidationError as e:
    print(f"ValidationError: {e}")   

print("\n-------------------------------------------------\n")     

try:
    user_data = UserWithAddress(
        id=4,
        name="areeba zafar",
        email="abc@gmail.com",
        addresses=[
            {"street": "123 street - PCHS", "city": "Karachi", "zip_code": "00345"},
            {"street": "942 street - Shah Faisal", "city": "Karachi", "zip_code": "00345"}
        ], # type: ignore
    )
    print(user_data.model_dump())
except ValidationError as e:
    print(f"ValidationError: {e}")
    
print("\n-------------------------------------------------\n")     
    
    
try:
    user_data = UserWithAddress(
        id=5,
        name="A",
        email="abc@gmail.com",
        addresses=[
            {"street": "123 street - PCHS", "city": "Karachi", "zip_code": "00345"},
            {"street": "942 street - Shah Faisal", "city": "Karachi", "zip_code": "00345"}
        ], # type: ignore
    )
    
    print(user_data.model_dump())
except ValidationError as e:
    print(f"ValidationError: {e}")

print("\n-------------------------------------------------\n")     
    
try:
    user_data = UserWithAddress(
        id=6,
        name="",
        email="abc@gmail.com",
        addresses=[
            {"street": "123 street - PCHS", "city": "Karachi", "zip_code": "00345"},
            {"street": "942 street - Shah Faisal", "city": "Karachi", "zip_code": "00345"}
        ], # type: ignore
    )
    
    print(user_data.model_dump())
    
except ValidationError as e:
    print(f"ValidationError: {e}")        

print("\n-------------------------------------------------\n")     
    