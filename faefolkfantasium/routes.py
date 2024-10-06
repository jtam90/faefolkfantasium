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

    @app.route("/edit/<int:being_id>", methods=["GET", "POST"])
def edit_being(being_id):
    being = Being.query.get_or_404(being_id)  # Get the being by ID

    if request.method == "POST":
        # Update the being's details
        being.name = request.form.get("name")
        being.description = request.form.get("description")

        db.session.commit()  # Save changes to the database
        flash('Being updated successfully!', 'success')  # Flash message
        return redirect(url_for("home"))  # Redirect to home page

    return render_template("edit_being.html", being=being)  # Render the edit form

# Route for Deleting a Being
@app.route("/delete/<int:being_id>", methods=["POST"])
def delete_being(being_id):
    being = Being.query.get_or_404(being_id)  # Get the being by ID
    db.session.delete(being)  # Delete the being
    db.session.commit()  # Commit the changes
    flash('Being deleted successfully!', 'success')  # Flash message
    return redirect(url_for("home"))  # Redirect to home page

