
"""Explore NumPy arrays, dimensions, shapes, and data types."""

import numpy as np


def demonstrate_arrays() -> None:
    """Create and inspect one-dimensional, two-dimensional, and three-dimensional arrays."""
    one_dimensional = np.array([10, 20, 30, 40])
    two_dimensional = np.array([[1, 2, 3], [4, 5, 6]])
    three_dimensional = np.array(
        [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ]
    )

    arrays = {
        "1D": one_dimensional,
        "2D": two_dimensional,
        "3D": three_dimensional,
    }

    for name, array in arrays.items():
        print(f"\n{name} Array:")
        print(array)
        print("Shape:", array.shape)
        print("Dimensions:", array.ndim)
        print("Data type:", array.dtype)


if __name__ == "__main__":
    demonstrate_arrays()
