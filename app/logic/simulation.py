from app.logic.structures.body import Body
from app.logic.structures.vector import Vector3


class Simulation:

    def __init__(
        self,
        initial_bodies: int = 3,
        height: float = 500,
        width: float = 500,
        depth: float = 500,
        delta_t: float = 0.0001,
        gravitational_constant: float = 1,
        cuttof: float = 1000000,
    ) -> None:

        self.CUTTOF: float = cuttof
        self.GRAVITATIONAL_CONSTANT: float = gravitational_constant
        self.DELTA_T: float = delta_t

        self.bodies: list[Body] = [Body() for _ in range(initial_bodies)]
        for i in self.bodies:
            i.adjust_position(height, width, depth)

    def calculate_next_step(self):
        for i in self.bodies:
            sum_forces_i: Vector3 = Vector3(0, 0, 0)
            for j in self.bodies:
                if i is j:
                    continue

                distance_vector: Vector3 = j.position - i.position
                magnitude_distance: float = distance_vector.size()

                if magnitude_distance > self.CUTTOF:
                    continue

                force_ij: Vector3 = (
                    distance_vector
                    * 1
                    * (
                        self.GRAVITATIONAL_CONSTANT
                        * i.mass
                        * j.mass
                        * ((magnitude_distance + 10) ** -3)
                    )
                )
                sum_forces_i = sum_forces_i + force_ij

            i.acceleration = sum_forces_i * (i.mass**-1)
            i.velocity = i.velocity + (i.acceleration * self.DELTA_T)
            i.position = i.position + (i.velocity * self.DELTA_T)
