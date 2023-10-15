"""Fichier de démarrage"""

from Monpackage.affich import loadweb

if __name__ == '__main__':
    username ="RM"
    nomsociete = "HVALVES_prod"
    password = "Regis2022!"
    url = "https://vnsylob1:8443/rest/login"
    
    loadweb.run_server(loadweb.open_browser,loadweb.app)

# httpXlmDoc.open "GET", url, False, login, encodepassword
# httpXlmDoc.setRequestHeader "content-type", application/x-www-form-urlencoded"
# httpXlmDoc.send



