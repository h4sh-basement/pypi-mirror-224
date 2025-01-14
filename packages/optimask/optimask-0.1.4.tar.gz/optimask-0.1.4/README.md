# OptiMask: A Python Package for Computing Optimal Masks in Matrix NaN Data Removal

Introducing OptiMask, a comprehensive Python package designed to facilitate the seamless computation of optimal masks for efficient removal of NaN (Not-a-Number) data from matrices. The core principle behind OptiMask is to generate masks that result in processed matrices devoid of NaN values while retaining the maximum number of non-NaN cells from the original input matrix. This functionality is particularly valuable when dealing with datasets containing missing or incomplete information.

**Key Features:**
- **Efficient Mask Computation:** OptiMask streamlines the process of deriving masks that are optimized for NaN data elimination.
- **NaN Data Removal:** The package enables users to effortlessly generate processed submatrices by excluding NaN values, ensuring data integrity and reliability.
- **Maximized Data Retention:** OptiMask's algorithm focuses on preserving the highest count of non-NaN cells within the processed matrix.
- **Compatibility with Numpy Arrays and Pandas DataFrames:** OptiMask seamlessly integrates with both Numpy arrays and Pandas DataFrames, two of the most widely used data structures in Python. This ensures that you can apply OptiMask's functionality to your preferred data format without any hassle.
- **User-Friendly Interface:** With its Python-based interface, OptiMask is designed to be intuitive and user-friendly, catering to both beginners and experienced programmers.

Experience the convenience of NaN data removal with unparalleled efficiency and accuracy using OptiMask. Whether you're working with Numpy arrays or Pandas DataFrames, OptiMask provides a versatile solution to enhance your data preprocessing and analysis workflows.

## Installation

You can install `optimask` using pip:

```
pip install optimask
```

## Usage

Import the `OptiMask` class from the `optimask` package and use its methods to optimize data masking:

```
from optimask import OptiMask
import numpy as np

m = 120
n = 7
data = np.zeros(shape=(m, n))
data[24:72, 3] = np.nan
data[95, :5] = np.nan

rows, cols = OptiMask.solve(data)
len(rows)*len(cols)/data.size, np.isnan(data[rows][:, cols]).any()
```

## Contributing

Contributions to `optimask` are welcome! If you find a bug, have a feature request, or want to contribute code, please feel free to open an issue or submit a pull request.
