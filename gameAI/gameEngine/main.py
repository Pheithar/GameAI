import sys
from typing import Tuple

import numpy as np
import pygame

from gameAI.movement.movementStructures.static import Static
from gameAI.utils import actions


class PyGame:
    def __init__(self, screen_size: Tuple[int, int], wait_time: int) -> None:

        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()

        self.wait_time = wait_time

    def init(self, action: str):
        """
        Run the action from the module and play it on screen
        """

        pygame.init()

        while True:

            self.clock.tick(self.wait_time)

            self.screen.fill((0, 0, 0))

            # ACTIONS
            if action == actions.ACTION_MOVEMENT_SEEK:
                self.display_static(Static(np.array([100, 100]), 75))

            # EVENTS
            for event in pygame.event.get():

                # Close game
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

    def display_static(self, static: Static) -> None:

        position = np.array([[0, 10], [10, 10], [5, 0]])

        # Rotate
        position = [
            pygame.math.Vector2(x[0], x[1]).rotate(static.orientation) for x in position
        ]

        # Move
        position = position + static.position

        pygame.draw.polygon(self.screen, (255, 0, 0), position)
