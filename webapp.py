from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('outfitt.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=('GET', 'POST'))
def creation():
    if request.method == 'POST':
        WhiteTee = request.form['WhiteTee']  # Change to a single form field
        BlackTee = request.form['BlackTee']       # Add other fields as needed
        BeigeTee = request.form['BeigeTee']       # Add other fields as needed


        if WhiteTee or BlackTee or BeigeTee:  # Check if t_shirt is not empty
            conn = get_db_connection()
            conn.execute('INSERT INTO outfit (WhiteTee, BlackTee, BeigeTee) VALUES (?, ?, ?)',(WhiteTee, BlackTee, BeigeTee))  # Ensure values match your DB schema
            conn.commit()
            conn.close()
            return redirect(url_for('creation'))

    return render_template("creation.html")

@app.route('/favourites')
def favourites():
    conn = get_db_connection()
    outfit = conn.execute('SELECT * FROM outfit WHERE id = ?',(id))

    if request.method == 'POST':
        WhiteTee = request.form['WhiteTee']
        BlackTee = request.form['BlackTee']
        BeigeTee = request.form['BeigeTee']
          
        conn.execute('UPDATE outfit SET WhiteTee = ?, BlackTee = ?  BeigeTee = ?, WHERE id = ?',
                    (WhiteTee,BlackTee,BeigeTee,id))
        conn.commit()
        conn.close()
        return redirect(url_for('favourites'))

    return render_template('favourites.html', outfit=outfit)

if __name__ == '__main__':
    app.run(debug=True, port=6298)
