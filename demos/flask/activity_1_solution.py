from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name):
   greating = "hello " + name
   return greating




if __name__ == '__main__':
    app.run(debug=True)