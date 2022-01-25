import numpy as np

from gameAI.movement.movementStructures.kinematic import Kinematic
from gameAI.movement.movementStructures.static import Static
from gameAI.movement.movementStructures.steeringOutput import SteeringOutput
from gameAI.utils.movementUtils import normalize


class KinematicSeek:
    """
    Seek a path from a character to a target
    """

    def __init__(
        self, character: Static, target: Kinematic, max_speed: float, radius: float = 0
    ) -> None:
        self.character = character
        self.target = target
        self.max_speed = max_speed
        self.radius = radius

    def get_steering(
        self, set_orientation: bool = True, seek: bool = True, arrive: bool = False
    ) -> SteeringOutput:
        """
        Returns the steering output from the character to the target

        Args:
            set_orientation (optional): Whether or not to set orientation
            movement directions
            seek (optional): Whether the algorithm seeks or flee
            arrive (optional): Whether the algorithm uses distance to
            set speed. Not done for fleeing
        """

        result = SteeringOutput([], 0)

        # Get direction from character to target
        if seek:
            linear = self.target.position - self.character.position
        else:
            linear = self.character.position - self.target.position

        # Distance fom character to target
        distance = np.linalg.norm(linear)

        # Normalize speed
        linear = normalize(linear)

        # Set velocity in that direction speed depending on distance
        if arrive and distance / 5 < self.max_speed:
            print(distance)
            linear = linear * (distance / 5)

        else:
            linear = linear * self.max_speed

        # If close to the target, do nothing
        if distance < self.radius:
            result = SteeringOutput(np.array([0, 0]), 0)
        else:

            result = SteeringOutput(linear, 0)

        if set_orientation:
            self.character.new_orientation()

        return result
