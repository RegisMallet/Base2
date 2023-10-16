"""Défini les éléments de connection"""


from Monpackage.Encode64 import encodage

class log():
    
    def requestelement(username,nomsociete,password):
        login = "%CP1252%" + encodage.encod(username) + "@@" + nomsociete + "@@noSession"
        encodpassword = encodage.encod(password)
        return login, encodpassword
    




