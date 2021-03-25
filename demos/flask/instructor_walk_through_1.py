from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name):
   greating = "hello " + name
   return """
   <html>
   <head>
    <title> Flask Routes Demo </title>
   </head>
   
   
   <body>
    <h1> Name page </h1>
    <p> Hello {}!</p>
   </body>
   
   </html>
   """.format(name)




if __name__ == '__main__':
    app.run(debug=True)