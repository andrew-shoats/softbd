import dataclasses as dc

@dc.dataclass
class Point:
    # Position
    x: float  
    y: float
    
    # Velocity
    vx: float
    vy: float

    # Force accumulator
    fx: float 
    fy: float