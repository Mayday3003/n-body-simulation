import pygame
from app.logic.structures.simulation import Simulation

class SimulationRenderer:
    def __init__(self, simulation, screen_width=800, screen_height=800):
        pygame.init()
        self.simulation = simulation
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("N-Body Simulation")
        self.clock = pygame.time.Clock()
        self.running = True

    def draw_body(self, body: Body):
        x = int(body.position.x)
        y = int(body.position.y)
        radius = max(2, int(body.mass ** (1 / 3) / 100))
        pygame.draw.circle(self.screen, (255, 255, 255), (x, y), radius)

    def render(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))  
            self.simulation.calculate_next_step()  

            for body in self.simulation.bodies:
                self.draw_body(body)

            pygame.display.flip()
            self.clock.tick(60)  

        pygame.quit()

