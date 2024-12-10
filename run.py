import webbrowser
from faefolkfantasium.app import create_app

# Create the app instance
app = create_app()

if __name__ == "__main__":
    # Open the browser automatically
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, use_reloader=False)



