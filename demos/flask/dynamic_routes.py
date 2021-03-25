from flask import Flask

app = Flask(__name__)


@app.route('/dynamic/<word>')
def home(word):
    return word


@app.route('/square/<int:number>')
def square(number):
    squared =number ** 2
    line ="your number squared is " + str(squared)
    return line


if __name__ == '__main__':
    app.run(debug=True)