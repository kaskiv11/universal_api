from flask import Flask, jsonify, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from data.database_data import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = USERNAME
app.config['MAIL_PASSWORD'] = PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = "kaskiv11@gmail.com"
mail = Mail(app)

app.config['SECRET_KEY'] = 'my_secretkey'
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=False)


with app.app_context():
    db.create_all()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            return render_template("register.html", message="Email already registered")

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        token = s.dumps(email, salt="email-confirm")
        link = url_for('confirm_email', token=token, _external=True)

        msg = Message(subject='Confirm your email', recipients=[email])
        msg.body = f"Please click on the link to confirm your registration: {link}"

        try:
            mail.send(msg)
            return render_template("confirm.html", message="Check your email to confirm registration")
        except Exception as e:
            return render_template("confirm.html", message=f"Error sending confirmation email: {str(e)}")

    return render_template("register.html")


@app.route('/confirm/<token>', methods=['GET'])
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        return render_template('confirm.html', message="The confirmation link has expired")
    except BadSignature:
        return render_template('confirm.html', message="Token is invalid")

    user = User.query.filter_by(email=email).first_or_404()
    if user.is_active:
        return render_template('success.html', message="Account already confirmed")

    user.is_active = True
    db.session.commit()
    return render_template('success.html', message="Account confirmed successfully")


if __name__ == '__main__':
    app.run(debug=True)

