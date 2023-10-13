"""encode une chaine en utf-8."""

import base64


class encodage():
    def __init__(self,chaine):
        """Initialise la chaine à encoder."""
        self.chaine = chaine
    
    def encod(chaine):
        """encode une chaine en utf-8."""
        chaine_encodee = base64.b64encode(chaine.encode('utf-8'))
        print(chaine_encodee)  # Affiche : b'QUJDMTIzIQ=='
    
    def decod(chaine):
        """dé-encode une chaine en utf-8."""
        chaine_decodee = base64.b64decode(chaine).decode('utf-8')
        print(chaine_decodee)  # Affiche : ABC123!
        

# # Encoder une chaîne de caractères
# chaine = "Regis2022!"
# chaine_encodee = base64.b64encode(chaine.encode('utf-8'))
# print(chaine_encodee)  # Affiche : b'QUJDMTIzIQ=='

# # Décoder une chaîne de caractères
# chaine_decodee = base64.b64decode(chaine_encodee).decode('utf-8')
# print(chaine_decodee)  # Affiche : ABC123!
#base64.b64encode,base64.b64decode