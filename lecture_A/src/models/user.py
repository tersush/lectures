from pydantic import BaseModel, Field, EmailStr, AnyHttpUrl, SecretStr, UUID8

class User(BaseModel):
    id: UUID int 
    email: EnailStr = field(default=uuid4, description= "User IDuv add pydantuc")
    name: str
    age: int
    personal_website