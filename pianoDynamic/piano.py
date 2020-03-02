from subprocess import run
from os import getcwd


def getEmo(eg):
    happyHist = [2, 0, 3, 0, 1, 2, 0, 3, 0, 2, 0, 3]
    sadHist = [1, 2, 0, 3, 0, 2, 1, 1, 1, 0, 2, 0]
    hist = []
    temp = 0.0

    for i in eg:
        tempvals = sorted(list(map(lambda x: (x, i[x]), [
            "Bored", "Excited"])), key=lambda x: x[1], reverse=True)
        histvals = sorted(list(map(lambda x: (x, i[x]), [
            "Happy", "Sad", "Fear"])), key=lambda x: x[1], reverse=True)

        if histvals[0][0] == "happy":
            hist = happyHist
        else:
            hist = sadHist
        if tempvals[0][0] == "Excited":
            temp = 0.8
        else:
            temp = 1.0
    return hist, temp


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

hist , temp =getEmo(eg)
print("python3 "+getcwd()+"/pianoDynamic/performance_rnn_generate.py \
--config=multiconditioned_performance_with_dynamics \
--bundle_file=./models/multiconditioned_performance_with_dynamics.mag \
--output_dir=./out/piano \
--num_outputs=10 \
--num_steps=3000 \
--pitch_class_histogram=\""+str(hist)+"\" \
--temperature=")

run(["python3 "+getcwd()+"pianoDynamic/performance_rnn_generate.py --config=multiconditioned_performance_with_dynamics"])
# run(["python3 "+getcwd()+"pianoDynamic/performance_rnn_generate.py \
# --config=multiconditioned_performance_with_dynamics \
# --bundle_file=./models/multiconditioned_performance_with_dynamics.mag \
# --output_dir=./out/piano \
# --num_outputs=10 \
# --num_steps=3000 \
# --pitch_class_histogram=\""+str(hist)+"\" \
# --temperature="+str(temp)],capture_output=True)

