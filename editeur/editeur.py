from systeme.FondMarin import *
from ui.bouton.bouton import Bouton
from editeur.elements import segments
from editeur.segment import Segment
from random import choice

class Editeur:
    def __init__(self) -> None:
        self.selection = None
        # Boutons
        self.btHasard = Bouton(TB1o, BTV, "Nouveau", '', [self.alea])
        """, 
                    [Bouton(TB1o, BTV, "Jouer", '', [self.portailBoreal]), "J1"],
                    [Bouton(TB1n, PTIBT1, "Parametres", 'images/ui/rouage.png', [self.portailBoreal]), "ANOVEL_OPTIONS"],
                    [Bouton(TB1o, BTDANGER, "Quitter", 'images/ui/quitte.png', [self.portailBoreal]), "QUITTE"]]"""
        # /
        # Images
        """bn = load_image('images/menu/bn.png')
        ratio = yf*0.3/bn.height
        image_resize(bn, int(bn.width*ratio), int(bn.height*ratio))
        self.ibn = load_texture_from_image(bn)
        unload_image(bn)
        j1 = load_image('images/menu/j1.png')
        image_resize(j1, int(j1.width*ratio), int(j1.height*ratio))
        self.ij1 = load_texture_from_image(j1)
        unload_image(j1)"""
        # Between the worlds
        self.play = False
        self.message = ""
        self.lu = True

    def dessine(self):
        taille = segments[0].getDims()[0]
        x = int(xf/2-taille/2)
        y = int(yf*0.41-taille/2)
        draw_rectangle_rounded([x, y, taille, taille], 0.2, 300, [210, 210, 210, 165])
        if type(self.selection) == Segment:
            self.selection.dessine(int(xf/2), int(yf*0.41))
        self.btHasard.dessine(int(xf/2), int(yf*0.70))
        # numéro de version
        taille = int(yf*0.025)
        tv = measure_text_ex(police3i, version, taille, 0)
        draw_text_pro(police2i, f"{version} - {etatVersion.lower()}", (int(xf*0.005), int(yf-tv.y*1.1)), 
                    (0, 0), 0, taille, 0, GRAY)

    def alea(self) -> None:
        self.selection = choice(segments)

    # Between the worlds
    def portailBoreal(self) -> None:
        i = 0
        v = False
        while i < len(self.opt) and not v:
            if self.opt[i][0].getContact():
                v = True
                self.nouveauMessage(self.opt[i][1])
            else:
                i += 1

    def nouveauMessage(self, message: str) -> None:
        self.message = message
        self.lu = False