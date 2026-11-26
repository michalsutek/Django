from datetime import date

from django.shortcuts import render, HttpResponse

def ahoj(request):
    return HttpResponse("Ahoj svet!")

def o_mne(request):
    kontext = {
        "meno": "Michal",
        "vek": 48,
        "zaluby": ["skola", "matematika", "hokej"],
    }
    return render(request, "ulohy/o_mne.html", kontext)

def rozvrh(request):
    hodiny = [
        {"cislo": 1, "predmet": "Programovanie"},
        {"cislo": 2, "predmet": "Programovanie"},
        {"cislo": 3, "predmet": "Matematika"},
        {"cislo": 4, "predmet": "Prax"},
        {"cislo": 5, "predmet": "Prax"},
        {"cislo": 1, "predmet": "Anglický jazyk"},
    ]
    return render(request, "ulohy/rozvrh.html", {"den": "Pondelok", "hodiny": hodiny})

def pozdrav(request):
    meno = request.GET.get("meno","") # .get nájde a vráti hodnotu prvku s indexom(kľúčom) meno, ak ho nenájde vloží prázdy string
    return render(request, "ulohy/pozdrav.html", {"meno": meno})

def sucet(request):
    vysledok = None
    if request.method == "POST":
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        vysledok = a + b
    return render(request, "ulohy/sucet.html", {"vysledok": vysledok})


def obdlznik(request):
    kontext = {}
    if request.method == "POST":
        a = float(request.POST["a"])
        b = float(request.POST["b"])
        kontext = {"a": a, "b": b, "obsah": a * b, "obvod": 2 * (a + b)}
    return render(request, "ulohy/obdlznik.html", kontext)


def vek(request):
    roky = None
    if request.method == "POST":
        rok = int(request.POST["rok"])
        roky = date.today().year - rok
    return render(request, "ulohy/vek.html", {"roky": roky})
