from flask import Flask, request, jsonify
import json
import os
import pandas as pd
import numpy as np

app = Flask(__name__)

# functions which I made available to script execution
AVAILABLE_FUNCTIONS = {
    '__builtins__': {
        'print': print,
        'range': range,
        'len': len,
        'int': int,
        'float': float,
        'str': str,
        'bool': bool,
        'dict': dict,
        'list': list,
        'set': set,
        'tuple': tuple,
        'min': min,
        'max': max,
        'abs': abs,
        'sum': sum,
        'pow': pow,
        'enumerate': enumerate,
        'zip': zip,
        'sorted': sorted,
        'Exception': Exception,
        'ValueError': ValueError,
        'isinstance': isinstance,
        'type': type
    },
    'os': os,
    'pd': pd,
    'np': np,
    'json': json
}

@app.route('/execute', methods=['POST'])
def execute_script():
    data = request.get_json()
    script_content = data.get("script")

    if not script_content:
        return jsonify({"error": "No script provided"}), 400

    # temp dict
    exec_namespace = {}
    exec_namespace.update(AVAILABLE_FUNCTIONS)

    # wrapper to exectue thr script and return the o/p
    wrapped_script = """
def main_wrapper():
    try:
        result = main()
        if not isinstance(result, dict):
            raise ValueError("main() must return a dictionary")
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})

result = main_wrapper()
"""

    full_script = f"{script_content}\n{wrapped_script}"
    try:
        exec(full_script, exec_namespace, exec_namespace)
        output = exec_namespace.get('result', '{"error": "No O/P"}')
        output_dict = json.loads(output)
    except Exception as e:
        output_dict = {"error": f"Script error: {str(e)}"}

    return jsonify({"result": output_dict})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
