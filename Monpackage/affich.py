
import webbrowser
from threading import Timer
from flask import Flask
from Monpackage.request import requete
#from Monpackage import fit_url
#from Monpackage.log import log


class loadweb(requete):
    app = Flask(__name__)

    @app.route('/')
 
    def home():
        url = "https://vnsylob1:8443/rest/login"
        affichage =requete.request_method(url)
        return affichage


    def open_browser():
        webbrowser.open_new('http://127.0.0.1:5000/')

    def run_server(open_browser,app):
        Timer(1, open_browser).start()
        app.run(debug=True)


#from urllib import response
#requete,Timer,webbrowser,Flask