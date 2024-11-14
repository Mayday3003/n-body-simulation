import time
import pygame
from app.logic.structures.vector import Vector2
from app.logic.structures.body import Body
from app.logic.simulation import Simulation


class Interface:

    BLACK = (0, 0, 0)

    def __init__(self, width: float, height: float) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        self.simulation = Simulation(width=width, height=height)
        self.font = pygame.font.SysFont("Arial", 30)

    def __draw_body(self, body: Body) -> None:
        pygame.draw.circle(
            self.window, body.color, (int(body.position.x), int(body.position.y)), 5
        )

    def init(self) -> None:
        running = True
        start_time = time.time()

        while running:
            time_elapsed = time.time() - start_time
            if time_elapsed >= self.simulation.CUTTOF:
                print("Simulation reached cutoff time.")
                running = False
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.simulation.add_body(Body(position=Vector2(x, y)))

            self.window.fill(Interface.BLACK)
            for body in self.simulation.bodies:
                self.__draw_body(body)

            # draw text
            text_bodies = self.font.render(
                "bodies: " + str(len(self.simulation.bodies)), True, (255, 255, 255)
            )
            text_energy = self.font.render(
                "energy: " + str(self.simulation.get_total_energy()),
                True,
                (255, 255, 255),
            )
            text_energy_rect = text_energy.get_rect(center=(200, 200))
            text_bodies_rect = text_bodies.get_rect(center=(60, 80))
            self.window.blit(text_bodies, text_bodies_rect)
            self.window.blit(text_energy, text_energy_rect)

            pygame.display.flip()

            self.simulation.calculate_next_step()

    def finish(self):
        pygame.quit()
