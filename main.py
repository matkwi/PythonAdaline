import random
from tkinter.ttk import Progressbar

from Adaline import Adaline
import numpy as np
from tkinter import *

root = Tk()

root.geometry('501x432')
root.title("Adaline")
root.resizable(False, False)

canvas = Canvas(root, height=350, width=501, bg="white")

rectColors = [[0 for x in range(7)] for x in range(7)]  # Tablica z 0 i 1, gdzie 0 to szary, a 1 to zielony

perceptrons = []
for _ in range(10):
    perceptrons.append(Adaline(7 * 7))


my_rects = []
z = False


# Kliknięcie w piksel
def clicked(eventorigin):
    x = eventorigin.x
    y = eventorigin.y
    x = x / 50
    x = int(x)
    y = y / 50
    y = int(y)
    if rectColors[x][y] == 0:
        canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="green", tags="clicked")
        rectColors[x][y] = 1
    else:
        canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey", tags="clicked")
        rectColors[x][y] = 0


# Wszystkie piksele na szaro
def resetCanvas():
    for x in range(7):
        for y in range(7):
            canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey", tags="clicked")
            rectColors[x][y] = 0


def drawCanvas():
    for x in range(7):
        for y in range(7):
            if rectColors[x][y] == 1:
                canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="green", tags="clicked")
            elif rectColors[x][y] == 0:
                canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey", tags="clicked")


resetCanvas()

canvas.tag_bind("clicked", "<Button-1>", clicked)

canvas.pack()

number = [[] for _ in range(10)]
number[0] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
number[1] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
number[2] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
number[3] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
number[4] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
number[5] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
number[6] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
number[7] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
number[8] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
number[9] = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]

numbers = [np.ravel(n) for n in number]


# Rysowanie klikniętej cyfry
def makeNumber(num):
    resetCanvas()
    p = 0
    for y in range(7):
        for x in range(7):
            if numbers[num][p] == 1:
                canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="green", tags="clicked")
                rectColors[x][y] = 1
            p = p + 1


def b0Clicked():
    makeNumber(0)


def b1Clicked():
    makeNumber(1)


def b2Clicked():
    makeNumber(2)


def b3Clicked():
    makeNumber(3)


def b4Clicked():
    makeNumber(4)


def b5Clicked():
    makeNumber(5)


def b6Clicked():
    makeNumber(6)


def b7Clicked():
    makeNumber(7)


def b8Clicked():
    makeNumber(8)


def b9Clicked():
    makeNumber(9)


b0 = Button(root, text="0", command=b0Clicked).place(x=0, y=355, width=50, height=25)
b1 = Button(root, text="1", command=b1Clicked).place(x=50, y=355, width=50, height=25)
b2 = Button(root, text="2", command=b2Clicked).place(x=100, y=355, width=50, height=25)
b3 = Button(root, text="3", command=b3Clicked).place(x=150, y=355, width=50, height=25)
b4 = Button(root, text="4", command=b4Clicked).place(x=200, y=355, width=50, height=25)
b5 = Button(root, text="5", command=b5Clicked).place(x=0, y=380, width=50, height=25)
b6 = Button(root, text="6", command=b6Clicked).place(x=50, y=380, width=50, height=25)
b7 = Button(root, text="7", command=b7Clicked).place(x=100, y=380, width=50, height=25)
b8 = Button(root, text="8", command=b8Clicked).place(x=150, y=380, width=50, height=25)
b9 = Button(root, text="9", command=b9Clicked).place(x=200, y=380, width=50, height=25)


# Przycisk resetuje piksele
def cleanClicked():
    resetCanvas()
    varOut.set("OUT")


# Uczenie algorytmem Adaline
def learnClicked():
    close_file = False
    training_inputs = [np.ravel(n) for n in number]
    colors = ["red", "orange", "yellow", "green", "blue", "pink", "purple", "grey", "black", "brown"]
    label = '0'
    for i, value in enumerate(training_inputs):
        training_inputs[i] = np.concatenate((np.array([1]), training_inputs[i]))  # Dodanie biasu
    for i in range(10):
        label = i.__str__()
        labels = np.zeros(10)
        labels[i] = 1
        if i == 9:
            close_file = True
        perceptrons[i].train(training_inputs, labels, 'file', colors[i], close_file, label)


