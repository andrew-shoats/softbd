import dataclasses as dc

@dc.dataclass
class Spring:
    # Points indices
    i: int  
    j: int
    
    # Rest length
    length: float

    # Normal vector
    nx: float
    ny: float