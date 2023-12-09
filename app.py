import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify
from gradient import tools as gt


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gradient', methods=['POST'])
def gradient():
    if request.is_json:
        return _generate_gradient_response(request.get_json())
    else:
        return jsonify({'message': 'Invalid request'})


#############################################
# Helper functions                          #
#############################################

def _generate_gradient_response(json_data):

    r_vars = json_data['variables']
    r_func = json_data['function']
    r_vec = json_data['initialVector']
    r_rate = json_data['learningRate']
    r_tol = json_data['tolerance']
    r_iters = json_data['maxIterations']

    g_function = gt.gradient_function(
        variables=r_vars,
        function=r_func,
    )

    if g_function is None:
        return jsonify({'message': 'Invalid function', 'code': 1})

    try:
        initial_value = np.array(
            r_vec.split(' ')).astype(np.float64
        )

        learning_ratio = np.float64(float(r_rate))
        tolerance = np.float64(float(r_tol))
        max_iterations = np.int64(float(r_iters))

    except ValueError as e:
        print(e)
        return jsonify({'message': 'Invalid parameters', 'code': 2})

    try:
        result = gt.gradient_descent(
            grandient=g_function,
            initial_value=initial_value,
            learning_ratio=learning_ratio,
            tolerance=tolerance,
            max_iterations=max_iterations,
        )

        f_value = g_function.evaluate_function(vector=result)

    except Exception:
        return jsonify({'message': 'Execution error', 'code': 3})

    return jsonify({
        'message': 'Success',
        'code': 0,
        'result': result.tolist(),
        'value': f_value,
    })


    return jsonify({'message': 'Success'})
