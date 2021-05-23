from tkinter import *
from tkinter import ttk
import random
from typing import Collection

color = {
    "DARK_GRAY" : '#65696B',
    "LIGHT_GRAY" : '#C4C5BF',
    "BLUE" : '#0CA8F6',
    "DARK_BLUE" : '#4204CC',
    "WHITE" : '#FFFFFF',
    "BLACK" : '#000000',
    "RED" : '#F22810',
    "YELLOW" : '#F7E806',
    "PINK" : '#F50BED',
    "LIGHT_GREEN" : '#05F50E',
    "PURPLE" : '#BF01FB'
}
#Main Window

mainWindow = Tk()
mainWindow.title("Sorting Algorithms Visualizer")
mainWindow.maxsize(1000,700)
mainWindow.config(bg=color["WHITE"])

algo_name = StringVar()
algo_list = ['Bubble Sort','Merge Sort']

speed_name = StringVar()
speed_list = ['Fast','Medium','Slow']

array = []

def drawArray (array,colorArray):
    visualCanvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width /(len(array)+1)
    offset = 4
    spacing = 2
    normalizedArray = [i/max(array) for i in array]

    for i,height in enumerate(normalizedArray):
        x0 = i*x_width + offset + spacing
        y0 = canvas_height - height*390
        x1 = (i+1)*x_width+offset
        y1 = canvas_height
        visualCanvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i]) 
    
    mainWindow.update_idletasks()

def generate():
    global array
    array = []
    for i in range(0,100):
        randomval = random.randint(1,150)
        array.append(randomval)
    drawArray(array,[color['BLUE'] for x in range(len(array))])


def setspeed():
    if speedMenu.get() == 'Slow':
        return 0.3
    elif speedMenu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

def sort():
    global array
    timespeed = setspeed()

    if algoMenu.get() == 'Bubble Sort':
        bubble_sort(array,drawArray,timespeed)
    pass

# <--- Algorithms --->

def bubble_sort(array,drawArray,timespeed):
    size = len(array)
    for i in range(size-1):
        for j in range(size-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                drawArray(array,[color['YELLOW'] if x ==j or x==j+1 else color["BLUE"] for x in range(len(array))])

    drawArray(array,[color['BLUE'] for x in range(len(array))])

# <--- UI elements here --->

uiFrame = Frame(mainWindow,width=900,height=300,bg=color['WHITE'])
uiFrame.grid(row=0,column=0,padx=10,pady=5)

uiAlgos = Label(uiFrame,text='Algorithms: ',bg=color['WHITE'])
uiAlgos.grid(row=0,column=1,padx=10,pady=5,sticky=W)
algoMenu = ttk.Combobox(uiFrame,textvariable=algo_name,values=algo_list)
algoMenu.grid(row=0,column=2,padx=5,pady=5)
algoMenu.current(0)

uiSpeed = Label(uiFrame,text='Speed: ',bg=color['WHITE'])
uiSpeed.grid(row=1,column=1,padx=10,pady=5,sticky=W)
speedMenu = ttk.Combobox(uiFrame,textvariable=speed_name,values=speed_list)
speedMenu.grid(row=1,column=2,padx=5,pady=5)
speedMenu.current(0)

generateButton = Button(uiFrame,text='Generate Array',command=generate,bg=color['WHITE'])
generateButton.grid(row=2,column=0,padx=5,pady=5)

sortButton = Button(uiFrame,text='Sort',command=sort,bg=color['WHITE'])
sortButton.grid(row=2,column=1,padx=5,pady=5)

visualCanvas = Canvas(mainWindow,width=800,height=400,bg=color['WHITE'])
visualCanvas.grid(row=3 ,column=0,padx=10,pady=5 )

#Print Main Window

mainWindow.mainloop()