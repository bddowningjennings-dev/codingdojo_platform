from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=["GET"])

def home():
  return render_template('index.html')

# @app.route('/<color>')

# def ninja_color(color):
#   turtle = ''
#   color = color.lower()
#   if color == 'blue':
#     turtle = 'leonardo'
#   elif color == 'orange':
#     turtle = 'michelangelo'
#   elif color == 'purple':
#     turtle = 'donatello'
#   elif color == 'red':
#     turtle = 'raphael'
#   else:
#     turtle = 'notapril'
#   turtle += '.jpg'
#   return render_template('index.html', img = turtle)

@app.route('/', methods=["POST"])

def result():
  print 'hihixx'
  # return render_template('ninja.html', img = 'tmnt.png')
  return redirect('/')

app.run(debug=True)