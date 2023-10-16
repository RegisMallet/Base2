"""Envoie requête URL"""


import requests
#from requests.auth import HTTPBasicAuth

#from Monpackage.fit_url import fit_url

class requete():
    
    def request_method(urlstr,requestlogin):
        retour = requests.get(urlstr, auth=requestlogin)
        #retour = requests.get(urlstr, auth=HTTPBasicAuth(requestlogin))
        
        return retour.status_code
    #(login, encodpassword))
        # url = "votre_url"
        # login = "votre_login"
        # encodepassword = "votre_encodepassword"
