from math import sqrt
from random import uniform
from typing import Optional


class Vector2:
    def __init__(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
    ) -> None:
        if x is None:
            self.x: float = uniform(-1, 1)
        else:
            self.x: float = x

        if y is None:
            self.y: float = uniform(-1, 1)
        else:
            self.y: float = y

    def size(self) -> float:
        return sqrt((self.x**2) + (self.y**2))

    def __add__(self, b: "Vector2") -> "Vector2":
        return Vector2(self.x + b.x, self.y + b.y)

    def __sub__(self, b: "Vector2") -> "Vector2":
        return Vector2(self.x - b.x, self.y - b.y)

    def __mul__(self, a: float) -> "Vector2":
        return Vector2(self.x * a, self.y * a)

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
