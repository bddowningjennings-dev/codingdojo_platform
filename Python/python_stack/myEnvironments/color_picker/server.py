from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
  return render_template('index.html', red = 50, green = 205, blue = 255)

@app.route('/', methods=['POST'])

def process():
  colors = {}
  for key, val in request.form.items():
    colors[key] = val
  return render_template('index.html', red = colors['red'], green = colors['green'], blue = colors['blue'])

app.run(debug=True)