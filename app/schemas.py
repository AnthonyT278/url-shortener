from datetime import datetime
from pydantic import BaseModel, HttpUrl, EmailStr, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LinkCreate(BaseModel):
    original_url: HttpUrl
    custom_code: str | None = None


class LinkOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    short_code: int 
    original_url: str
    clicks: int
    created_at: datetime


class LinkStats(BaseModel):
    short_code: str
    total_clicks: int 
    created_at: datetime
