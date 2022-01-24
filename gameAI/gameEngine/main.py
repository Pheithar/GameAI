import sys
import time
from typing import Tuple

import numpy as np
import pygame

from gameAI.movement.kinematicMovement.seek import KinematicSeek
from gameAI.movement.movementStructures.kinematic import Kinematic
from gameAI.movement.movementStructures.static import Static
from gameAI.utils import actions, colors
from gameAI.utils.pygameUtils import rotate_polygon_2d

TRIANGLE_IN_ZERO = np.array([[-5, 5], [5, 5], [0, -5]])

MOVEMENT_SPEED = 75


class PyGame:
    def __init__(self, screen_size: Tuple[int, int], frame_rate: int) -> None:

        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()

        self.frame_rate = frame_rate

    def init(self, action: str):
        """
        Run the action from the module and play it on screen
        """

        pygame.init()

        # Caption
        pygame.display.set_caption(action)

        # Initialize time
        prev_time = time.time()

        # Setup depending on action
        if action == actions.ACTION_MOVEMENT_SEEK:

            target = Static(np.array([512, 256]), 180)
            character = Kinematic(np.array([500, 50]), 0, np.array([0, 0]), 0)

            kseek = KinematicSeek(character, target, MOVEMENT_SPEED)

        while True:

            self.clock.tick(self.frame_rate)

            self.screen.fill(colors.BLACK)

            # time with deltatime to avoid framerate tied with speed
            now = time.time()
            dt = now - prev_time
            prev_time = now

            # ACTIONS
            if action == actions.ACTION_MOVEMENT_SEEK:

                self.display_static(target)

                self.display_static(character, color=colors.GREEN)

                steering = kseek.get_steering()

                character.update(steering, dt)

            # EVENTS
            for event in pygame.event.get():

                # Close game
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

    def display_static(
        self, static: Static, color: Tuple[int, int, int] = colors.RED
    ) -> None:
        """
        Draws on the screen the input static
        """

        position = TRIANGLE_IN_ZERO

        # Move
        position = position + static.position

        # Rotate
        position = rotate_polygon_2d(static.position, position, static.orientation)

        # Draw
        pygame.draw.polygon(self.screen, color, list(position))
