from app.logic.structures.vector import Vector2
import random

class Body:
    def __init__(
        self,
        position: Vector2 | None = None,
        velocity: Vector2 | None = None,
        acceleration: Vector2 = Vector2(0, 0),
        mass: float = 3000000,
        color: tuple[int, int, int] = None,
    ) -> None:
        if position is None:
            self.position = Vector2()
        else:
            self.position: Vector2 = position

        if velocity is None:
            self.velocity = Vector2()
        else:
            self.velocity: Vector2 = velocity
        self.acceleration: Vector2 = acceleration
        self.mass: float = mass
        self.color = color
            
        self.__post_init__()

    def __post_init__(self):
        if self.color is None:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def adjust_position(self, height: float, width: float) -> None:
        self.position.x = ((self.position.x + 1) / 2) * width
        self.position.y = ((self.position.y + 1) / 2) * height
