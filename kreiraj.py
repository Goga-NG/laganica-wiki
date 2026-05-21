import os

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
        "nomenklatura-i-klasifikacija-enzima.md",  # Popravljeni razmaci u crtice
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

# Identitičan tekst i link kakav imaš u proteinima
sadrzaj = "# *Pitanje nije završeno*\n\n[← Nazad na pitanja](index.md)\n"

for folder, fajlovi in struktura.items():
    # Kreira folder ako ne postoji
    os.makedirs(folder, exist_ok=True)
    
    for f in fajlovi:
        putanja = os.path.join(folder, f)
        
        # Prvo obrišemo stari fajl ako postoji, da očistimo eventualne greške
        if os.path.exists(putanja):
            os.remove(putanja)
            
        # Upisujemo svež sadržaj sa linkom
        with open(putanja, "w", encoding="utf-8") as file:
            file.write(sadrzaj)

print("Svi fajlovi u enzimima su uspešno prepisani i sada imaju identičan hiperlink!")