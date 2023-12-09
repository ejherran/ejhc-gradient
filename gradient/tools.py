import numpy as np
from typing import Optional
from gradient.core import FunctionGradient

def gradient_function(
        *,
        variables: str,
        function: str,
) -> Optional[FunctionGradient]:
    """Summary: Create a FunctionGradient object from string expressions.

    Args:
        variables (str): A string containing the variables of the function.
        function (str): A string containing the function.
    """

    try:
        return FunctionGradient(
            variables=variables,
            function=function,
        )

    except Exception:
        return None


def gradient_descent(
    *,
    grandient: FunctionGradient,
    initial_value: np.ndarray,
    learning_ratio: np.float64,
    tolerance: np.float64,
    max_iterations: np.int64,
) -> np.ndarray:
    """Summary: Perform gradient descent.
    
    Args:
        grandient (FunctionGradient): The gradient of the function.
        initial_value (np.ndarray): The initial value of the vector.
        learning_ratio (np.float64): The learning ratio.
        tolerance (np.float64): The tolerance.
        max_iterations (np.int64): The maximum number of iterations.
    """

    x_current = initial_value

    for _ in range(max_iterations):

        grandient_vector = grandient.evaluate_gradient(
            vector=x_current
        )

        x_next = x_current - learning_ratio * grandient_vector

        if np.linalg.norm(grandient_vector) < tolerance:
            break

        x_current = x_next

    return x_next
