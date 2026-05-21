import os

# Sveobuhvatna struktura svih lekcija iz medicinske biohemije
# Putanje su prebačene na forward-slash (/) za maksimalnu kompatibilnost
struktura = {
    "docs/druga-godina/medicinska-biohemija/proteini": [
        "struktura-proteina-nivoi-organizacije-molekula.md",
        "proteini-koji-vezuju-kiseonik-hemoglobin-i-mioglobin.md",
        "elementi-koji-cine-biohemijsku-masineriju-za-sintezu-proteina-ribozomi-i-rnk.md",
        "aktivacija-aminokiselina-i-sklapanje-funkcionalnog-ribozoma.md",
        "elongacija-polipeptidnog-lanca-i-okoncanje-sinteze-proteina.md",
        "posttranslaciona-obrada-proteina-u-endoplazmatskom-retikulumu-i-golgijevom-aparatu.md",
        "regulacija-genske-ekspresije-i-sinteze-proteina.md",
        "unutarcelijska-razgradnja-proteina-lizozomi-i-ubikvitin-sistem.md",
    ],
    
    "docs/druga-godina/medicinska-biohemija/enzimi": [
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
    ],

    "docs/druga-godina/medicinska-biohemija/metabolizam-i-digestija": [
        "enzimi-unutarcelijske-oksidacije-redukcije-dehidrogenaze-oksidaze-oksigenaze-sistem-citohroma-p450.md",
        "metabolicka-uloga-familije-enzima-citohroma-p450.md",
        "oksidacije-i-redukcije-u-celiji-priroda-i-dinamika-oslobadjanja-energije.md",
        "metabolicki-putevi-priroda-podela-nacin-regulacije-i-znacaj.md",
        "izmena-energije-u-celiji-slobodna-energija-endergonicne-egzergonicne-reakcije-i-veze.md",
        "enzimi-digestije-ugljenih-hidrata-i-mehanizmi-transporta-monosaharida.md",
        "digestija-resorpcija-i-reesterifikacija-lipida.md",
        "digestija-proteina-i-enzimi-digestije-resorpcija-amino-kiselina-i-transportni-sistemi.md",
    ],

    "docs/druga-godina/medicinska-biohemija/respiratorni-lanac": [
        "mitohondrijski-sistem-za-transport-elektrona-respiratorni-lanac.md",
        "atp-sintaza-i-mehanizam-oksidativne-fosforilacije.md",
    ],

    "docs/druga-godina/medicinska-biohemija/ugljeni-hidrati": [
        "znacaj-ugljenih-hidrata-in-metabolizmu.md",
        "glikoliza-reakcije-kosupstrati-i-enzimi.md",
        "kljucni-enzimi-glikolize-i-regulacija.md",
        "stvaranje-visoko-energetskih-fosfata-u-glikolizi.md",
        "glukoneogeneza-reakcije-enzimi-i-energetski-bilans.md",
        "supstrati-za-glukoneogenezu-i-regulacija.md",
        "glikemija-i-regulacija-glikemije.md",
        "sinteza-glikogena-i-regulacija.md",
        "katabolizam-glikogena-i-regulacija.md",
        "alternativni-putevi-metabolizma-i-ciklus-glukuronske-kiseline.md",
        "heksozomonofosfatni-put.md",
        "metabolizam-fruktoze-galaktoze-i-laktoze.md",
        "ugljeni-hidrati-kao-strukturni-elementi.md",
        "metabolicke-sudbine-piruvata-oksidacija-u-acetil-coa.md",
        "ciklus-trikarboksilnih-kiselina-reakcije-enzimi-i-znacaj.md",
        "regulacija-ciklusa-trikarboksilnih-kiselina.md",
        "prenosenje-redukcionih-ekvivalenata-cunasti-mehanizmi.md",
    ],

    "docs/druga-godina/medicinska-biohemija/lipidi": [
        "transport-lipida-hilomikroni-i-transport-masnih-kiselina.md",
        "sinteza-zasicenih-masnih-kiselina-izvori-acetil-coa.md",
        "sintaza-masnih-kiselina-struktura-funkcija-reakcije-i-regulacija.md",
        "elongacija-i-desaturacija-masnih-kiselina.md",
        "sinteza-i-deponovanje-triacilglicerola.md",
        "lipoliza-triacilglicerola-i-kontrola-lipolize-u-adipocitima.md",
        "oksidacija-masnih-kiselina-sa-parnim i-neparnim-brojem-atoma.md",
        "oksidacija-nezasicenih-masnih-kiselina.md",
        "metabolicke-sudbine-acetil-coa.md",
        "alternativni-putevi-oksidacije-masnih-kiselina.md",
        "fosfogliceroli-struktura-i-metabolizam.md",
        "sfingolipidi-sfingomijelin-i-glikosfingolipidi-struktura-i-metabolizam.md",
        "metabolizam-ketonskih-tela-znacaj-u-gladovanju-i-dijabetesu.md",
        "lipoproteini-plazme-metabolizam-i-klinicki-znacaj-hilomikrona-i-vldl.md",
        "lipoproteini-plazme-metabolizam-i-klinicki-znacaj-ldl-i-hdl.md",
        "metabolizam-i-klinicki-znacaj-holesterola.md",
        "holesterol-kao-prekursor-zucnih-kiselina.md",
        "sinteza-lipoproteina-u-jetri.md",
    ],

    "docs/druga-godina/medicinska-biohemija/metabolizam-proteina": [
        "slobodne-aminokiseline-u-organizmu-i-njihov-promet.md",
        "metabolicki-procesi-u-kojima-se-koriste-slobodne-aminokiseline.md",
        "katabolizam-aminokiselina-transaminacija-i-oksidativna-deaminacija.md",
        "metabolicka-sudbina-azota-aminokiselina-ciklus-ureje.md",
        "metabolicke-sudbine-ugljovodonicnog-kostura-aminokiselina.md",
        "sinteza-aminokiselina-iz-intermedijera-glikolize.md",
        "sinteza-aminokiselina-iz-intermedijera-ciklusa-trikarboksilnih-kiselina.md",
        "katabolizam-aminokiselina-koje-se-razgradjuju-do-acetil-coa.md",
        "katabolizam-aminokiselina-razgranatog-lanca-i-lizina.md",
        "katabolizam-aminokiselina-koje-se-razgradjuju-do-alfa-ketoglutarata-ili-oksalacetata.md",
        "katabolizam-aminokiselina-koje-se-razgradjuju-do-sukcinil-coa.md",
        "katabolizam-aminokiselina-koje-se-razgradjuju-do-piruvata.md",
        "aminokiseline-kao-prekursori-bioloski-vaznih-jedinjenja.md",
        "biosinteza-hema-regulacija.md",
        "razgradnja-porfirina-i-katabolizam-hema-metabolizam-bilirubina.md",
        "metabolizam-gvozdja.md",
    ],

    "docs/druga-godina/medicinska-biohemija/metabolizam-nukleotida": [
        "sinteza-purinskih-nukleotida-regulacija.md",
        "sinteza-pirimidinskih-nukleotida-regulacija.md",
        "katabolizam-purinskih-i-pirimidinskih-nukleotida.md",
        "dnk-sastav-struktura-i-organizacija-u-hromatinu.md",
        "rnk-sastav-struktura-i-vrste.md",
        "replikacija-dnk.md",
        "transkripcija-dnk-u-rnk.md",
        "posttranskripciona-obrada-rnk.md",
        "regulacija-transkripcije-dnk-u-rnk.md",
    ],

    "docs/druga-godina/medicinska-biohemija/signalni-putevi": [
        "bioloske-membrane-sastav-i-organizacija.md",
        "receptori-na-celijskim-membranama-i-u-celiji.md",
        "receptori-povezani-sa-g-proteinima-sistem-adenilat-ciklaze.md",
        "receptori-povezani-sa-g-proteinima-signalni-put-fosfolipaze-c.md",
        "uloga-fosforilacije-defosforilacije-proteina-u-unutarcelijskoj-signalizaciji.md",
        "receptori-sa-tirozin-kinaznom-enzimskom-aktivnoscu.md",
        "hormoni-definicija-podela-prema-mestu-delovanja-i-hemijskom-sastavu.md",
        "hijerarhijska-organizacija-endokrinog-sistema.md",
        "endokrina-regulacija-na-nivou-hipotalamusa-i-hipofize-faktori-oslobadjanja.md",
        "hormon-rasta-hemijska-priroda-sinteza-transport-mehanizam-i-efekti.md",
        "hormoni-tireoidne-zlezde-hemijska-priroda-sinteza-transport-i-mehanizam.md",
        "hormoni-koji-regulisu-metabolizam-kalcijuma.md",
        "glukokortikoidi-hemijska-priroda-sinteza-transport-i-mehanizam.md",
        "mineralokortikoidi-hemijska-priroda-sinteza-transport-i-mehanizam.md",
        "hormoni-srzi-nadbubrezne-zlezde-hemijska-priroda-sinteza-i-mehanizam.md",
        "muski-polni-hormoni-hemijska-priroda-sinteza-transport-i-mehanizam.md",
        "zenski-polni-hormoni-hemijska-priroda-sinteza-transport-i-mehanizam.md",
        "hormoni-pankreasa-hemijska-priroda-sinteza-transport-i-mehanizam.md",
        "hormoni-gastrointestinalnog-trakta-hemijska-priroda-i-mehanizam-delovanja.md",
        "hemijski-prenos-signala-u-nervnom-sistemu.md",
        "azotni-oksid-sistem-gvanilat-ciklaze.md",
        "metaboliti-arahidonske-kiseline-prostaglandini-tromboksani-i-leukotrijeni.md",
        "celijski-ciklus-uloga-kompleksa-ciklin-ciklin-zavisne-kinaze.md",
    ],

    "docs/druga-godina/medicinska-biohemija/vitamini": [
        "biohemijske-karakteristike-i-biohemijski-znacaj-hidrosolubilnih-vitamina.md",
        "biohemijske-karakteristike-i-biohemijski-znacaj-liposolubilnih-vitamina.md",
        "vitamini-kao-antioksidanti.md",
        "vitamini-b-kompleksa-kao-kofaktori-niacin-i-riboflavin.md",
        "vitamini-b-kompleksa-kao-kofaktori-tiamin-b6.md",
        "vitamini-b-kompleksa-kao-kofaktori-b12-i-folna-kiselina.md",
        "vitamini-b-kompleksa-kao-kofaktori-pantotenska-kiselina-i-biotin.md",
        "koenzimi-u-prenosenju-jednougljenicnih-ostataka.md",
    ],

    "docs/druga-godina/medicinska-biohemija/regulacija-metabolizma": [
        "slobodni-radikali-nastanak-detoksikacija-i-patofizioloski-znacaj.md",
        "regulacija-metabolizma-na-nivou-organizma-uloga-jetre.md",
        "metabolicke-specificnosti-skeletnih-i-srcanog-misica.md",
        "metabolizam-posle-obroka-izmedju-obroka-i-u-gladovanju.md",
        "biohemijska-organizacija-celijskog-jezgra.md",
        "biohemijska-organizacija-mitohondrija.md",
        "biohemijske-karakteristike-celijskih-membrana.md",
        "proteini-krvne-plazme.md",
        "biohemijske-karakteristike-krvnih-celija.md",
        "metabolicke-funkcije-jetre.md",
        "metabolizam-etanola.md",
        "molekulska-osnova-procesa-detoksikacije-u-jetri.md",
        "neurotransmiteri-i-hemijska-transmisija-u-nervnom-sistemu.md",
        "metabolizam-ksenobiotika-sistem-citohroma-p450-i-konjugacija.md",
        "biohemijski-pokazatelji-funkcije-bubrega-urea-i-kreatinin.md",
        "klinicko-biohemijski-pokazatelji-regulacije-glikemije.md",
        "fizicko-hemijske-i-biohemijske-karakteristike-urina.md",
        "endokrina-funkcija-bubrega-raas-eritropoetin-prostaglandini-vitamin-d.md",
    ]
}

