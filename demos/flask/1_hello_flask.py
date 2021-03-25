from flask import Flask

myapp = Flask(__name__)


@myapp.route('/')
def hello_world():
    return 'hello world from flask!'

if __name__ == '__main__':
    myapp.run()