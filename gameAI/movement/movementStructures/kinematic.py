import numpy as np

from gameAI.movement.movementStructures.steeringOutput import SteeringOutput


class Kinematic:
    """
    Element with movement
    """

    def __init__(
        self,
        position: np.ndarray,
        orientation: float,
        velocity: np.ndarray,
        rotation: float,
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
        self.velocity = self.velocity + steering.linear * time
        self.rotation = self.rotation + steering.angular * time
