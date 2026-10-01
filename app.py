from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
#function for calculating operations

def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

    else:
        raise ValueError("Invalid operation")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def perform_calculation():
    data = request.get_json()

    try:
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        operation = data["operation"]

        result = calculate(num1, num2, operation)

        return jsonify({
            "success": True,
            "result": result
        })

    except ValueError as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 400

    except (KeyError, TypeError):
        return jsonify({
            "success": False,
            "error": "Invalid input"
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
