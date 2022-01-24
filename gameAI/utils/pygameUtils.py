import math

import numpy as np

"""
Multiple functions to help in pygame
"""


def rotate_polygon_2d(
    current_position: np.ndarray, points: np.ndarray, angle: float
) -> np.ndarray:
    """
    Rotates a polygon in a 2 dimensional environment by an angle.
    Angle must be degree
    """

    angle = math.radians(angle)

    # Rotation matrix :
    #   [[cos(theta), -sin(theta)],
    #    [sin(theta),  cos(theta)]]
    rotation_matrix = np.array(
        [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]
    )

    # Move to the origin
    origin_points = points - current_position

    rotated_origin_points = []

    for origin_point in origin_points:
        rotated_origin_points.append(rotation_matrix.dot(origin_point))

    rotated_origin_points_np = np.array(rotated_origin_points)

    rotated_points = rotated_origin_points_np + current_position

    return rotated_points
