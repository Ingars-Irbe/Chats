from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def getIndex():
  return render_template('index.html')





if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5050, debug=True) 