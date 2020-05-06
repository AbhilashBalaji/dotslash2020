from requests import post
import re
# with open('joker.html') as f :
#     text = f.read()
# text = re.sub(r'<.*>|</.*>|\n|\t|[0-9]+|\.|\:|\(.*\)','',text)
# text = ['i am sad', 'i feel sad']
# data={
#     'text' : str(text),
#     #DQGXTm78iYT5YNaGec63L3anhkURdTCbEgvmxiTtuas
#     'api_key' : 'QYBB8z8xGCp0c2N4N8sPUz6pKe0MxGKJb0ct80NZgi8'
# }
# r = post('https://apis.paralleldots.com/v4/emotion_batch', data)
# eg = r.json()['emotion']
eg = [{
    "Bored": 0.0768371562,
    "Angry": 0.2231197248,
    "Sad": 0.2348101367,
    "Fear": 0.2431143526,
    "Happy": 0.1176188243,
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
    happyHist = [2, 0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 1]
    sadHist = [1, 2, 0, 3, 0, 2, 1, 1, 1, 0, 2, 0]
    hists = []
    temps = []

    for i in eg:
        tempvals = sorted(list(map(lambda x: (x, i[x]), [
            "Bored", "Excited"])), key=lambda x: x[1], reverse=True)
        histvals = sorted(list(map(lambda x: (x, i[x]), [
            "Happy", "Sad", "Fear"])), key=lambda x: x[1], reverse=True)

        if histvals[0][0] == "happy":
            hists.append( happyHist)
        else:
            hists.append(sadHist)
        if tempvals[0][0] == "Excited":
            temps.append(1)
        else:
            temps.append(1.2)
    return hists,temps


hists,temps=getEmo(eg)
# print(his)
temps = list(map(lambda x: float(x), temps))
# print(hists,temps)
a = list(zip(hists, temps))[0]
print(str(a[0]),a[1],sep=";")
