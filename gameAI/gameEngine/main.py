import sys
import time
from typing import Tuple, Union

import numpy as np
import pygame

from gameAI.movement.kinematicMovement.seek import KinematicSeek
from gameAI.movement.movementStructures.kinematic import Kinematic
from gameAI.movement.movementStructures.static import Static
from gameAI.utils import actions, colors
from gameAI.utils.pygameUtils import rotate_polygon_2d

TRIANGLE_IN_ZERO = np.array([[-5, 5], [5, 5], [0, -5]])

MOVEMENT_SPEED = 100


class PyGame:
    def __init__(self, screen_size: Tuple[int, int], frame_rate: int) -> None:

        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()

        self.frame_rate = frame_rate

    def init(self, action: str) -> None:
        """
        Run the action from the module and play it on screen

        Args:
            action: the action to run
        """

        pygame.init()

        # Caption
        pygame.display.set_caption(action)

        # Initialize time
        prev_time = time.time()

        #####################################################################
        # Setup depending on action
        #####################################################################
        # --------------
        # MOVEMENT ACTIONS
        # --------------
        if action in actions.MOVEMENT_ACTIONS:
            target, character, kseek = self.movement_actions_setup(action)

        while True:

            self.clock.tick(self.frame_rate)

            self.screen.fill(colors.BLACK)

            # time with deltatime to avoid framerate tied with speed
            now = time.time()
            dt = now - prev_time
            prev_time = now

            #################################################################
            # ACTIONS
            #################################################################
            # --------------
            # MOVEMENT ACTIONS
            # --------------
            self.run_movement_actions(action, target, character, kseek, dt)

            # EVENTS
            for event in pygame.event.get():

                # Close game
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

    def movement_actions_setup(
        self, action: str
    ) -> Tuple[Static, Kinematic, KinematicSeek]:
        """
        Setup the appropirate parameters given that it is a movement action

        Args:
            action: action to do the setup for

        Return:
            target: target of the movement action
            character: character that does the moving
            kseek: kinematic seek instance with appropriate parameters
        """

        # --------------
        # ACTION_MOVEMENT_SEEK
        # --------------
        if action == actions.ACTION_MOVEMENT_SEEK:

            target = Static(np.array([512, 256]))
            character = Kinematic(np.array([50, 50]))

            kseek = KinematicSeek(character, target, MOVEMENT_SPEED)
        # --------------
        # ACTION_MOVEMENT_FLEE
        # --------------
        elif action == actions.ACTION_MOVEMENT_FLEE:
            target = Static(np.array([5, 5]))
            character = Kinematic(np.array([7, 7]))

            kseek = KinematicSeek(character, target, MOVEMENT_SPEED)
        # --------------
        # ACTION_MOVEMENT_SEEK_ARRIVE
        # --------------
        elif action == actions.ACTION_MOVEMENT_SEEK_ARRIVE:

            target = Static(np.array([512, 256]))
            character = Kinematic(np.array([50, 50]))

            kseek = KinematicSeek(character, target, MOVEMENT_SPEED, 20)
        # --------------
        # ACTION_MOVEMENT_WANDERING
        # --------------
        elif action == actions.ACTION_MOVEMENT_WANDERING:

            target = None
            character = Kinematic(np.array([512, 450]))

            kseek = KinematicSeek(character, None, MOVEMENT_SPEED / 10)

        return target, character, kseek

    def run_movement_actions(
        self,
        action: str,
        target: Static,
        character: Kinematic,
        kseek: KinematicSeek,
        dt: float,
    ) -> None:
        """
        Runs the appropriate movement action

        Args:
            action: action to run
            target: target of the action
            character: character that runs the action
            dt: timestep of current loop
        """
        # --------------
        # ACTION_MOVEMENT_SEEK
        # --------------
        if action == actions.ACTION_MOVEMENT_SEEK:

            self.display_element(target)
            self.display_element(character, color=colors.GREEN)
            steering = kseek.get_steering()
            character.update(steering, dt)

        # --------------
        # ACTION_MOVEMENT_FLEE
        # --------------
        elif action == actions.ACTION_MOVEMENT_FLEE:
            self.display_element(target)
            self.display_element(character, color=colors.GREEN)
            steering = kseek.get_steering(seek=False)
            character.update(steering, dt)
        # --------------
        # ACTION_MOVEMENT_SEEK_ARRIVE
        # --------------
        elif action == actions.ACTION_MOVEMENT_SEEK_ARRIVE:

            self.display_element(target)
            self.display_element(character, color=colors.GREEN)
            steering = kseek.get_steering(arrive=True)
            character.update(steering, dt)
        # --------------
        # ACTION_MOVEMENT_WANDERING
        # --------------
        elif action == actions.ACTION_MOVEMENT_WANDERING:

            # self.display_element(target)
            self.display_element(character, color=colors.GREEN)
            steering = kseek.get_wandering()
            character.update(steering, dt)

    def display_element(
        self,
        element: Union[Static, Kinematic],
        color: Tuple[int, int, int] = colors.RED,
    ) -> None:
        """
        Draws on the screen the input element

        Args:
            element: Element to draw
            color (optional): color to draw the element with
        """

        position = TRIANGLE_IN_ZERO

        # Move
        position = position + element.position

        # Rotate
        position = rotate_polygon_2d(element.position, position, element.orientation)

        # Draw
        pygame.draw.polygon(self.screen, color, list(position))
