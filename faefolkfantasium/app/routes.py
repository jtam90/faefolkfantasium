from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db  # Import db from the current package
from .models import Being  
import os

# Define the blueprint
bp = Blueprint('main', __name__)

# Utility function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to display the image
@bp.route('/uploads/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

# Home Route
@bp.route("/")
def home():
    beings = Being.query.all()  # Query all beings from the database
    return render_template("index.html", beings=beings)

# Route for Creating a New Being
@bp.route("/create", methods=["GET", "POST"])
def create_being():
    if request.method == "POST":
        # Get the form data
        name = request.form.get("name")
        description = request.form.get("description")

        # Initialize new being without image path
        new_being = Being(name=name, description=description)

        # Add the new being to the database
        db.session.add(new_being)
        db.session.commit()  # Commit the new being to the database

        flash(f"Successfully created a new being: {name}")
        return redirect(url_for("main.home"))

    return render_template("create_being.html")  # No need to pass image_path anymore

# Route for Editing an Existing Being
@bp.route("/edit/<int:being_id>", methods=["GET", "POST"])
def edit_being(being_id):
    being = Being.query.get_or_404(being_id)  # Fetch the being or return 404 if not found

    if request.method == "POST":
        being.name = request.form.get("name")
        being.description = request.form.get("description")

        # Save changes to the database
        db.session.commit()
        flash(f"Successfully updated the being: {being.name}")
        return redirect(url_for("main.home"))

    return render_template("edit_being.html", being=being)  # No need to handle image_path anymore

# Route for Deleting a Being
@bp.route("/delete/<int:being_id>", methods=["POST"])
def delete_being(being_id):
    being = Being.query.get_or_404(being_id)
    if request.method == "POST":
        db.session.delete(being)
        db.session.commit()
        flash(f"Successfully deleted the being: {being.name}")
        return redirect(url_for("main.home"))

# Route for handling uploads specifically, if needed
@bp.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        flash("No file part in the request.")
        return redirect(url_for('create_being'))
    
    file = request.files['image']
    if file.filename == '':
        flash("No selected file.")
        return redirect(url_for('create_being'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash("File successfully uploaded.")
        return redirect(url_for("main.home"))
    else:
        flash("Allowed file types are png, jpg, jpeg, gif.")
        return redirect(url_for("create_being"))

