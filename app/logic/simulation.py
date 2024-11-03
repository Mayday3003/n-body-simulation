from app.logic.structures.body import Body
from app.logic.structures.vector import Vector3


class Simulation:

    INITIAL_BODIES: int = 20
    GRAVITATIONAL_CONSTANT: float = 1
    DELTA_T: float = 0.0001
    WIDTH: float = 500
    HEIGHT: float = 500
    DEPTH: float = 500
    CUTTOF: float = 1000000

    def __init__(self) -> None:
        self.bodies: list[Body] = [Body() for _ in range(Simulation.INITIAL_BODIES)]
        for i in self.bodies:
            i.adjust_position(Simulation.HEIGHT, Simulation.WIDTH, Simulation.DEPTH)

    def calculate_next_step(self):
        for i in self.bodies:
            sum_forces_i: Vector3 = Vector3(0, 0, 0)
            for j in self.bodies:
                if i is j:
                    continue

                distance_vector: Vector3 = j.position - i.position
                magnitude_distance: float = distance_vector.size()

                if magnitude_distance > Simulation.CUTTOF:
                    continue

                force_ij: Vector3 = (
                    distance_vector
                    * 1
                    * (
                        Simulation.GRAVITATIONAL_CONSTANT
                        * i.mass
                        * j.mass
                        * ((magnitude_distance + 10) ** -3)
                    )
                )
                sum_forces_i = sum_forces_i + force_ij

            i.acceleration = sum_forces_i * (i.mass**-1)
            i.velocity = i.velocity + (i.acceleration * Simulation.DELTA_T)
            i.position = i.position + (i.velocity * Simulation.DELTA_T)
