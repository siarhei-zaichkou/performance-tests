from pydantic import BaseModel, Field, EmailStr


# Базовая модель с общими полями
class UserBase(BaseModel):
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


# Модель пользователя
class UserSchema(UserBase):
    id: str


# Модель запроса при создании пользователя
class CreateUserRequestSchema(UserBase):
    pass


# Модель ответа при создании пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema
