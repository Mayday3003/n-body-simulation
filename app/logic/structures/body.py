from app.logic.structures.vector import Vector2


class Body:
    def __init__(
        self,
        position: Vector2 | None = None,
        velocity: Vector2 | None = None,
        acceleration: Vector2 = Vector2(0, 0),
        mass: float = 3000000,
    ) -> None:
        if position is None:
            self.postiion = Vector2()
        else:
            self.position: Vector2 = position

        if velocity is None:
            self.position = Vector2()
        else:
            self.velocity: Vector2 = velocity
        self.acceleration: Vector2 = acceleration
        self.mass: float = mass

    def adjust_position(self, height: float, width: float) -> None:
        self.position.x = ((self.position.x + 1) / 2) * width
        self.position.y = ((self.position.y + 1) / 2) * height

if __name__ == '__main__':
    bodies = [Body() for _ in range(3)]
    other1 = Body()
    print(other1.position)
    other2 = Body()
    print(other2.position)
    for body in bodies:
        print(body.position)
