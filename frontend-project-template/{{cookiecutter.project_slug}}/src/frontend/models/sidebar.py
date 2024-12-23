from pydantic import BaseModel

class SideBarModel(BaseModel):
    first_number: float
    second_number: float