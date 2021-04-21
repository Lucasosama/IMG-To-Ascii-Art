import os
import time

from PIL import Image
import tkinter as tk
from tkinter import filedialog



if __name__ == '__main__':
    print("Welecome to Image to Ascii!")
    print("Please choose the Path to your Image(C:/Users/Desktop/test.png)")
    path = filedialog.askopenfilename()
    img = Image.open(path, "r")
    print("Whats the IMG size?")
    size = input()
    if(500 < int(size)):
        print("Error!! Too much Pixels! max is 500! Press Enter to Escape.")
        t = input()
        quit()
    px = img.load()
    bsize = int(size)





tsize = bsize - 1
count = 1
line = 1
ccount = 1
lineprint = ""
lates = ""

while line < tsize:

    if (ccount == tsize):
        ccount = 1
        lineprint += "\n"
        lates += lineprint
        lineprint = ""
        line += 1




    cur_color = px[ccount, line]

    if(cur_color <= (25, 25, 25)):
        lineprint += "@@"
    else:
        if (cur_color <= (40, 40, 40)):
            lineprint += '##'
        else:
            if (cur_color <= (80, 80, 80)):
                lineprint += 'ßß'
            else:
                if(cur_color <= (100, 100, 100)):
                    lineprint += "AA"
                else:
                    if (cur_color <= (120, 120, 120)):
                        lineprint += "qq"
                    else:
                        if (cur_color <= (150, 150, 150)):
                            lineprint += "??"
                        else:
                            if (cur_color <= (190, 190, 190)):
                                lineprint += "**"
                            else:
                                if (cur_color <= (210, 210, 210)):
                                    lineprint += "++"
                                else:
                                    if (cur_color <= (225, 225, 225)):
                                        lineprint += '""'
                                    else:
                                        if (cur_color <= (240, 240, 240)):
                                            lineprint += "~~"
                                        else:
                                            if (cur_color <= (255, 255, 255)):
                                                lineprint += "°°"


    ccount += 1






f = open("output.txt", "w")
f.close()
f1 = open("output.txt", "w")
f1.write(lates)
f1.close()


