from systeme.FondMarin import begin_drawing, end_drawing, clear_background, WHITE, config_sys
from systeme.fenetre import Fenetre
from editeur.editeur import Editeur

fen = Fenetre()
fenetres = {"editeur": Editeur()}

fenetres['editeur'].play = True
if config_sys['dev']:
    precedent = fenetres[config_sys['dev'].lower()]
    actif = fenetres[config_sys['dev'].lower()]
else:
    precedent = fenetres['editeur']
    actif = fenetres['editeur']

while not fen.jeuDoitFermer():
    begin_drawing()
    clear_background(WHITE)
    actif.dessine()
    if not actif.lu:
        actif.lu = True
        if actif.message == "QUITTE":
            fen.switchEtat()
        # modules noirs et oranges
        elif actif.message == "PRECEDENT":
            actif.play = False
            a = actif
            actif = precedent
            precedent = a
        else:
            actif.play = False
            precedent = actif
            """if actif.message == "ANOVEL_OPTIONS":
                actif = param
            elif actif.message == "ANOVEL_MENU":
                actif = menu
                if precedent == bataille:
                    bataille.timeline = 0
                    bataille.rejouer()
            elif actif.message == "BN":
                actif = bataille
            elif actif.message == "J1":
                j1.initialise()
                actif = j1"""
            actif.play = True
    end_drawing()

fen.finDuJeu()
