from pydantic import BaseModel

class Mixer(BaseModel):

    brand: str
    cost: int
    color: str
    wattage: int