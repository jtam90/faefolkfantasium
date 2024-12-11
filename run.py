import os
from faefolkfantasium.app import app

# Get the port number from the environment variable, default to 5000
port = int(os.environ.get("PORT", 5000))

# Run the Flask app with the correct host and port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=False)







