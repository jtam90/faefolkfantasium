document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('create-being-form'); // Get the form by its ID
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the default form submission (no page reload)

            const formData = new FormData(form); // Gather the form data
            console.log('Submitting form with data:', formData);

            // Use fetch to send the form data to the server
            fetch(form.action, {
                    method: 'POST',
                    body: formData, // Send the form data as the request body
                })
                .then(response => {
                    console.log('Response:', response);
                    if (response.ok) {
                        // Redirect to the homepage after a successful form submission
                        window.location.href = '/'; // Replace with the correct URL if necessary
                    } else {
                        alert('Failed to submit the form. Please try again.');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Something went wrong. Please try again.');
                });
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.getElementById("image");
    const fileNameDisplay = document.getElementById("file-name");

    // Only run if #image element exists on the page
    if (imageInput && fileNameDisplay) {
        imageInput.addEventListener("change", function () {
            const fileName = this.files.length > 0 ? this.files[0].name : "No file chosen";
            fileNameDisplay.textContent = fileName;
        });
    } else {
        console.log("Image input not found on this page, skipping file input script.");
    }
});
