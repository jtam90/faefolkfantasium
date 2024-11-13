from flask import render_template, redirect, url_for, request, flash
from faefolkfantasium import app, db
from faefolkfantasium.models import Being  # Assuming 'Being' is your model
from werkzeug.utils import secure_filename
import os

# Utility function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to display the image
@app.route('/uploads/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

# Home Route
@app.route("/")
def home():
    beings = Being.query.all()  # Query all beings from the database
    return render_template("index.html", beings=beings)


# Route for Creating a New Being
@app.route("/create", methods=["GET", "POST"])
def create_being():
    image_path = None  # Initialize as None

    if request.method == "POST":
        # Get the form data
        name = request.form.get("name")
        description = request.form.get("description")

        # Initialize new being without image path
        new_being = Being(name=name, description=description)

        # Handle file upload for a new image
    if 'image' in request.files:
        file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        try:
            file.save(upload_path)
            new_being.image_path = filename  # Save the image filename in the database
            print(f"Image Path Saved: {new_being.image_path}")  # Debugging line
        except FileNotFoundError:
            flash("The upload folder does not exist or is inaccessible. Please check configuration.")
            return redirect(url_for("create_being"))
    else:
        flash("Invalid file type. Please upload a PNG, JPG, JPEG, or GIF image.")


        # Add the new being to the database
        db.session.add(new_being)
        db.session.commit()  # Make sure the new being is committed to the database

        flash(f"Successfully created a new being: {name}")
        return redirect(url_for("home"))

    return render_template("create_being.html", image_path=image_path)  # Pass image_path to template



# Route for Editing an Existing Being
@app.route("/edit/<int:being_id>", methods=["GET", "POST"])
def edit_being(being_id):
    being = Being.query.get_or_404(being_id)  # Fetch the being or return 404 if not found

    if request.method == "POST":
        being.name = request.form.get("name")
        being.description = request.form.get("description")

        # Handle file upload for updating image
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                # Save the file and update image path in the model
                try:
                    file.save(upload_path)
                    being.image_path = filename  # Update the being's image path with new filename
                except FileNotFoundError:
                    flash("The upload folder does not exist or is inaccessible. Please check configuration.")
                    return redirect(url_for("edit_being", being_id=being_id))
            else:
                flash("Invalid file type. Please upload a PNG, JPG, JPEG, or GIF image.")

        # Save changes to the database
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit_being.html", being=being)  # Pass the existing being data to the template

# Route for Deleting a Being
@app.route("/delete/<int:being_id>", methods=["POST"])
def delete_being(being_id):
    being = Being.query.get_or_404(being_id)
    if request.method == "POST":
        db.session.delete(being)
        db.session.commit()
        flash(f"Successfully deleted the being: {being.name}")
        return redirect(url_for("home"))

# Route for handling uploads specifically, if needed
@app.route('/upload_image', methods=['POST'])
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
        return redirect(url_for("home"))
    else:
        flash("Allowed file types are png, jpg, jpeg, gif.")
        return redirect(url_for("create_being"))

