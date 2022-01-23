import numpy as np


class SteeringOutput:
    """
    Output from steering behaviours
    """

    def __init__(self, linear: np.ndarray, angular: float) -> None:
        self.linear = linear
        self.angular = angular
