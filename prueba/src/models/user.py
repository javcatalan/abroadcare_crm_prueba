from turtle import st
from pydantic import BaseModel
from typing import Optional

class survey(BaseModel):
    id: Optional[str]
    uuidApplication: str
    uuidQuestion: str
    responseOptions: str
    responseSpecify: str

class applications(BaseModel):
    id: Optional[str]
    uuid: str
    firstName: str
    lastName: str
    countryCode: str
    phoneNumber: str
    email: str
    history: object
    utmData: object


class questions(BaseModel):
    id: Optional[str]
    uuid: str
    questions:str
    commentary: bool
    options: object
    specify: str
    specifyWhen: str
    responseOptions: str
    responseSpecifyType: str
    tags: str
    isOpen: bool
    placeholder: str

# from pydantic import BaseModel
# from typing import Optional

# class User(BaseModel):
#     id: Optional[str]
#     name: str
#     email: str
#     password: str