# W1D1 — Python for ML: NumPy Fundamentals

## Overview

This activity explores NumPy fundamentals through practical array operations and statistical analysis of the Iris dataset.

## Learning Objectives

- Create and inspect 1D, 2D, and 3D NumPy arrays.
- Understand array shapes and dimensions.
- Perform broadcasting and vectorised operations.
- Perform matrix multiplication.
- Calculate mean, standard deviation, and correlation.

## Technology Stack

- Python 3.11
- NumPy
- Jupyter Notebook

## Project Structure

```text
W1D1/
├── data/
│   └── iris.csv
├── evidence/
├── notebooks/
│   └── numpy_fundamentals.ipynb
├── src/
│   ├── array_basics.py
│   ├── array_operations.py
│   └── dataset_statistics.py
└── README.md
```

## Setup Instructions

Activate the project's virtual environment from the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```powershell
python -m pip install numpy notebook ipykernel
```

## Execution

Run the Python scripts from the repository root:

```powershell
python weekly-activities/W1D1/src/array_basics.py
python weekly-activities/W1D1/src/array_operations.py
python weekly-activities/W1D1/src/dataset_statistics.py
```

Launch Jupyter Notebook:

```powershell
python -m notebook weekly-activities/W1D1/notebooks
```

Select the `Python (Cynaris W1D1)` kernel.

## Dataset

**Dataset:** Iris

**Source:** UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/53/iris

The dataset contains 150 observations, four numerical flower measurements, and one species label.

The numerical measurements used are:

- Sepal length
- Sepal width
- Petal length
- Petal width

**Attribution:** UCI Machine Learning Repository
**License:** CC BY 4.0

## Implementation Details

### 1. Array Fundamentals

Created 1D, 2D, and 3D arrays and inspected their shapes, dimensions, and data types.

### 2. Broadcasting

Added a one-dimensional vector to each row of a two-dimensional matrix using NumPy broadcasting.

### 3. Vectorisation

Performed element-wise squaring and scaling without explicit Python loops.

### 4. Matrix Multiplication

Multiplied matrices with compatible dimensions using the `@` operator.

### 5. Statistical Analysis

Used NumPy to calculate:

- Feature-wise mean.
- Population standard deviation (`ddof=0`).
- Pairwise Pearson correlation matrix.

## Results

| Feature      |  Mean | Standard Deviation |
| ------------ | ----: | -----------------: |
| Sepal length | 5.843 |              0.825 |
| Sepal width  | 3.054 |              0.432 |
| Petal length | 3.759 |              1.759 |
| Petal width  | 1.199 |              0.761 |

The strongest positive correlation was between petal length and petal width (0.963).

## Learning Outcomes

This activity demonstrated how NumPy supports efficient numerical computation through multidimensional arrays, broadcasting, vectorisation, matrix multiplication, and statistical functions.

## Evidence

Execution screenshots and notebook outputs are stored in the `evidence/` directory.
