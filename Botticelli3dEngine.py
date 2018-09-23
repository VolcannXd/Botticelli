# -----------------------------------------------------------
# PROGRAMMED BY ARTHUR DETAILLE - 19/09/2018
# BOTTICELLI 3D ENGINE
# -----------------------------------------------------------

import tkinter as tk
import time

from tkinter import StringVar
from random import randint

fSize = [500, 500]

lignCountH = 25
lignCountV = 100

camPos = [0, 3, 0]

canvasPosX = 2

lastLignPosY = 0

#prgmStatus = StringVar()
frame = tk.Tk() # setup tkinter frame
frame.title("Botticelli 3D engine")

def ResetDefault() :
    camPos[1] = 3
    canvasPosX = 2

    print("[DEBUG] : Reset, Cam position = 3, canvas position X = 2")

def ChangeParam() :
    camPos[1] = randint(1, 5)
    canvasPosX = randint(1, 5)
    print("[DEBUG] : Change 3D parameters, cam Y pos =", camPos[1], "; canvas Pos X =", canvasPosX)

def GphysiXpanel() :
    GphysiXRoot = tk.Tk()
    GphysiXRoot.title("3D Parameters")
    
    GphysiXframe = tk.Frame(GphysiXRoot, width = 250, height = 250)
    GphysiXframe.pack(fill = None, expand = False)

    TitleTXT = tk.Label(master = GphysiXframe, text = "GphysiX 1.0", width = 20, height = 2, font=('Open Sans', '24')).pack()
    ResetBTN = tk.Button(master = GphysiXframe, text = "Reset Default Parameters", command = ResetDefault, width = 50, bg = "#07C87D", fg = "#FFFFFF").pack()
    RandomBTN = tk.Button(master = GphysiXframe, text = "Set Random Parameters", command = ChangeParam, width = 50, bg = "#07C87D", fg = "#FFFFFF").pack()
    

    GphysiXRoot.mainloop()

def changeParametersFrame() :
    stgRoot = tk.Tk()
    stgRoot.title("3D Parameters")
    
    stgFrame = tk.Frame(stgRoot, width = 250, height = 250)
    stgFrame.pack(fill = None, expand = False)

    TitleTXT = tk.Label(master = stgFrame, text = "Parameters", width = 20, height = 2, font=('Open Sans', '24')).pack()
    ResetBTN = tk.Button(master = stgFrame, text = "Reset Default Parameters", command = ResetDefault, width = 50, bg = "#07C87D", fg = "#FFFFFF").pack()
    RandomBTN = tk.Button(master = stgFrame, text = "Set Random Parameters", command = ChangeParam, width = 50, bg = "#07C87D", fg = "#FFFFFF").pack()
    

    stgRoot.mainloop()


c = tk.Canvas(frame, width = fSize[0], height = fSize[1], background = "black") # create canvas
c.pack() # compile canvas (c)

print("[DEBUG] : PROGRAM START, WELCOME !")

#prgmStatus.set("Nothing to do for now....")

def Generate3dGrid() :
    #prgmStatus.set("PROCESSING 3D CALCULATION....")
    #statusTXT.update_idletasks()
    
    c.delete("all")
    c.create_rectangle(0, fSize[1], fSize[0], fSize[1], fill = "blue") # draw sky
    
    for h in range(0, lignCountH) : # Drawing horizontal ligns
        pointOnScreenY = fSize[1] - int(((camPos[1] * ((h + 1) - canvasPosX)) / (h + 1)) * 100)

        if h == 2 :
            c.create_line(0, pointOnScreenY, fSize[0], pointOnScreenY, fill = "blue")
        else :
            c.create_line(0, pointOnScreenY, fSize[0], pointOnScreenY, fill = "white")
    
        print("[DEBUG] : drawing horizontal lign", h + 1, "| Y =", pointOnScreenY)

        if h == (lignCountH - 1) :
            lastLignPosY = pointOnScreenY
            print("")
            print("[DEBUG] : last lign Y =", lastLignPosY)

    print("") # Make some space in the console

    for v in range(0, int(lignCountV / 2)) : # Drawing 'vertical' ligns
        x1 = int(((canvasPosX * (v + 1)) / lignCountV) * 100)
        x2 = int(((canvasPosX * (v + 1)) / 1) * 100)

        x1 += (fSize[1] / 2)
        x2 += (fSize[1] / 2)
    
        c.create_line(x1, lastLignPosY, x2, fSize[1], fill = "white")
    
        print("[DEBUG] : drawing vertical lign", v + 1, "| x =", x1, ";", x2)

    for v in range(0, int(lignCountV / 2)) : # Drawing 'vertical' ligns
        x1 = int(((canvasPosX * (v + 1)) / lignCountV) * 100)
        x2 = int(((canvasPosX * (v + 1)) / 1) * 100)

        x1 = -x1 + (fSize[1] / 2)
        x2 = -x2 + (fSize[1] / 2)
    
        c.create_line(x1, lastLignPosY, x2, fSize[1], fill = "white")
    
        print("[DEBUG] : drawing vertical lign", v + 1, "| x =", x1, ";", x2)

    c.create_line(fSize[0] / 2, lastLignPosY, fSize[0] / 2, fSize[1], fill = "red")
    

    print("[DEBUG] : Displaying 3D grid")

def GetInfos() :
    print()
    print("======== [INFOS] =========")
    print("Cam Pos = ", camPos)
    print("Canvas x Offset = ", canvasPosX)
    print("Frame size =", fSize)
    print("==========================")
    print()


genBTN = tk.Button(master = frame, text = "Generate 3D grid", command = Generate3dGrid, bg = "#07C87D", fg = "#FFFFFF", font=('Open Sans', '12'), width = 50).pack()
changeBTN = tk.Button(master = frame, text = "Change 3D parameters", command = changeParametersFrame, bg = "#07C87D", fg = "#FFFFFF", font=('Open Sans', '12'), width = 50).pack()
GphysiXBTN = tk.Button(master = frame, text = "Open GphysiX 1.0 panel", command = GphysiXpanel, bg = "#07C87D", fg = "#FFFFFF", font=('Open Sans', '12'), width = 50).pack()
infosBTN = tk.Button(master = frame, text = "Get Infos (CONSOLE)", command = GetInfos, bg = "#07C87D", fg = "#FFFFFF", font=('Open Sans', '12'), width = 50).pack()
closeBTN = tk.Button(master = frame, text = "Close", command = exit, bg = "#07C87D", fg = "#FFFFFF", font=('Open Sans', '12'), width = 50).pack()
tk.Label(master = frame,text = "Botticelli 3D engine - Arthur DETAILLE").pack()

frame.mainloop()
