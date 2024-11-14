from app.logic.structures.body import Body
from app.logic.structures.vector import Vector2


class Simulation:

    def __init__(
        self,
        initial_bodies: int = 3,
        height: float = 500,
        width: float = 500,
        delta_t: float = 0.0001,
        gravitational_constant: float = 1,
        cuttof: float = 1000000,
    ) -> None:

        self.CUTTOF: float = cuttof
        self.GRAVITATIONAL_CONSTANT: float = gravitational_constant
        self.DELTA_T: float = delta_t

        self.bodies: list[Body] = [Body() for _ in range(initial_bodies)]
        for i in self.bodies:
            i.adjust_position(height, width)

    def calculate_next_step(self):
        for i in self.bodies:
            sum_forces_i: Vector2 = Vector2(0, 0)
            for j in self.bodies:
                if i is j:
                    continue

                distance_vector: Vector2 = j.position - i.position
                magnitude_distance: float = distance_vector.size()

                if magnitude_distance > self.CUTTOF:
                    continue

                force_ij: Vector2 = (
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

    def add_body(self, body: Body) -> None:
        self.bodies.append(body)

    def get_kinetic_energy(self) -> float:
        results: float = 0.0
        for body in self.bodies:
            results += 0.5 * body.mass * (body.velocity**2)
        return results

    def get_potential_energy(self) -> float:
        result: float = 0.0
        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                distance_vector = self.bodies[i].position - self.bodies[j].position
                if distance_vector != Vector2(0, 0):
                    result += (
                        -1
                        * (
                            self.GRAVITATIONAL_CONSTANT
                            * self.bodies[i].mass
                            * self.bodies[j].mass
                        )
                        / distance_vector.size()
                    )
        return result

    def get_total_energy(self) -> float:
        return self.get_potential_energy() + self.get_kinetic_energy()
