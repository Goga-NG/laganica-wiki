import os

# Rečnik sa strukturom foldera i pripadajućih fajlova
struktura = {
    r"docs\druga-godina\medicinska-biohemija\proteini": [
        "struktura-proteina-nivoi-organizacije-molekula.md",
        "proteini-koji-vezuju-kiseonik-hemoglobin-i-mioglobin.md",
        "elementi-koji-cine-biohemijsku-masineriju-za-sintezu-proteina-ribozomi-i-rnk.md",
        "aktivacija-aminokiselina-i-sklapanje-funkcionalnog-ribozoma.md",
        "elongacija-polipeptidnog-lanca-i-okoncanje-sinteze-proteina.md",
        "posttranslaciona-obrada-proteina-u-endoplazmatskom-retikulumu-i-golgijevom-aparatu.md",
        "regulacija-genske-ekspresije-i-sinteze-proteina.md",
        "unutarcelijska-razgradnja-proteina-lizozomi-i-ubikvitin-sistem.md",
    ],
    
    r"docs\druga-godina\medicinska-biohemija\enzimi": [
        "opste-osobine-enzima-i-struktura-molekula-enzima.md",
        "kvaternarna-struktura-enzima-izoenzimi.md",
        "struktura-aktivnog-mesta-enzima-familije-enzima.md",
        "nomenklatura-i-klasifikacija-enzima.md",
        "mehanizmi-enzimske-katalize.md",
        "kinetika-enzimske-katalize.md",
        "inhibicija-enzima-bioloski-znacaj-reverzibilne-i-ireverzibilne-inhibicije-enzima.md",
        "metali-i-oligoelementi-kao-kofaktori-enzima.md",
        "multienzimski-kompleksi.md",
        "subcelijska-organizacija-enzima.md",
        "posttranslacioni-kovalentni-mehanizmi.md",
        "posttranslacioni-nekovalentni-mehanizmi.md",
        "regulacija-kolicine-enzima-u-celiji.md",
        "alosterni-enzimi.md",
        "koenzimi.md",
        "ribozimi.md",
        "funkcionalni-i-nefunkcionalni-enzimi-plazme.md",
        "transaminaze.md",
        "ggt.md",
        "ck.md",
        "ldh.md",
        "amilaza.md",
    ]
}

# ISPRAVLJENO: Dodat čist razmak i formatiran naslov
sadrzaj = "# *Pitanje nije završeno*\n\n[← Nazad na pitanja](index.md)\n"

# Prolazak kroz strukturu i ponovno kreiranje/prebrisavanje fajlova
for folder, fajlovi in struktura.items():
    os.makedirs(folder, exist_ok=True)
    
    for f in fajlovi:
        putanja = os.path.join(folder, f)
        with open(putanja, "w", encoding="utf-8") as file:
            file.write(sadrzaj)
        print(f"Osvežen: {putanja}")