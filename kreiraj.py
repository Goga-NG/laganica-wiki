import os

folder = r"docs\druga-godina\medicinska-biohemija\proteini"

fajlovi = [
    "struktura-proteina-nivoi-organizacije-molekula.md",
    "proteini-koji-vezuju-kiseonik-hemoglobin-i-mioglobin.md",
    "elementi-koji-cine-biohemijsku-masineriju-za-sintezu-proteina-ribozomi-i-rnk.md",
    "aktivacija-aminokiselina-i-sklapanje-funkcionalnog-ribozoma.md",
    "elongacija-polipeptidnog-lanca-i-okoncanje-sinteze-proteina.md",
    "posttranslaciona-obrada-proteina-u-endoplazmatskom-retikulumu-i-golgijevom-aparatu.md",
    "regulacija-genske-ekspresije-i-sinteze-proteina.md",
    "unutarcelijaska-razgradnja-proteina-lizozomi-i-ubikvitin-sistem.md",
]

sadrzaj = "*Pitanje nije završeno*\n\n[← Nazad na pitanja](index.md)\n"

for f in fajlovi:
    putanja = os.path.join(folder, f)
    with open(putanja, "w", encoding="utf-8") as file:
        file.write(sadrzaj)
    print(f"Kreiran: {f}")