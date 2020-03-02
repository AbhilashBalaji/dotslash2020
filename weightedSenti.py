from subprocess import call
from os import getcwd
import re

eg = [{
    "Bored": 0.2768371562,
    "Angry": 0.2231197248,
    "Sad": 10.2348101367,
    "Fear": 0.2431143526,
    "Happy": 3.5176188243,
    "Excited": 0.1044998055,
},
    {
    "Bored": 0.1220240678,
    "Angry": 0.4097742549,
    "Sad": 0.3024230883,
    "Fear": 0.1383221974,
    "Happy": 0.0160412186,
    "Excited": 0.011415173,
}
]


def getEmo(eg):
    # happyHist = [2, 0, 1, 0, 3, 1, 0, 3, 0, 2, 0, 1]
    happyHist = [2, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
    sadHist = [2, 1, 0, 3, 0, 2, 0, 2, 1, 0, 2, 0]
    # happyPrimer = []

    hists = []
    temps = []

    for i in eg:
        tempvals = sorted(list(map(lambda x: (x, i[x]), [
            "Bored", "Excited"])), key=lambda x: x[1], reverse=True)
        histvals = sorted(list(map(lambda x: (x, i[x]), [
            "Happy", "Sad", "Fear"])), key=lambda x: x[1], reverse=True)

        if histvals[0][0] == "Happy":
            hists.append(happyHist)
        else:
            hists.append(sadHist)
        if tempvals[0][0] == "Excited":
            temps.append(15)
        else:
            temps.append(5)
    return hists, temps


hists, temps = getEmo(eg)

temps = list(map(lambda x: float(x), temps))

a = list(zip(hists, temps))[0]
with open('./params', 'w') as the_file:
    print(str(a[0]), a[1], sep=";", file=the_file)

call([getcwd()+"/pianoDynamic/piano.sh"])
