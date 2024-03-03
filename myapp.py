from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
db_path = "database.db" 

if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            name TEXT,
            id INTEGER PRIMARY KEY,
            points INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form.get('search')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + search_term + '%',))
        users = cursor.fetchall()
        conn.close()
        return render_template('crud.html', users=users, search_term=search_term)
    else:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return render_template('crud.html', users=users, search_term='')

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        points = request.form['points']
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, id, points) VALUES (?, ?, ?)", (name, id, points))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:user_id>')
def delete(user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:user_id>', methods=['POST'])
def update(user_id):
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        points = request.form['points']
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name=?, id=?, points=? WHERE id=?", (name, id, points, user_id))
        conn.commit()
        conn.close()
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
