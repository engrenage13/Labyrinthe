from systeme.FondMarin import *

class Segment:
    def __init__(self, nord: bool, est: bool, sud: bool, ouest: bool) -> None:
        self.bordures = {"nord": nord, "est": est, "sud": sud, "ouest": ouest}
        self.petiteTaille = int(xf*0.04)
        self.grandeTaille = int(xf*0.23)
        self.espaceBordure = int(xf*0.01)
        self.grandEspaceBordure = int(xf*0.03)

    def dessine(self, x: int, y: int) -> None:
        c1 = BLACK
        c2 = [170, 170, 170, 170]
        epaisseur = int(xf*0.005)
        if self.bordures["nord"]:
            couleur = c1
        else:
            couleur = c2
        draw_line_ex((int(x-self.grandeTaille/2), int(y-self.grandeTaille/2)), (int(x+self.grandeTaille/2), int(y-self.grandeTaille/2)), epaisseur, couleur)
        if self.bordures["est"]:
            couleur = c1
        else:
            couleur = c2
        draw_line_ex((int(x+self.grandeTaille/2), int(y-self.grandeTaille/2)), (int(x+self.grandeTaille/2), int(y+self.grandeTaille/2)), epaisseur, couleur)
        if self.bordures["sud"]:
            couleur = c1
        else:
            couleur = c2
        draw_line_ex((int(x-self.grandeTaille/2), int(y+self.grandeTaille/2)), (int(x+self.grandeTaille/2), int(y+self.grandeTaille/2)), epaisseur, couleur)
        if self.bordures["ouest"]:
            couleur = c1
        else:
            couleur = c2
        draw_line_ex((int(x-self.grandeTaille/2), int(y-self.grandeTaille/2)), (int(x-self.grandeTaille/2), int(y+self.grandeTaille/2)), epaisseur, couleur)

    def getDims(self) -> tuple[int]:
        taille = int(self.grandeTaille+self.grandEspaceBordure*2)
        return (taille, taille)