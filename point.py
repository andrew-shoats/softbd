import dataclasses as dc

@dc.dataclass
class Point:
    # Position
    x: float = 0
    y: float = 0
    
    # Velocity
    vx: float = 0
    vy: float = 0

    # Force accumulator
    fx: float = 0
    fy: float = 0