import re  
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."
   if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."
        return True, "Your password is strong."

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = ""
    is_strong = None  

    if request.method == 'POST':
        password = request.form['password']
        is_strong, feedback = check_password_strength(password)

    return render_template('index.html', feedback=feedback, is_strong=is_strong)

if __name__ == "__main__":
    app.run(debug=True)

