from flask import Flask, request, render_template_string

app = Flask(__name__)

# Dictionary of usernames and their passwords
USERS = {
    "admin": "letmein",
    "user1": "qwerty",
    "maciusk": "czesio"
}

html_form = '''
<!DOCTYPE html>
<html>
<body>
    <h2>Login Page</h2>
    <form action="/login" method="POST">
        Username: <input name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET"])
def index():
    return render_template_string(html_form)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in USERS and USERS[username] == password:
        return render_template_string(html_form, message="✅ Login successful!")
    else:
        return render_template_string(html_form, message="❌ Invalid login.")

if __name__ == "__main__":
    app.run(debug=True)