from django.shortcuts import render


def cv1_index(request):
    return render(request, "cv1/cv1_index.html", {"meno": "Jana Nováková"})


def cv1_obchod(request):
    produkty = [
        {"nazov": "Rožok", "cena": 0.15},
        {"nazov": "Mlieko", "cena": 1.29},
        {"nazov": "Syr", "cena": 6.50},
        {"nazov": "Káva", "cena": 8.90},
    ]
    max_cena = None
    if request.GET.get("max"):
        max_cena = float(request.GET["max"])
    return render(request, "cv1/cv1_obchod.html", {"produkty": produkty, "max_cena": max_cena})


def cv1_body(request):
    kontext = {}
    if request.method == "POST":
        body = float(request.POST["body"])
        maximum = float(request.POST["maximum"])
        percenta = body / maximum * 100
        if percenta >= 90:
            znamka = 1
        elif percenta >= 75:
            znamka = 2
        elif percenta >= 50:
            znamka = 3
        elif percenta >= 30:
            znamka = 4
        else:
            znamka = 5
        kontext = {"body": body, "maximum": maximum, "percenta": percenta, "znamka": znamka}
    return render(request, "cv1/cv1_body.html", kontext)
