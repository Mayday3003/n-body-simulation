from typing import Optional
from random import uniform
from math import sqrt

class Vector3:
    def __init__(self, x: Optional[float] = None, y: Optional[float] = None, z: Optional[float] = None) -> None:
        if x is None:
            self.x: float = uniform(-1, 1)
        else:
            self.x: float = x

        if y is None:
            self.y: float = uniform(-1, 1)
        else:
            self.y: float = y

        if z is None:
            self.z: float = uniform(-1, 1)
        else:
            self.z: float = z

    def __add__(self, b: 'Vector3') -> 'Vector3':
        return Vector3(self.x + b.x, self.y + b.y, self.z + b.z)

    def __sub__(self, b: 'Vector3') -> 'Vector3':
        return Vector3(self.x - b.x, self.y - b.y, self.z - self.z)

    def __mul__(self, a: float) -> 'Vector3':
        return Vector3(self.x * a, self.y * a, self.z * a)

    def __repr__(self) -> str:
        return f'Vector3({self.x}, {self.y}, {self.z})'

    def __len__(self) -> float:
        return sqrt((self.x**2) + (self.y**2) + (self.z**2))
