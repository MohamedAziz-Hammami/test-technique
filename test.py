import re
def concatination(chaine):
    nombres = re.findall(r'[0-9]+', chaine)
    nombre_concatene = ""
    for nombre in nombres:
      nombre_concatene += nombre
    if nombre_concatene:
     return int(nombre_concatene)
    else:
     return 0

def fichier(nom_fichier):
    total = 0
    try:
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:
                 total += concatination(ligne)
        return total
    except Exception:
        print(f"Erreur : Le fichier '{filename}' est introuvable.")
        return None
filename = r"C:\Users\bazaz\Downloads\document.txt"
resultat = fichier(filename)
if resultat is not None:
    print(f"La somme totale des nombres est : {resultat}")
