from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

# Configure Flask-Mail (replace with your Gmail credentials)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kbdCaps@gmail.com'         # <-- your Gmail address
app.config['MAIL_PASSWORD'] = 'njjt ppfm jcpp wdty'            # <-- your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'kbdCaps@gmail.com'   # <-- your Gmail address

mail = Mail(app)
subscribers = set()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')
    if not email or '@' not in email:
        return jsonify({'success': False, 'message': 'Invalid email'}), 400
    if email in subscribers:
        return jsonify({'success': False, 'message': 'Already subscribed'}), 409
    subscribers.add(email)
    # Send confirmation email
    try:
        msg = Message(
            subject="Welcome to EuCaps!",
            recipients=[email],
            body="Thank you for subscribing to EuCaps! We'll keep you updated."
        )
        mail.send(msg)
        print(f"Sent confirmation email to {email}")  # Add this line
    except Exception as e:
        return jsonify({'success': False, 'message': f'Could not send email: {str(e)}'}), 500
    return jsonify({'success': True, 'message': 'Subscribed successfully!'})

if __name__ == '__main__':
    app.run(debug=False)