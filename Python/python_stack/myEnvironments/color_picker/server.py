from flask import Flask, render_template, request, redirect

app = Flask(__name__)

colors = {'red': 50, 'green': 205, 'blue': 255}

@app.route('/')

def home():
  return render_template('index.html', red = colors['red'], green = colors['green'], blue = colors['blue'])

@app.route('/process', methods=['POST'])

def process():
  global colors
  for key, val in request.form.items():
    colors[key] = val
  return redirect('/')

app.run(debug=True)