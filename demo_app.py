from flask import Flask

app = Flask(_name_)

# Main url code
@app.route('/')
def index():
    return "Hello World"

# Run the app
if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)