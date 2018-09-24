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

camPos = [0, 1, 0]

canvasPosX = 2

lastLignPosY = 0

frame = tk.Tk() # setup tkinter frame
frame.title("Botticelli 3D engine")

def panelEnv() :
    envFrame = tk.Tk()
    envFrame.title("3D Environment")

    envC = tk.Canvas(envFrame, width = 300, height = 300, background = "black")
    envC.pack(padx=10, pady=10)

    def drawEnv() :
        #camPosTXT.config(text = "Camera position = " + str(camPos[0]) + ";" + str(camPos[1]) + ";" + str(camPos[2]))
        
        envC.delete("all")
        for x in range(0, 10):
            if x == 5 :
                envC.create_line(x * 30, 0, x * 30, 300, fill = "red")
            else :
                envC.create_line(x * 30, 0, x * 30, 300, fill = "white")

        for y in range(0, 10):
            if y == 5 :
                envC.create_line(0, y * 30, 300, y * 30, fill = "blue")
            else :
                envC.create_line(0, y * 30, 300, y * 30, fill = "white")

        camX = int(camPos[0] * 30 + 150)
        camY = int(camPos[2] * 30 + 150)
        
        envC.create_rectangle(camX - 5, camY - 5, camX + 5, camY + 5, fill = "yellow")
        envC.create_line(camX - 50, camY - 2 * 30, camX + 50, camY - 2 * 30, fill = "green")

        print("[DEBUG] : Draw Environment")

    def resetParam() :
        camPos = [0, 0, 3]
        canvasPosX = camPos[0] + 2
        print("[DEBUG] : Reset parameters")
        drawEnv()


    def randomParam() :
        camPos[2] = 5
        canvasPosX = camPos[0] + 5
        print("[DEBUG] : random parameters")
        drawEnv()

    def Refresh() :
        camPos[0] = int(CamXsb.get())
        camPos[1] = int(CamYsb.get())
        camPos[2] = int(CamZsb.get())

        drawEnv()
        Generate3dGrid()
        
    #RandomBTN = tk.Button(master = envFrame, text = "Random Parameters", command = randomParam).pack()

    camPosTXT = tk.Label(master = envFrame, text = "Camera position :", fg = "black").pack()
    CamXsb = tk.Spinbox(master = envFrame, from_=0, to=10).pack()
    CamYsb = tk.Spinbox(master = envFrame, from_=1, to=10).pack()
    CamZsb = tk.Spinbox(master = envFrame, from_=0, to=10).pack()

    RefreshBTN = tk.Button(master = envFrame, text = "Refresh", command = Refresh).pack()
    ResetBTN = tk.Button(master = envFrame, text = "Reset Parameters", command = resetParam).pack()

    drawEnv()
    envFrame.mainloop()


c = tk.Canvas(frame, width = fSize[0], height = fSize[1], background = "black") # create canvas
c.pack(padx=10, pady=10) # compile canvas (c)

print("[DEBUG] : PROGRAM START, WELCOME !")    

def Generate3dGrid() :
    
    c.delete("all")
    c.create_rectangle(0, fSize[1], fSize[0], fSize[1], fill = "blue") # draw sky
    
    for h in range(0, lignCountH) : # Drawing horizontal ligns
        pointOnScreenY = fSize[1] - int(((camPos[1] * ((h + 1) - canvasPosX)) / (h + 1)) * 100)

        if h == 0 :
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


envBTN = tk.Button(master = frame, text = "Environment", command = panelEnv, bg = "#07C87D", fg = "#FFFFFF", font=('Open Sans', '12'), width = 50).pack()
HierarchyBTN = tk.Button(master = frame, text = "Movement", command = Generate3dGrid, bg = "#07C87D", fg = "#FFFFFF", font=('Open Sans', '12'), width = 50).pack()
genBTN = tk.Button(master = frame, text = "Generate 3D grid", command = Generate3dGrid, bg = "#07C87D", fg = "#FFFFFF", font=('Open Sans', '12'), width = 50).pack()
tk.Label(master = frame,text = "Botticelli 3D engine - Arthur DETAILLE").pack()

frame.mainloop()
