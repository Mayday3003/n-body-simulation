from time import sleep
import pygame
from app.logic.structures.vector import Vector2
from app.logic.structures.body import Body
from app.logic.simulation import Simulation
from random import randint


def random_color() -> tuple[int, int, int]:
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Interface:

    BLACK = (0, 0, 0)

    def __init__(self, width: float, height: float) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        self.simulation = Simulation(width=width, height=height)

    def __draw_body(self, body: Body) -> None:
        pygame.draw.circle(
            self.window, random_color(), (body.position.x, body.position.y), 5
        )

    def init(self) -> None:
        running = True

        while running:
            self.window.fill(Interface.BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.simulation.add_body(Body(position=Vector2(x, y)))


            for body in self.simulation.bodies:
                self.__draw_body(body)


            self.simulation.calculate_next_step()
            sleep(0.5)

    def finish(self):
        pygame.quit()
