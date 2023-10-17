"""Fichier de démarrage"""

from Monpackage.request import requete
#from Monpackage.log import log
from Monpackage.variable_a_afficher import vaffich
from Monpackage import affich

if __name__ == '__main__':
    username ="RM"
    nomsociete = "HVALV_prod"
    password = "Regis!"
    url = "https://www.google.fr/"
    
    #urlstr = fitting_url(url)
    #urlstr = url
    #requestlogin = log.requestelement(username,nomsociete,password)
    #requeteresult = requete.request_method(urlstr,requestlogin)
    
    vaffich.enregistrer_variable("cette fois")
    affich.loadweb.app_run(affich.loadweb.app,affich.loadweb.open_browser)
    

    #loadweb.run_server(loadweb.open_browser,loadweb.app)

# httpXlmDoc.open "GET", url, False, login, encodepassword
# httpXlmDoc.setRequestHeader "content-type", application/x-www-form-urlencoded"
# httpXlmDoc.send



