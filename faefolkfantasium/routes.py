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

# Route for Editing an Existing Being
@app.route("/edit/<int:being_id>", methods=["GET", "POST"])
def edit_being(being_id):
    being = Being.query.get(being_id)
    if request.method == "POST":
        being.name = request.form.get("name")
        being.description = request.form.get("description")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("create_being.html", being=being)

# Route for Deleting a Being
@app.route("/delete/<int:being_id>", methods=["POST"])
def delete_being(being_id):
    being = Being.query.get_or_404(being_id)
    db.session.delete(being)
    db.session.commit()
    return redirect(url_for("home"))

