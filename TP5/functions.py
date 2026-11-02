def lettre_vers_nombre(c):
    return ord(c) - ord('A')

def nombre_vers_lettre(n):
    return chr(ord('A') + n)

def nettoyer(texte):
    texteNettoye = ""
    for caracter in texte:
        caracterNumber = lettre_vers_nombre(caracter)
        if(caracterNumber) :
            texteNettoye += nombre_vers_lettre(caracterNumber%26) 

def chiffrer(texte, a, b):
    resultat = []
    for c in nettoyer(texte):    
    x = lettre_vers_nombre(c)    
    resultat.append(nombre_vers_lettre((a * x + b) % 26))
    return "".join(resultat)
    message = "ATTAQUEALAUBE"