from flask import render_template, redirect, url_for, request
from faefolkfantasium import app, db
from faefolkfantasium.models import Being  # Assuming 'Being' is your model

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
    if request.method == "POST":
        db.session.delete(being)
        db.session.commit()
        return redirect(url_for("home"))

from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Print statements for debugging
    print("Form submitted")

    # Check if any file part is present in request
    if 'image' not in request.files:
        print("No file part in request")
        return redirect(request.url)

    # Get the file from the request
    file = request.files['image']
    if file.filename == '':
        print("No file selected")
        return redirect(request.url)

    # Process file if available
    if file:
        # Use secure filename and save to upload folder
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(f"File {filename} saved successfully")

        # Retrieve other form fields
        name = request.form.get('name')
        description = request.form.get('description')
        print(f"Name: {name}, Description: {description}")

        # After saving the file and getting the form data, you could store it in a database
        # return a success message
        return "Image uploaded successfully with name and description"
