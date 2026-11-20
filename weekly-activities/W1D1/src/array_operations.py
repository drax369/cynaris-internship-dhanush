
"""Demonstrate NumPy broadcasting, vectorisation, and matrix multiplication."""

import numpy as np


def demonstrate_operations() -> None:
    """Perform common numerical operations without explicit Python loops."""
    # Broadcasting: add a 1D array to every row of a 2D array.
    matrix = np.array([[10, 20, 30], [40, 50, 60]])
    offset = np.array([1, 2, 3])
    broadcast_result = matrix + offset

    # Vectorisation: apply operations to every element simultaneously.
    numbers = np.array([1, 2, 3, 4, 5])
    squared = numbers**2
    scaled = numbers * 10

    # Matrix multiplication: (2, 3) multiplied by (3, 2).
    first_matrix = np.array([[1, 2, 3], [4, 5, 6]])
    second_matrix = np.array([[7, 8], [9, 10], [11, 12]])
    product = first_matrix @ second_matrix

    print("Broadcasting result:\n", broadcast_result)
    print("\nOriginal array:", numbers)
    print("Squared:", squared)
    print("Scaled:", scaled)
    print("\nMatrix multiplication result:\n", product)
    print("Product shape:", product.shape)


if __name__ == "__main__":
    demonstrate_operations()
