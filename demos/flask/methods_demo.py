from flask import Flask, request

app = Flask(__name__)

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])

def method_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"


if __name__ == '__main__':
    app.run(debug=True)

