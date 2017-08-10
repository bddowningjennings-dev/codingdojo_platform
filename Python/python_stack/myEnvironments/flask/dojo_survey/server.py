
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")

def root():
    return render_template("index.html")

@app.route("/result", methods=['POST'])

def results():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    print "printing name"
    print name
    return render_template("result.html", name=name, location=location, language=language, comment=comment)

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

app.run(debug=True)
