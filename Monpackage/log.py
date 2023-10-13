"""Défini les éléments de connection"""


from Monpackage.Encode64 import encodage
from Monpackage.user import User


class log(encodage,User):
    
    def requestelement(encodage):
        login = "%CP1252%" & encodage.encod(User.username + "@@" + User.nomsociete + "@@noSession")
        encodpassword = encodage.encod(User.password)
        return login, encodpassword
    




