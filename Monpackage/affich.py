
import webbrowser
from threading import Timer
from flask import Flask
from Monpackage import module_globalV

class loadweb():

    app = Flask(__name__)

    @app.route('/')

    def home():
        return module_globalV.ma_variable

    def open_browser():
        #pass
        webbrowser.open('http://127.0.0.1:5000/')

    def app_run(app,open_browser):
        Timer(1, open_browser).start()
        
        app.run(debug=True, use_reloader = False)