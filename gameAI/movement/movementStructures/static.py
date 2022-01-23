import numpy as np


class Static:
    """
    Static element
    """

    def __init__(self, position: np.ndarray, orientation: float) -> None:
        self.position = position
        self.orientation = orientation
