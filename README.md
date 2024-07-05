# Polynomials

## Overview
This project, is a reusable library for facilitating polynomial operations using Python. It includes various scripts to define, manipulate, and present polynomials, designed to work with algebraic expressions. The demonstration part is included to showcase how to use the library and demonstrate its capabilities.

## File Contents
- **Polynomials.py**: Contains the core polynomial operations and definitions.
- **Presentation.py**: Demonstrates polynomial operations and results.
- **main.py**: Conventional entry point that currently just executes "Presentation.py".

## Requirements
- Python 3.x
- `numpy` (for calculations)
- `matplotlib` (for plotting graphs)

## Setup
1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip:
   ```sh
   pip install numpy
   pip install matplotlib
   ```

## Instructions
1. **Run**: Execute the `Presentation.py` script to see polynomial operations in action:
   ```sh
   python Presentation.py
   ```

## Features
- **Polynomial Calculations**:
  - Finding zero places (implemented for polynomials of degree 2 to 0)
  - Plotting graphs (implemented for polynomials of degree 2 to 0)
  - Finding derivatives
  - Perform operations like addition, subtraction, and multiplication (division is not implemented yet)
- **Polynomial Manipulations**:
  - Moving their terms left or right
  - Changing or adding terms
  - Concatenating with other polynomial or list objects
  - Possesses most properties of a list object, but is indexed from n to 0, where n equals its degree.

## Creation details
### Author
Tomasz Nehring
### Created in ~ 2019 AD

## Repository
[GitHub Repository](https://github.com/Siiir/python3-polynomials)
