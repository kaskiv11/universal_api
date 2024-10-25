from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure the Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_DEFAULT_SENDER'] = 'DEFAULT'

mail = Mail(app)

@app.route('/test_email')
def test_email():
    msg = Message(subject='Test Email', recipients=['Email'])
    msg.body = 'This is a test email.'
    try:
        mail.send(msg)
        return 'Email sent successfully!'
    except Exception as e:
        return f'Error sending email: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
