from flask import render_template, redirect, url_for, request
from faefolkfantasium import app, db
from faefolkfantasium.models import Being  # Assuming 'Being' is your model

# Home Route
@app.route("/")
def home():
    beings = Being.query.all()  # Query all beings from the database
    return render_template("home.html", beings=beings)

# Route for Creating a New Being
@app.route("/create", methods=["GET", "POST"])
def create_being():
    if request.method == "POST":
        # Get the form data
        name = request.form.get("name")
        description = request.form.get("description")

        # Create a new Being object
        new_being = Being(name=name, description=description)

        # Add to database
        db.session.add(new_being)
        db.session.commit()

        return redirect(url_for("home"))  # Redirect to home page after creating the being

    return render_template("create_being.html")

