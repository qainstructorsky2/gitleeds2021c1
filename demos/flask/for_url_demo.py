from flask import Flask, Response,url_for

app = Flask(__name__)


@app.route('/get/text')
def get_text():
    return Response("Hello from flask using an explicit Response object", mimetype='text/plain')


@app.route("/index/<name>/<int:age>")
def index(name,age):
    url =url_for("get_text")
    return """
   <html>
   <head>
    <title> Flask url Demo </title>
   </head>


   <body>
    <h1> Name page </h1>
    <p> Hello {}!</p>
    <p> You are {} years(s) old</p>
    <hr>
    <a href="{}">Welcome</a>
   </body>

   </html>
   """.format(name,age,url)


if __name__ == '__main__':
    app.run(debug=True)