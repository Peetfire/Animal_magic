# import render template for use in main root
from flask import Flask, render_template

# import blueprints from cntrollers
# from controllers.<name>_controller import <name>_blueprint


app = Flask(__name__)

# Register all blueprints here
# app.register_blueprint(<name>_blueprint)


# Sets base root to index.html
@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
