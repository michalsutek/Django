from django.shortcuts import render


def du2_vizitka(request):
    kontext = {
        "meno": "Peter Kováč",
        "trieda": "III.A",
        "vek": 17,
        "predmety": ["Programovanie", "Matematika", "Telesná výchova"],
    }
    return render(request, "domace/du2_vizitka.html", kontext)


def du3_teplota(request):
    vysledok = None
    jednotka = ""
    if request.method == "POST":
        hodnota = float(request.POST["hodnota"])
        if request.POST["smer"] == "c2f":
            vysledok = hodnota * 9 / 5 + 32
            jednotka = "°F"
        else:
            vysledok = (hodnota - 32) * 5 / 9
            jednotka = "°C"
    return render(request, "domace/du3_teplota.html", {"vysledok": vysledok, "jednotka": jednotka})
