import json
from pyray import *
from raylib import TEXTURE_FILTER_TRILINEAR
from raylib.colors import *
from ui.bouton.taille import Taille
from ui.bouton.apparence import Apparence

TITRE_F = 'LABYRINTHE'
etatVersion = "alpha"
version = "0.1.1"

init_window(1100, 750, TITRE_F)
set_target_fps(60)

# Configuration système
fichier = open("systeme/sys.json")
config_sys = json.loads(fichier.read())

# Dimensions
xf = get_screen_width()
yf = get_screen_height()

espaceBt = int(xf*0.003)
# /

# polices
police1 = load_font('polices/Roboto-Bold.otf')
gen_texture_mipmaps([police1.texture])
set_texture_filter(police1.texture, TEXTURE_FILTER_TRILINEAR)
police1i = load_font('polices/Roboto-BoldItalic.otf')
gen_texture_mipmaps([police1i.texture])
set_texture_filter(police1i.texture, TEXTURE_FILTER_TRILINEAR)
police2 = load_font('polices/Roboto-Regular.otf')
gen_texture_mipmaps([police2.texture])
set_texture_filter(police2.texture, TEXTURE_FILTER_TRILINEAR)
police2i = load_font('polices/Roboto-Italic.otf')
gen_texture_mipmaps([police2i.texture])
set_texture_filter(police2i.texture, TEXTURE_FILTER_TRILINEAR)
police3 = load_font('polices/Roboto-Light.otf')
gen_texture_mipmaps([police3.texture])
set_texture_filter(police3.texture, TEXTURE_FILTER_TRILINEAR)
police3i = load_font('polices/Roboto-LightItalic.otf')
gen_texture_mipmaps([police3i.texture])
set_texture_filter(police3i.texture, TEXTURE_FILTER_TRILINEAR)

# -- Boutons
# Tailles
TB1o = Taille(int(yf*0.07), True)
TB1n = Taille(int(yf*0.07), False)
TB2o = Taille(int(yf*0.05), True)
TB2n = Taille(int(yf*0.05), False)

# Apparences
PTIBT1 = Apparence([[255, 255, 255, 70], [255, 255, 255, 130]], police2, 1, False)
PTIBT2 = Apparence([[0, 0, 0, 70], [0, 0, 0, 150]], police2, 1, False)
PTIBT3 = Apparence([[225, 225, 225, 255], WHITE], police2, 1, False)
PTIBT4 = Apparence([[0, 0, 0, 225], [0, 0, 0, 255]], police2, 1, False)
BTNOIR = Apparence([[0, 0, 0, 70], [0, 0, 0, 150]], police2, 1, True)
BTV = Apparence([[18, 82, 219, 255]], police2, 1, True)
BTX = Apparence([[207, 35, 41, 255]], police2, 1, True)
BTDANGER = Apparence([[118, 33, 33, 100], [151, 31, 31, 100]], police2, 1, True)
BTANNULE = Apparence([[118, 33, 33, 200], [151, 31, 31, 200]], police2, 1, False)
BTDEV = Apparence([[237, 206, 104, 200], [233, 190, 47, 200]], police2, 1, False)
