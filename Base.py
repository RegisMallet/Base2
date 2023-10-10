# C'est parti

# Rajout de ce commentaire

from flask import Flask
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def home():
    return "Bonjour, bienvenue sur mon application web !"

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')
      


if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)
    


