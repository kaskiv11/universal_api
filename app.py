from flask import Flask, jsonify, request, url_for, render_template,  flash, redirect, session
from flask_bcrypt import Bcrypt
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"
bcrypt = Bcrypt(app)

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "pass",
    "database": "api_web"
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form.get("email")
        password = request.form.get("password")
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO users (username, email, password) VALUES (%s, %s, %s)
            """, (username, email, hashed_password))

            conn.commit()
            cursor.close()
            flash("Registration successful", "success")
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError as e:
            flash(str(e), "danger")
    return render_template("registration.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            db = mysql.connector.connect(**db_config)
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            cursor.close()
            db.close()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['username'] = user['username']
                flash('Login successful!', 'success')
                return redirect('/')
            else:
                flash('Invalid email or password.', 'danger')
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", 'danger')

    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user and bcrypt.check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['username'] = user['username']
                flash('Login successful!', 'success')
                return redirect('/')
            else:
                flash('Invalid email or password.', 'danger')
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", 'danger')

    return render_template('login.html')


@app.route('/leave_review', methods=['GET', 'POST'])
def leave_review():
    if 'user_id' not in session:
        flash("Sign in to leave a review.", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':
        content = request.form['content']
        user_id = session['user_id']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reviews (user_id, content) 
            VALUES (%s, %s)
        """, (user_id, content))
        conn.commit()
        cursor.close()
        conn.close()

        flash("Your review has been successfully saved!", "success")
        return redirect(url_for('leave_review'))

    return render_template('leave_review.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)