from gameAI.movement.movementStructures.kinematic import Kinematic
from gameAI.movement.movementStructures.static import Static
from gameAI.movement.movementStructures.steeringOutput import SteeringOutput
from gameAI.utils.movementUtils import normalize


class KinematicSeek:
    """
    Seek a path from a character to a target
    """

    def __init__(self, character: Static, target: Kinematic, max_speed: float) -> None:
        self.character = character
        self.target = target
        self.max_speed = max_speed

    def get_steering(self) -> SteeringOutput:
        """
        Returns the steering output from the character to the target
        """

        result = SteeringOutput([], 0)

        # Get direction from character to target
        result.linear = self.target.position - self.character.position

        # Set velocity in that direction at full speed
        result.linear = normalize(result.linear)
        result.linear = result.linear * self.max_speed

        return result
