from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/get/text')
def get_text():
    return Response("Hello from flask  using an explicit Response object", mimetype='text/plain')

@app.route('/get/accounts')
def get_account():
    return Response("Hello from flask  using an accounts", mimetype='text/plain')

@app.route('/get/books')
def get_books():
    return Response("Hello from flask  books", mimetype='text/plain')

@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent=request.data.decode('utf-8')
    return Response("You posted this data to the flask app ",+ data_sent,  mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)