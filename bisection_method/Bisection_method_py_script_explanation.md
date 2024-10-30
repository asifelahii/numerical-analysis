
# Bisection Method in Python

This document provides an explanation of implementing the bisection method in Python to find the root of a given function. In this example, we use the function:

$$ f(x) = 3x - \cos(x) - 1 $$

## Code Explanation

The following Python code demonstrates how the bisection method works, including all necessary comments to explain each step.

```python
import math  # Import the math module to access trigonometric functions like cos()

# Define the function for which we want to find a root, f(x) = 3x - cos(x) - 1
def f(x):
    return 3 * x - math.cos(x) - 1  # Define the function

# Define the bisection method function
def bisection(func, a, b, tol):
    """
    This function finds a root of the function 'func' within the interval [a, b]
    using the bisection method.

    Parameters:
    func (function): The function to find the root of.
    a (float): Left endpoint of the interval.
    b (float): Right endpoint of the interval.
    tol (float): Tolerance, or the precision required for the solution.

    Returns:
    float: An approximation of the root if found within the interval.
           None if no root exists in the interval.
    """
    # Check if the initial values of a and b bracket a root (f(a) and f(b) must have opposite signs)
    if func(a) * func(b) >= 0:
        print("Error: Root is not bracketed")  # Error if the function does not change signs
        return None  # Exit if no root is bracketed

    # Initialize the midpoint variable 'c'
    c = a
    # Loop until the interval width is within the desired tolerance level
    while abs(b - a) / 2.0 > tol:
        c = (a + b) / 2.0  # Calculate midpoint of the interval

        # Check if we have found the exact root
        if func(c) == 0:
            break  # Root found, exit loop

        # Determine which subinterval to keep based on sign of func(c)
        elif func(a) * func(c) < 0:
            b = c  # Root is in left subinterval, so move 'b' to midpoint
        else:
            a = c  # Root is in right subinterval, so move 'a' to midpoint

    return c  # Return the root approximation

# Main script
a = 0      # Left endpoint of the interval
b = 1      # Right endpoint of the interval
tol = 1e-5 # Set tolerance level for accuracy

# Call the bisection function to find the root of f within [a, b]
root = bisection(f, a, b, tol)

# Display result
if root is not None:
    print(f"Root found: {root}")  # Print the found root if it exists
else:
    print("No root found")  # Indicate no root if function failed
```

## Explanation of Key Parts

- **`f(x)` function**: This is the function for which we are trying to find a root. In this example, it is defined as:
  \[
  f(x) = 3x - \cos(x) - 1
  \]
  
- **`bisection` function**: Implements the bisection method algorithm.
  - Checks if `a` and `b` bracket a root by confirming that `f(a)` and `f(b)` have opposite signs.
  - The midpoint `c` of the interval `[a, b]` is calculated repeatedly until the interval is smaller than the given tolerance `tol`.
  - The method returns the midpoint as the approximate root.

- **Main Code**:
  - Sets up the interval `[a, b]`, and the tolerance level.
  - Calls the `bisection` function and prints the result.

## Sample Output

The script will display the root if found within the specified tolerance or an error if no root is found within the interval.

