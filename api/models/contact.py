import os
from pydantic import BaseModel, EmailStr, constr
from dotenv import load_dotenv
load_dotenv('.env.local')


class ContactProperties(BaseModel):
    email: EmailStr
    firstname: constr(min_length=2, max_length=20)
    lastname: constr(min_length=2, max_length=20)
    phone: constr(min_length=10, max_length=20)
    website: constr(regex=r'^[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}$')# noqa
    estado_clickup: str = os.getenv("HUBSPOT_STATUS_PENDING")


class ContactCreateRequest(BaseModel):
    properties: ContactProperties
