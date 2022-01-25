import math

import numpy as np

from gameAI.movement.movementStructures.steeringOutput import SteeringOutput
from gameAI.utils.movementUtils import FRICCION


class Kinematic:
    """
    Element with movement
    """

    def __init__(
        self,
        position: np.ndarray,
        orientation: float = 0,
        velocity: np.ndarray = np.array([0, 0]),
        rotation: float = 0,
    ) -> None:
        self.position = position
        self.orientation = orientation
        self.velocity = velocity
        self.rotation = rotation

    def update(self, steering: SteeringOutput, time: float) -> None:
        """
        Update position and orientation manually

        Args:
            steering: output from a steering algorithm
            time: how much time has passed since last frame
        """

        # Update position and rotation
        self.position = self.position + self.velocity * time
        self.orientation = self.orientation + self.rotation * time

        # Update velocity and rotation
        self.velocity = self.velocity * FRICCION + steering.linear * time
        self.rotation = self.rotation + steering.angular * time

    def new_orientation(self) -> None:
        """
        Set orientation in the direction of the movement
        """
        self.orientation = math.degrees(math.atan2(self.velocity[0], -self.velocity[1]))
