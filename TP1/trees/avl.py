import networkx as nx
from visualization import dessiner_arbre

class Noeud:
    def __init__(self, cle):
        self.cle = cle
        self.gauche = None
        self.droite = None
        self.hauteur = 1

class ArbreAVL:
    def hauteur(self, noeud):
        return noeud.hauteur if noeud else 0

    def get_equilibre(self, noeud):
        return self.hauteur(noeud.gauche) - self.hauteur(noeud.droite) if noeud else 0

    # --- ROTATIONS ---
    def rotation_droite(self, y):
        x = y.gauche
        T2 = x.droite
        x.droite = y
        y.gauche = T2
        y.hauteur = 1 + max(self.hauteur(y.gauche), self.hauteur(y.droite))
        x.hauteur = 1 + max(self.hauteur(x.gauche), self.hauteur(x.droite))
        return x

    def rotation_gauche(self, x):
        y = x.droite
        T2 = y.gauche
        y.gauche = x
        x.droite = T2
        x.hauteur = 1 + max(self.hauteur(x.gauche), self.hauteur(x.droite))
        y.hauteur = 1 + max(self.hauteur(y.gauche), self.hauteur(y.droite))
        return y

    # --- INSERTION ---
    def inserer(self, racine, cle):
        if not racine:
            return Noeud(cle)
        if cle < racine.cle:
            racine.gauche = self.inserer(racine.gauche, cle)
        elif cle > racine.cle:
            racine.droite = self.inserer(racine.droite, cle)
        else:
            return racine

        racine.hauteur = 1 + max(self.hauteur(racine.gauche), self.hauteur(racine.droite))
        equilibre = self.get_equilibre(racine)

        # Terminal logs only
        if equilibre > 1 and cle < racine.gauche.cle:
            print(f"Déséquilibre (Gauche-Gauche) sur {racine.cle} → rotation droite")
            return self.rotation_droite(racine)
        if equilibre < -1 and cle > racine.droite.cle:
            print(f"Déséquilibre (Droite-Droite) sur {racine.cle} → rotation gauche")
            return self.rotation_gauche(racine)
        if equilibre > 1 and cle > racine.gauche.cle:
            print(f"Déséquilibre (Gauche-Droite) sur {racine.cle} → rotation gauche puis droite")
            racine.gauche = self.rotation_gauche(racine.gauche)
            return self.rotation_droite(racine)
        if equilibre < -1 and cle < racine.droite.cle:
            print(f"Déséquilibre (Droite-Gauche) sur {racine.cle} → rotation droite puis gauche")
            racine.droite = self.rotation_droite(racine.droite)
            return self.rotation_gauche(racine)
        return racine

    # --- SUPPRESSION ---
    def noeud_min(self, noeud):
        courant = noeud
        while courant.gauche:
            courant = courant.gauche
        return courant

    def supprimer(self, racine, cle):
        if not racine: return racine
        if cle < racine.cle:
            racine.gauche = self.supprimer(racine.gauche, cle)
        elif cle > racine.cle:
            racine.droite = self.supprimer(racine.droite, cle)
        else:
            if not racine.gauche: return racine.droite
            if not racine.droite: return racine.gauche
            temp = self.noeud_min(racine.droite)
            racine.cle = temp.cle
            racine.droite = self.supprimer(racine.droite, temp.cle)

        racine.hauteur = 1 + max(self.hauteur(racine.gauche), self.hauteur(racine.droite))
        equilibre = self.get_equilibre(racine)

        if equilibre > 1 and self.get_equilibre(racine.gauche) >= 0:
            print(f"Déséquilibre (Gauche-Gauche) après suppression sur {racine.cle} → rotation droite")
            return self.rotation_droite(racine)
        if equilibre > 1 and self.get_equilibre(racine.gauche) < 0:
            print(f"Déséquilibre (Gauche-Droite) après suppression sur {racine.cle} → rotation gauche puis droite")
            racine.gauche = self.rotation_gauche(racine.gauche)
            return self.rotation_droite(racine)
        if equilibre < -1 and self.get_equilibre(racine.droite) <= 0:
            print(f"Déséquilibre (Droite-Droite) après suppression sur {racine.cle} → rotation gauche")
            return self.rotation_gauche(racine)
        if equilibre < -1 and self.get_equilibre(racine.droite) > 0:
            print(f"Déséquilibre (Droite-Gauche) après suppression sur {racine.cle} → rotation droite puis gauche")
            racine.droite = self.rotation_droite(racine.droite)
            return self.rotation_gauche(racine)
        return racine

# --- PROGRAMME PRINCIPAL ---
if __name__ == "__main__":
    avl = ArbreAVL()
    racine = None

    # Insertion
    valeurs = list(map(int, input("Entrez les valeurs à insérer séparées par des espaces : ").split()))
    for v in valeurs:
        racine = avl.inserer(racine, v)

    # Suppression (multiple)
    suppression_input = input("Entrez les valeurs à supprimer séparées par des espaces (ou rien pour ignorer) : ").strip()
    if suppression_input:
        valeurs_a_supprimer = list(map(int, suppression_input.split()))
        for val in valeurs_a_supprimer:
            racine = avl.supprimer(racine, val)

    # Afficher le graphique final
    dessiner_arbre(racine)
