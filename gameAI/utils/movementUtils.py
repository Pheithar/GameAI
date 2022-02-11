import numpy as np

"""
Additional functions for the movement algorithms
"""

FRICCION = 0.995


def normalize(vector: np.ndarray) -> np.ndarray:
    """
    Normalizes input vector to have a lenght of 1 if
    the vector is not a 0-vector. Otherwise, it is left unchanged

    Args:
        vector: vector to normalize

    Returns:
        vector: normalized vector
    """

    vec_norm = np.linalg.norm(vector)
    if vec_norm != 0:
        vector = vector / vec_norm
    return vector


def random_binomial() -> float:
    """
    Creates a random number between -1 and 1 where the numbers close
    to 0 are more likely to appear

    Returns:
        rand_num: random number between -1 and 1
    """

    rand_num = np.random.rand() - np.random.rand()

    return rand_num


def as_vector(orientation: float) -> np.ndarray:
    """
    Transform the orientation from floa type to vecor shape

    Args:
        orientation: orientation in float type (must be degrees)

    Returns:
        orientation_vector: orientation in type vector
    """

    orientation_vector = np.array(
        [np.sin(np.deg2rad(orientation)), -np.cos(np.deg2rad(orientation))]
    )

    return orientation_vector
