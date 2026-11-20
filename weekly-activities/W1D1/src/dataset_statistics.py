
"""Calculate descriptive statistics for the UCI Iris dataset."""

from pathlib import Path

import numpy as np


def calculate_statistics() -> None:
    """Load Iris measurements and calculate descriptive statistics."""
    data_path = Path(__file__).resolve().parents[1] / "data" / "iris.csv"

    feature_names = [
        "Sepal length",
        "Sepal width",
        "Petal length",
        "Petal width",
    ]

    measurements = np.genfromtxt(
        data_path,
        delimiter=",",
        usecols=(0, 1, 2, 3),
        dtype=np.float64,
        autostrip=True,
    )

    measurements = np.atleast_2d(measurements)

    if not np.isfinite(measurements).all():
        raise ValueError("Dataset contains missing or invalid measurements.")

    means = np.mean(measurements, axis=0)
    standard_deviations = np.std(measurements, axis=0)
    correlation_matrix = np.corrcoef(measurements, rowvar=False)

    print("Dataset shape:", measurements.shape)

    print("\nMean:")
    for name, value in zip(feature_names, means):
        print(f"{name}: {value:.3f}")

    print("\nStandard deviation:")
    for name, value in zip(feature_names, standard_deviations):
        print(f"{name}: {value:.3f}")

    print("\nCorrelation matrix:")
    print(np.round(correlation_matrix, 3))


if __name__ == "__main__":
    calculate_statistics()
