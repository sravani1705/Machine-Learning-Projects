from pydantic import BaseModel
from typing import Literal

class cardio(BaseModel):
    age: int 
    gender: Literal[1, 2]
    height: int 
    weight: float 
    ap_hi: int
    ap_lo: int
    cholestrol: Literal[1, 2, 3]
    gluc: Literal[1, 2, 3]
    smoke: Literal[0, 1]
    alco: Literal[0, 1]
    active: Literal[0, 1]
