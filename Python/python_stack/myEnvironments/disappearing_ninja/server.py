from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def home():
  return render_template('index.html')

@app.route('/ninja/<color>')

def ninja_color(color):
  turtle = ''
  color = color.lower()
  if color == 'blue':
    turtle = 'leonardo'
  elif color == 'orange':
    turtle = 'michelangelo'
  elif color == 'purple':
    turtle = 'donatello'
  elif color == 'red':
    turtle = 'raphael'
  else:
    turtle = 'notapril'
  turtle += '.jpg'
  return render_template('ninja.html', img = turtle)

@app.route('/ninja')

def ninja():
  return render_template('ninja.html', img = 'tmnt.png')

app.run(debug=True)