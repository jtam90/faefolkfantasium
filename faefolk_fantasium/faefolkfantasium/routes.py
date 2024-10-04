from flask import render_template
from faefolkfantasium import app, db
from faefolkfantasium.models import EtherealBeing

@app.route("/")
def home():
    beings = EtherealBeing.query.all()  # Fetch all beings from the database
    return render_template("home.html", beings=beings)  # Render the home page with beings
