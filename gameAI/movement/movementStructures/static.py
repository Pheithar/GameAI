import numpy as np


class Static:
    """
    Static element. Orientation must be passed in angles
    """

    def __init__(self, position: np.ndarray, orientation: float) -> None:
        self.position = position
        self.orientation = orientation
