from pydantic import BaseModel, ValidationError


# create a model with BaseModel
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field with default None
    
user_data = {"id": 1, "name": "Areeba", "email": "areebazafar@gmail.com", "age": 19} 

user = User(**user_data) 

print(user) # id=1 name='Areeba' email='areebazafar@gmail.com' age=19
print("\n", user.model_dump()) # model.dump() returns data in dictionary 
# {'id': 1, 'name': 'Areeba', 'email': 'areebazafar@gmail.com', 'age': 19}


# invalid data raise an error so we handle it on try except
try:
    invalid_user = User( id="not_an_int", name="Sara", email="sarachohan@gmail.com") # type: ignore
except ValidationError as e:
    print(f"Validation Error: {e}")    
    