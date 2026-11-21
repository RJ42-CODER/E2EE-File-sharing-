from pydantic import BaseModel, EmailStr, Field


# why two schemas? one for request and one for response. This is because we don't want to expose the password in the response.
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=12, max_length=132)

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool

    model_config = {
        "from_attributes": True
    }

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1,max_length=128)
