import sympy as sp
import numpy as np

class FunctionGradient:
    """Summary: A class to represent a function with its gradient.

    Attributes:
        _variables: A list of sympy symbols.
        _function: A sympy expression.
        _gradient: A list of sympy expressions that represent the gradient.
        _lambda_function: A lambda function that evaluates the function.
        _lambda_gradient: A lambda function that evaluates the gradient.
    """

    def __init__(
        self,
        *,
        variables: str,
        function
    ) -> None:
        self._variables = sp.symbols(variables)                                                     # Transform the string into a list of sympy symbols.
        self._function = sp.sympify(function)                                                       # Transform the string into a sympy expression.
        self._gradient = sp.derive_by_array(
            self.function, self.variables
        )                                                                                           # Compute the partial derivatives of the function.

        self._lambda_function = sp.lambdify(
            self.variables, self.function
        )                                                                                           # Create a lambda function that evaluates the function.

        self._lambda_gradient = sp.lambdify(
            self.variables, self.gradient
        )                                                                                           # Create a lambda function that evaluates the gradient.


    @property
    def variables(self) -> sp.Symbol:
        return self._variables

    @property
    def function(self)-> sp.Expr:
        return self._function

    @property
    def gradient(self) -> sp.Array:
        return self._gradient

    def evaluate_function(self, *, vector: np.ndarray) -> np.float64:
        return self._lambda_function(*vector)

    def evaluate_gradient(self, *, vector: np.ndarray) -> np.ndarray:
        return self._lambda_gradient(*vector)
