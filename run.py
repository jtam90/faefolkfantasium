import os
from faefolkfantasium import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT not set
    app.run(host="0.0.0.0", port=port, debug=False)  # Use host="0.0.0.0" for Heroku




