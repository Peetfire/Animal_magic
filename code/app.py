# import render template for use in main root
from flask import Flask, render_template

# import blueprints from cntrollers
from controllers.appointments_controller import appointments_blueprint


app = Flask(__name__)

# Register all blueprints here
app.register_blueprint(appointments_blueprint)


# Sets base root to index.html
@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
