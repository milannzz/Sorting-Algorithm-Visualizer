from math import fabs
from tkinter import *
from tkinter import ttk
import random
import time

# Clearer Ui using ctypes
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

color = {
    "DARK_GRAY" : '#65696B',
    "LIGHT_GRAY" : '#d3d3d3',
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

# <--- Main Window --->

mainWindow = Tk()
mainWindow.title("Sorting Algorithms Visualizer")
mainWindow.maxsize(1000,700)
mainWindow.config(bg=color["LIGHT_GRAY"])

algo_name = StringVar()
algo_list = ['Bubble Sort','Merge Sort','Bogo Sort']

speed_name = StringVar()
speed_list = ['Fast','Medium','Slow']

array = []

# <--- Functions/definations --->

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
        return 0.300
    elif speedMenu.get() == 'Medium':
        return 0.100
    else:
        return 0.001

def sort():
    global array
    timespeed = setspeed()

    if algoMenu.get() == 'Bubble Sort':
        bubble_sort(array,drawArray,timespeed)
    elif algoMenu.get() == 'Merge Sort':
        merge_sort(array,0,len(array)-1,drawArray,timespeed)
    elif algoMenu.get() == 'Bogo Sort':
        bogo_sort(array,drawArray,timespeed)

def stop():
    pass
    

# <--- Algorithms --->

# Bogo Sort

def bogo_sort(array,drawArray,timespeed):
    size = len(array)
    while(is_sorted(array,drawArray,timespeed)==False):
        shuffle(array,drawArray,timespeed)
    
def is_sorted(array,drawArray,timespeed):
    size = len(array)
    for i in range (0,size-1):
        if(array[i] > array[i-1]):
            return False    
    return True

def shuffle(array,drawArray,timespeed):
    size = len(array)
    for i in range (0,size):
        r = random.randint(0,size-1)
        array[i],array[r] = array[r],array[i]
        drawArray(array,[color["YELLOW"] if x == i or x == r 
        else color['BLUE'] for x in range(len(array))])
        time.sleep(timespeed)
    
    drawArray(array,[color['BLUE'] for x in range(len(array))])

# Selection Sort

def selection_sort(array,drawArray,timespeed):
    pass

# Bubble Sort

def bubble_sort(array,drawArray,timespeed):
    size = len(array)
    for i in range(size-1):
        for j in range(size-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                drawArray(array,[color['YELLOW'] if x ==j or x==j+1 
                else color["BLUE"] for x in range(len(array))])
                time.sleep(timespeed)

    drawArray(array,[color['BLUE'] for x in range(len(array))])

# Merge Sort

def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def merge_sort(array,start,end,drawArray,timespeed):
    if start<end:
        mid = int((start+end)/2)
        merge_sort(array,start,mid,drawArray,timespeed)
        merge_sort(array,mid+1,end,drawArray,timespeed)

        merge(array,start,mid,end,drawArray,timespeed)

        drawArray(array,[color["PURPLE"] if x >=start 
            and x < mid else color['YELLOW'] if x==mid 
            else color['DARK_BLUE'] if x >mid and x<=end 
            else color['BLUE'] for x in range(len(array))])
        
        time.sleep(timespeed)
    
    drawArray(array,[color["BLUE"] for x in range(len(array))])


# <--- UI elements here --->

uiFrame = Frame(mainWindow,width=900,height=300,bg=color['WHITE'])
uiFrame.grid(row=0,column=0,padx=10,pady=5)

uiAlgos = Label(uiFrame,text='Algorithms: ',bg=color['WHITE'])
uiAlgos.grid(row=0,column=0,padx=10,pady=5,sticky=W)
algoMenu = ttk.Combobox(uiFrame,textvariable=algo_name,values=algo_list)
algoMenu.grid(row=0,column=2,padx=5,pady=5)
algoMenu.current(0)

uiSpeed = Label(uiFrame,text='Speed: ',bg=color['WHITE'])
uiSpeed.grid(row=1,column=0,padx=10,pady=5,sticky=W)
speedMenu = ttk.Combobox(uiFrame,textvariable=speed_name,values=speed_list)
speedMenu.grid(row=1,column=2,padx=5,pady=5)
speedMenu.current(0)

generateButton = Button(uiFrame,text='Generate Array',command=generate,bg=color['WHITE'])
generateButton.grid(row=2,column=0,padx=10,pady=10)

sortButton = Button(uiFrame,text='Sort',command=sort,bg=color['WHITE'],width=10)
sortButton.grid(row=2,column=1,padx=10,pady=10)

sortButton = Button(uiFrame,text='Stop',command=stop,bg=color['WHITE'],width=10)
sortButton.grid(row=2,column=2,padx=10,pady=10)

visualCanvas = Canvas(mainWindow,width=800,height=400,bg=color['WHITE'])
visualCanvas.grid(row=3 ,column=0,padx=10,pady=10)

# <--- Print Main Window --->

mainWindow.mainloop()
