from app.logic.structures.vector import Vector3


class Body:
    def __init__(
        self,
        position: Vector3 = Vector3(),
        velocity: Vector3 = Vector3(),
        acceleration: Vector3 = Vector3(0, 0, 0),
        mass: float = 3000000,
    ) -> None:
        self.position: Vector3 = position
        self.velocity: Vector3 = velocity
        self.acceleration: Vector3 = acceleration
        self.mass: float = mass

    def adjust_position(self, height: float, width: float, depth: float) -> None:
        self.position.x *= width
        self.position.y *= height
        self.position.z *= depth
