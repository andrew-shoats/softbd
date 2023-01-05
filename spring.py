import dataclasses as dc

@dc.dataclass
class Spring:
    # Points indices
    i: int = 0
    j: int = 0
    
    # Rest length
    length: float = 0

    # Normal vector
    nx: float = 0
    ny: float = 0