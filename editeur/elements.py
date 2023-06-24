import json
from editeur.segment import Segment

fichier = open("editeur/segments.json")
elements = json.loads(fichier.read())

segments = []
for i in range(len(elements["segments"])):
    seg = elements["segments"][i]
    segments.append(Segment(seg["cotes"][0], seg["cotes"][1], seg["cotes"][2], seg["cotes"][3]))