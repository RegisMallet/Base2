
import webbrowser
from threading import Timer
from flask import Flask


class loadweb(requete):
    app = Flask(__name__)

    @app.route('/')
 
    def home():
        global url
        affichage =requete.request_method(url)
        return affichage


    def open_browser():
        webbrowser.open_new('http://127.0.0.1:5000/')

        Timer(1, open_browser).start()
        app.run(debug=True)


#from urllib import response
#requete,Timer,webbrowser,Flask