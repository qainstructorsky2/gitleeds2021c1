from flask import Flask

app = Flask(__name__)


@app.route('/newyork')

def newyork_page():
    return """
      <h1>Hello New York!</h1>

      <img src="https://photos.mandarinoriental.com/is/image/MandarinOriental/new-york-2017-columbus-circle-01?wid=2880&hei=1280&fmt=jpeg&crop=6,1064,4928,2190&anchor=2032,2134&qlt=75,0&op_sharpen=0&resMode=sharp2&op_usm=0,0,0,0&iccEmbed=0&printRes=72&fit=crop">
      
      """

@app.route('/barra')
def barra_page():
    return """
      <h1>Hello Barra</h1>

      <img src="https://www.visitouterhebrides.co.uk/imageresizer/?image=%2Fdmsimgs%2F2015-07-15_13.46.25_-_Copy_-_Copy_515365848.jpg&action=ProductDetailImageFullWidthSite">

      """


if __name__ == '__main__':
    app.run()
