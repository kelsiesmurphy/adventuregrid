from flask import Flask, render_template
from controllers.experience_controller import experiences_blueprint
from controllers.users_experiences_controller import users_experiences_blueprint
from controllers.user_controller import users_blueprint

app = Flask(__name__)
app.register_blueprint(users_experiences_blueprint)
app.register_blueprint(experiences_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)