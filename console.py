import numpy as np
from gradient.tools import gradient_function, gradient_descent

def main():
    """Summary: Main function."""

    print('--------------------------------')
    print('EJHC Gradient Descent - VIU 2023')
    print('--------------------------------')

    while True:
        print('\n\n')

        input_variables = input('Enter the variables of the function separated by spaces: ')
        input_function = input('Enter the function: ')

        g_function = gradient_function(
            variables=input_variables,
            function=input_function,
        )

        if g_function is None:
            print('Invalid function, try again.')
            continue

        try:
            input_initial_value = input('Enter the initial vector separated by spaces: ')
            initial_value = np.array(
                input_initial_value.split(' ')).astype(np.float64
            )

            input_learning_ratio = input('Enter the learning ratio: ')
            learning_ratio = np.float64(float(input_learning_ratio))

            input_tolerance = input('Enter the tolerance: ')
            tolerance = np.float64(float(input_tolerance))

            input_max_iterations = input('Enter the maximum number of iterations: ')
            max_iterations = np.int64(float(input_max_iterations))

        except ValueError:
            print('Ivalid parameters, try again.')
            continue

        try:
            result = gradient_descent(
                grandient=g_function,
                initial_value=initial_value,
                learning_ratio=learning_ratio,
                tolerance=tolerance,
                max_iterations=max_iterations,
            )

            print('Resultant vector: ', result)
            print(
                'Value of the function: ',
                g_function.evaluate_function(vector=result)
            )

        except Exception:
            print('Error, try again.')
            continue


if __name__ == '__main__':
    main()
