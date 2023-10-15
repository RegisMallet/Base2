"""Envoie requête URL"""


import requests
from requests.auth import HTTPBasicAuth
from Monpackage.log import log
#from Monpackage.fit_url import fit_url

class requete(log):
    
    def request_method():
        global url 
        retour = requests.get(url, auth=HTTPBasicAuth(log.requestelement))
        
        return retour.status_code
    #(login, encodpassword))
        # url = "votre_url"
        # login = "votre_login"
        # encodepassword = "votre_encodepassword"