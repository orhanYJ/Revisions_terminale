"""Fabrique maths/carnet-math.woff2 : sous-ensemble de STIX Two Math (SIL OFL 1.1) renommé « Carnet Math ».

Les formules du site sont en MathML natif ; sans police mathématique (Android n'en a pas),
les parenthèses extensibles, racines et sommes s'affichent mal. Ce sous-ensemble (≈ 90 Ko)
ne garde que les glyphes utilisés et la table MATH.

Usage : pip install fonttools brotli
        python3 outils/specialites/maths/police.py STIXTwoMath-Regular.otf
(source : https://mirrors.ctan.org/fonts/stix2-otf/STIXTwoMath-Regular.otf)
"""
import os, sys
from fontTools import subset
from fontTools.ttLib import TTFont

UNICODES = ("U+0020-007E,U+00A0,U+00AB,U+00AC,U+00B0,U+00B1,U+00B7,U+00BB,U+00C0-00FF,U+2225,U+22A5,U+2016,U+0393,U+0394,U+03A3,U+03A9,U+03B1-03C9,"
            "U+03D5,U+03F5,U+2016,U+2026,U+2032-2034,U+203E,U+2061-2063,U+210E,U+212C,U+2130,U+2131,U+2115,"
            "U+211A,U+211D,U+2124,U+2113,U+2190,U+2192,U+21A6,U+21D0,U+21D2,U+21D4,U+2200,U+2203,U+2205,U+2208,"
            "U+2209,U+2211,U+220F,U+2212,U+2213,U+2216,U+2217,U+2218,U+221A,U+221E,U+2223,U+2229,U+222A,U+223C,"
            "U+2248,U+2260,U+2261,U+2264,U+2265,U+2282,U+22C5,U+22EF,U+2A7D-2A7E,U+1D434-1D467,U+1D49E,U+1D49F,"
            "U+1D4AB,U+1D6FC-1D71B")
SORTIE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "maths", "carnet-math.woff2")

opts = subset.Options()
opts.layout_features = ["*"]
opts.flavor = "woff2"
f = TTFont(sys.argv[1])
s = subset.Subsetter(opts)
s.populate(unicodes=subset.parse_unicodes(UNICODES))
s.subset(f)
for r in f["name"].names:
    if r.nameID in (1, 16):
        r.string = "Carnet Math"
    elif r.nameID == 4:
        r.string = "Carnet Math Regular"
    elif r.nameID == 6:
        r.string = "CarnetMath-Regular"
    elif r.nameID == 3:
        r.string = "Carnet Math (subset of STIX Two Math) 1.0"
f.flavor = "woff2"
f.save(SORTIE)
print(SORTIE, os.path.getsize(SORTIE), "octets")
