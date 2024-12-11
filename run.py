import webbrowser
from faefolkfantasium.app import create_app

# Create the app instance
app = create_app()

if __name__ == "__main__":
    # Open the browser automatically to the correct Gitpod port
    webbrowser.open("http://localhost:8081")
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)



