from flask_app import app
from flask_app.controllers import controller


if __name__ == '__main__':
    app.run(debug=True)

app.secret_key = "shhhhhh"