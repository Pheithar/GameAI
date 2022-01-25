import numpy as np


class Static:
    """
    Static element. Orientation must be passed in angles
    """

    def __init__(self, position: np.ndarray, orientation: float = 0) -> None:
        self.position = position
        self.orientation = orientation
