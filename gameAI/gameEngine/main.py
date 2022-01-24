import sys
from typing import Tuple

import numpy as np
import pygame

from gameAI.movement.movementStructures.static import Static
from gameAI.utils.pygameUtils import rotate_polygon_2d
from gameAI.utils import colors
from gameAI.utils import actions

TRIANGLE_IN_ZERO = np.array([[-5, 5], [5, 5], [0, -5]])


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

        pygame.display.set_caption(action)

        while True:

            self.clock.tick(self.wait_time)

            self.screen.fill((0, 0, 0))

            # ACTIONS
            if action == actions.ACTION_MOVEMENT_SEEK:
                self.display_static(Static(np.array([100, 100]), 180))

            # EVENTS
            for event in pygame.event.get():

                # Close game
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

    def display_static(self, static: Static) -> None:

        position = TRIANGLE_IN_ZERO

        # Move
        position = position + static.position

        # Rotate
        position = rotate_polygon_2d(
            static.position, position, static.orientation
        )

        pygame.draw.polygon(self.screen, colors.GREEN, list(position))
