# import render template for use in main root
from flask import Flask, render_template

# import blueprints from cntrollers
from controllers.appointments_controller import appointments_blueprint
from controllers.animals_controller import animals_blueprint
from controllers.vets_controller import vets_blueprint
from controllers.owners_controller import owners_blueprint

app = Flask(__name__)

# Register all blueprints here
app.register_blueprint(appointments_blueprint)
app.register_blueprint(animals_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(owners_blueprint)

# Sets base root to index.html
@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