# Sadržaj za svako pojedinačno pitanje
tekst_pitanja = "Pitanje nije zavrseno\n"

# Mapiranje čistih naslova za automatsku generaciju index.md fajlova
naslovi_indeksa = {
    "proteini": "Proteini",
    "enzimi": "Enzimi",
    "metabolizam-i-digestija": "Metabolizam i digestija",
    "respiratorni-lanac": "Respiratorni lanac",
    "ugljeni-hidrati": "Ugljeni hidrati",
    "lipidi": "Lipidi",
    "metabolizam-proteina": "Metabolizam proteina",
    "metabolizam-nukleotida": "Metabolizam nukleotida",
    "signalni-putevi": "Signalni putevi",
    "vitamini": "Vitamini",
    "regulacija-metabolizma": "Regulacija metabolizma", 
}

# Definišemo Markdown link za nazad 
dugme_nazad = "[🔙 Nazad na pitanja](../)\n\n"

# --- KOD ZA GENERISANJE FAJLOVA ---

for folder_putanja, fajlovi in struktura.items():
    try:
        # 1. Kreiranje celog stabla direktorijuma ukoliko već ne postoji
        os.makedirs(folder_putanja, exist_ok=True)
        
        # Ekstrakcija imena foldera za generisanje Index naslova
        ime_foldera = os.path.basename(os.path.normpath(folder_putanja))
        naslov_indeksa_str = naslovi_indeksa.get(ime_foldera, ime_foldera.replace("-", " ").capitalize())
        
        # Početni sadržaj za automatski index.md
        index_sadrzaj = f"[🔙 Nazad na pitanja](../index.md)\n\n# {naslov_indeksa_str}\n\n"
        
        # 2. Generisanje svakog .md fajla u direktorijumu
        for fajl in fajlovi:
            puna_putanja = os.path.join(folder_putanja, fajl)
            
            # Ekstrakcija i formatiranje naslova iz imena fajla 
            naslov_lekcije = fajl.replace(".md", "").replace("-", " ").capitalize()
            
            # Kreiranje konačnog sadržaja fajla
            sadrzaj = f"{dugme_nazad}# {naslov_lekcije}\n\n{tekst_pitanja}"
            
            # Upisivanje u specifični fajl lekcije
            with open(puna_putanja, "w", encoding="utf-8") as f:
                f.write(sadrzaj)
            
            # Dodavanje reference u index.md
            index_sadrzaj += f"- [{naslov_lekcije}](./{fajl})\n"
            
        # 3. Upisivanje zbirnog index.md fajla za taj folder
        puna_putanja_indeksa = os.path.join(folder_putanja, "index.md")
        with open(puna_putanja_indeksa, "w", encoding="utf-8") as f:
            f.write(index_sadrzaj)
            
    except Exception as e:
        print(f"❌ Došlo je do greške prilikom kreiranja foldera {folder_putanja}: {e}")

print("✅ Skripta je uspešno kreirala sve foldere, fajlove lekcija sa 'Nazad' dugmetom i index.md fajlove!")