# Check sprawdza narysowaną cyfrę
def check():
    global my_rects
    global z
    if z:
        for i in range(10):
            canvas.delete(my_rects[i])
        del my_rects[:]
    height = 30
    w = -20
    prediction = -1
    global rectColors
    inputs = [0 for x in range(49)]
    j = 0
    for x in range(7):
        for y in range(7):
            inputs[j] = rectColors[y][x]
            j = j + 1
    inputs = np.concatenate((np.array([1]), inputs))  # Dodanie biasu
    for x in range(10):
        if perceptrons[x].output(inputs) > 0:
            my_rects.append(canvas.create_rectangle(370, height, 370 + perceptrons[x].output(inputs) * 100, height + 15, fill="green"))
        else:
            my_rects.append(canvas.create_rectangle(370, height, 370, height + 15, fill="green"))
        height += 20
        if perceptrons[x].output(inputs) > w and perceptrons[x].output(inputs) > 0:
            w = perceptrons[x].output(inputs)
            prediction = x
    if prediction >= 0:
        varOut.set(prediction)
    else:
        varOut.set("NULL")
    z = True


def checkClicked():
    check()


# Resetowanie perceptronów
def resetPerceptrons():
    global perceptrons
    perceptrons = []
    for _ in range(10):
        perceptrons.append(Adaline(7 * 7))


def moveUpClicked():
    global rectColors
    for y in range(7):
        for x in range(7):
            if rectColors[x][y] == 1:
                if y == 0:
                    return
                rectColors[x][y] = 0
                canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey", tags="clicked")
                rectColors[x][y - 1] = 1
                canvas.create_rectangle(x * 50, (y-1) * 50, x * 50 + 50, (y-1) * 50 + 50, fill="green", tags="clicked")


def moveDownClicked():
    global rectColors
    for y in range(6, -1, -1):
        for x in range(7):
            if rectColors[x][y] == 1:
                if y == 6:
                    return
                rectColors[x][y] = 0
                canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey", tags="clicked")
                rectColors[x][y + 1] = 1
                canvas.create_rectangle(x * 50, (y+1) * 50, x * 50 + 50, (y+1) * 50 + 50, fill="green", tags="clicked")


def moveLeftClicked():
    global rectColors
    for x in range(7):
        for y in range(7):
            if rectColors[x][y] == 1:
                if x == 0:
                    return
                rectColors[x][y] = 0
                canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey", tags="clicked")
                rectColors[x - 1][y] = 1
                canvas.create_rectangle((x-1) * 50, y * 50, (x-1) * 50 + 50, y * 50 + 50, fill="green", tags="clicked")


def moveRightClicked():
    global rectColors
    for x in range(6, -1, -1):
        for y in range(7):
            if rectColors[x][y] == 1:
                if x == 6:
                    return
                rectColors[x][y] = 0
                canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey", tags="clicked")
                rectColors[x + 1][y] = 1
                canvas.create_rectangle((x+1) * 50, y * 50, (x+1) * 50 + 50, y * 50 + 50, fill="green", tags="clicked")


buttonClean = Button(root, text="Clean", command=cleanClicked).place(x=0, y=405, width=61, height=25)
buttonLearn = Button(root, text="Learn", command=learnClicked).place(x=63, y=405, width=61, height=25)
buttonCheck = Button(root, text="Check", command=checkClicked).place(x=126, y=405, width=61, height=25)
buttonResetPerceptrons = Button(root, text="resPerc", command=resetPerceptrons).place(x=189, y=405, width=61, height=25)
buttonMoveUp = Button(root, text="up", command=moveUpClicked).place(x=400, y=380, width=50, height=25)
buttonMoveDown = Button(root, text="down", command=moveDownClicked).place(x=400, y=405, width=50, height=25)
buttonMoveLeft = Button(root, text="left", command=moveLeftClicked).place(x=350, y=405, width=50, height=25)
buttonMoveRight = Button(root, text="right", command=moveRightClicked).place(x=450, y=405, width=50, height=25)


