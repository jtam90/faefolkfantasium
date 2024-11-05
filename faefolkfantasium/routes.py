from flask import render_template, redirect, url_for, request
from faefolkfantasium import app, db
from faefolkfantasium.models import Being  # Assuming 'Being' is your model
from werkzeug.utils import secure_filename
import os

app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Ensure this folder exists

# Home Route
@app.route("/")
def home():
    beings = Being.query.all()  # Query all beings from the database
    return render_template("index.html", beings=beings)

# Route for Creating a New Being
@app.route("/create", methods=["GET", "POST"])
def create_being():
    if request.method == "POST":
        # Get the form data
        name = request.form.get("name")
        description = request.form.get("description")

        # Handle file upload for a new image
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                new_being = Being(name=name, description=description, image_path=filename)
            else:
                new_being = Being(name=name, description=description)  # No image provided
        else:
            new_being = Being(name=name, description=description)  # No image provided

        # Add to database
        db.session.add(new_being)
        db.session.commit()

        return redirect(url_for("home"))  # Redirect to home page after creating the being

    return render_template("create_being.html")

# Route for Editing an Existing Being
@app.route("/edit/<int:being_id>", methods=["GET", "POST"])
def edit_being(being_id):
    being = Being.query.get_or_404(being_id)  # Fetch the being or return 404 if not found
    if request.method == "POST":
        being.name = request.form.get("name")
        being.description = request.form.get("description")

        # Handle file upload for a new image
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                being.image_path = filename  # Update the being's image path if a new file was uploaded

        # Save changes to the database
        db.session.commit()
        return redirect(url_for("home"))  # Redirect to home page after editing

    return render_template("edit_being.html", being=being)  # Pass the existing being data to the template

# Route for Deleting a Being
@app.route("/delete/<int:being_id>", methods=["POST"])
def delete_being(being_id):
    being = Being.query.get_or_404(being_id)
    if request.method == "POST":
        db.session.delete(being)
        db.session.commit()
        return redirect(url_for("home"))  # Redirect to home page after deletion

