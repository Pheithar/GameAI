import numpy as np

"""
Additional functions for the movement algorithms
"""

FRICCION = 0.995


def normalize(vector: np.ndarray) -> np.ndarray:
    """
    Normalizes input vector to have a lenght of 1 if
    the vector is not a 0-vector. Otherwise, it is left unchanged
    """

    vec_norm = np.linalg.norm(vector)
    if vec_norm != 0:
        vector = vector / vec_norm
    return vector
