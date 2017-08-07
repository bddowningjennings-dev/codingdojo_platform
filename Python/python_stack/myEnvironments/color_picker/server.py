from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home(red = 50, green = 205, blue = 255):
  return render_template('index.html', red = red, green = green, blue = blue)

@app.route('/process', methods=['POST'])

def process():
  return home(request.form['red'], request.form['green'], request.form['blue'])

app.run(debug=True)