def vertClicked():
    global rectColors
    for y in range(7):
        for x in range(3):
            temp = rectColors[x][y]
            rectColors[x][y] = rectColors[6 - x][y]
            rectColors[6 - x][y] = temp
            # swap(rectColors[x][y], rectColors[x][6 - y])
    drawCanvas()


def horiClicked():
    global rectColors
    for x in range(7):
        for y in range(3):
            temp = rectColors[x][y]
            rectColors[x][y] = rectColors[x][6 - y]
            rectColors[x][6 - y] = temp
            # swap(rectColors[x][y], rectColors[x][6 - y])
    drawCanvas()


def negClicked():
    global rectColors
    for x in range(7):
        for y in range(7):
            if rectColors[x][y] == 0:
                rectColors[x][y] = 1
            elif rectColors[x][y] == 1:
                rectColors[x][y] = 0
    drawCanvas()


def transClicked():
    global rectColors
    rectColors = np.transpose(rectColors)
    drawCanvas()


def rotaClicked():
    global rectColors
    rectColors = np.rot90(rectColors)
    drawCanvas()


def noiseClicked():
    global rectColors
    for _ in range(2):
        x = random.randint(0, 6)
        y = random.randint(0, 6)
        if rectColors[x][y] == 0:
            rectColors[x][y] = 1
        else:
            rectColors[x][y] = 0
    drawCanvas()


buttonVert = Button(root, text="Vert", command=vertClicked).place(x=250, y=355, width=50, height=25)
buttonHori = Button(root, text="Hori", command=horiClicked).place(x=300, y=355, width=50, height=25)
buttonNeg = Button(root, text="Neg", command=negClicked).place(x=250, y=380, width=50, height=25)
buttonTrans = Button(root, text="Trans", command=transClicked).place(x=300, y=380, width=50, height=25)
buttonRota = Button(root, text="Rota", command=rotaClicked).place(x=250, y=405, width=50, height=25)
buttonNoise = Button(root, text="Noise", command=noiseClicked).place(x=300, y=405, width=50, height=25)


varOut = StringVar()
label = Label(root, textvariable=varOut, relief=RAISED, font=(None, 25)).place(x=375, y=250, width=100, height=100)
varOut.set("OUT")

varOutConf = StringVar()
label_confidence = Label(root, textvariable=varOutConf, font=(None, 15)).place(x=370, y=10, width=100, height=14)
varOutConf.set("Confidence:")

varOut0 = StringVar()
label0 = Label(root, textvariable=varOut0, font=(None, 12)).place(x=355, y=30, width=15, height=14)
varOut0.set("0:")

varOut1 = StringVar()
label1 = Label(root, textvariable=varOut1, font=(None, 12)).place(x=355, y=50, width=15, height=14)
varOut1.set("1:")

varOut2 = StringVar()
label2 = Label(root, textvariable=varOut2, font=(None, 12)).place(x=355, y=70, width=15, height=14)
varOut2.set("2:")

varOut3 = StringVar()
label3 = Label(root, textvariable=varOut3, font=(None, 12)).place(x=355, y=90, width=15, height=14)
varOut3.set("3:")

varOut4 = StringVar()
label4 = Label(root, textvariable=varOut4, font=(None, 12)).place(x=355, y=110, width=15, height=14)
varOut4.set("4:")

varOut5 = StringVar()
label5 = Label(root, textvariable=varOut5, font=(None, 12)).place(x=355, y=130, width=15, height=14)
varOut5.set("5:")

varOut6 = StringVar()
label6 = Label(root, textvariable=varOut6, font=(None, 12)).place(x=355, y=150, width=15, height=14)
varOut6.set("6:")

varOut7 = StringVar()
label7 = Label(root, textvariable=varOut7, font=(None, 12)).place(x=355, y=170, width=15, height=14)
varOut7.set("7:")

varOut8 = StringVar()
label8 = Label(root, textvariable=varOut8, font=(None, 12)).place(x=355, y=190, width=15, height=14)
varOut8.set("8:")

varOut9 = StringVar()
label9 = Label(root, textvariable=varOut9, font=(None, 12)).place(x=355, y=210, width=15, height=14)
varOut9.set("9:")


root.mainloop()
