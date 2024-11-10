from app.logic.structures.vector import Vector2


class Body:
    def __init__(
        self,
        position: Vector2 = Vector2(),
        velocity: Vector2 = Vector2(),
        acceleration: Vector2 = Vector2(0, 0),
        mass: float = 3000000,
    ) -> None:
        self.position: Vector2 = position
        self.velocity: Vector2 = velocity
        self.acceleration: Vector2 = acceleration
        self.mass: float = mass

    def adjust_position(self, height: float, width: float) -> None:
        self.position.x = ((self.position.x + 1) / 2) * width
        self.position.y = ((self.position.y + 1) / 2) * height
