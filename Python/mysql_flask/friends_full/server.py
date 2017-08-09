from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def home():
  query = 'select name, age, date_format(created_at, "%b %D") as create_date, date_format(created_at, "%Y") as year from friends_full;'                # define your query
  results = mysql.query_db(query)                           # run query with query_db()  
  return render_template('index.html', results = results)

@app.route('/process', methods=['POST'])
def add():
  query = "INSERT INTO friends_full (name, age, created_at, updated_at) values (:name, :age, NOW(), NOW())"
  data = {
    'name': request.form['name'],
    'age': request.form['age']
  }
  mysql.query_db(query, data)
  return redirect('/')

app.run(debug=True)