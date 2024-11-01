from flask import Flask
from flask_mail import Mail, Message
from data.database_data import *

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = 'email@gmail.com'

mail = Mail(app)

@app.route('/test_email')
def test_email():
    msg = Message(subject='Test Email', recipients=['email2@lpnu.ua'])  # Введіть адресата
    msg.body = 'This is a test email.'
    try:
        mail.send(msg)
        return 'Email sent successfully!'
    except Exception as e:
        return f'Error sending email: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
