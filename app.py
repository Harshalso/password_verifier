import re  # Import the 're' module for regular expressions
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for both uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        if check_password_strength(password):
            feedback = "Your password is strong."
        else:
            feedback = ("Your password is weak. Please make sure it meets the following criteria:<br>"
                        "1. At least 8 characters long<br>"
                        "2. Contains both uppercase and lowercase letters<br>"
                        "3. Contains at least one digit (0-9)<br>"
                        "4. Contains at least one special character (e.g., !, @, #, $, %)")
        return render_template('index.html', feedback=feedback)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
