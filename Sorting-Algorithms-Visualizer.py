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
    "PURPLE" : '#BF01FB',
    "RED" : '#FF0000',
    "ORANGE" : '#FFA500'
}

# <--- Main Window --->

mainWindow = Tk()
mainWindow.title("Sorting Algorithms Visualizer")
mainWindow.maxsize(1000,700)
mainWindow.config(bg=color["LIGHT_GRAY"])

algo_name = StringVar()
algo_list = ['Bubble Sort','Merge Sort','Selection Sort','Bogo Sort']

speed_name = StringVar()
speed_list = ["Real-Time",'Fast','Medium','Slow','Slowest']

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
    if speedMenu.get() == 'Slowest':
        return 1000
    elif speedMenu.get() == 'Slow':
        return 500
    elif speedMenu.get() == 'Medium':
        return 100
    elif speedMenu.get() == 'Fast':
        return 10
    else:
        return 0

def sort():
    global array
    timespeed = setspeed()
    if algoMenu.get() == 'Bubble Sort':
        Algorithms.bubble_sort(array,drawArray,timespeed)
    elif algoMenu.get() == 'Merge Sort':
        Algorithms.merge_sort(array,0,len(array)-1,drawArray,timespeed)
    elif algoMenu.get() == 'Bogo Sort':
        Algorithms.bogo_sort(array,drawArray,timespeed)
    elif algoMenu.get() == 'Selection Sort':
        Algorithms.selection_sort(array,drawArray,timespeed)

def swithchon():
    global switch
    switch = True
    #print ('switch on')
    sort()

def stop():
    global switch
    switch = False
    #print("Stop")

def exit():
    #print("Exiting..")
    mainWindow.destroy()
    

# <--- Algorithms --->

class Algorithms:

    def bubble_sort(array,drawArray,timespeed):
        global switch
        mainWindow.update()
        size = len(array)
        for i in range(size-1):
            for j in range(size-i-1):
                mainWindow.update()
                if(switch == False):
                    return
                if array[j] > array[j+1]:
                    array[j],array[j+1] = array[j+1],array[j]
                    mainWindow.after(timespeed,
                    drawArray(array,[color['ORANGE'] if x ==j or x==j+1 
                    else color["BLUE"] for x in range(len(array))]))

        drawArray(array,[color['BLUE'] for x in range(len(array))])



    def bogo_sort(array,drawArray,timespeed):
        size = len(array)
        mainWindow.update()
        while(Algorithms.is_sorted(array,drawArray,timespeed)==False):
            Algorithms.shuffle(array,drawArray,timespeed)
        
    def is_sorted(array,drawArray,timespeed):
        size = len(array)
        mainWindow.update()
        for i in range (0,size-1):
            if(array[i] > array[i-1]):
                return False    
        return True

    def shuffle(array,drawArray,timespeed):
        global switch
        mainWindow.update()
        size = len(array)
        mainWindow.update()
        for i in range (0,size):
            mainWindow.update()
            if(switch == False):
                return
            r = random.randint(0,size-1)
            array[i],array[r] = array[r],array[i]
            mainWindow.after(timespeed,drawArray(array,[color["ORANGE"] if x == i or x == r 
                                                        else color['BLUE'] for x in range(len(array))]))
        
        drawArray(array,[color['BLUE'] for x in range(len(array))])



    def selection_sort(L,drawArray,timespeed):
        global switch
        for i in range(len(L)-1):
            min_index = i
            for j in range(i+1, len(L)):
                mainWindow.update()
                if(switch == False):
                    return
                if L[j] < L[min_index]:
                    min_index = j
                drawArray(array,[color['PURPLE'] if x == j 
                else color['ORANGE'] if x == i 
                else color['YELLOW'] if x == min_index 
                else color['BLUE'] for x in range(len(array))])
            
            drawArray(array,[color['ORANGE'] if  x==i 
                    else color['YELLOW'] if  x==min_index 
                    else color["BLUE"] for x in range(len(array))])

            L[i], L[min_index] = L[min_index], L[i]
            
            mainWindow.after(timespeed,drawArray(array,[color['YELLOW'] if  x==i 
                    else color['ORANGE'] if  x==min_index 
                    else color["BLUE"] for x in range(len(array))]))

        drawArray(array,[color['BLUE'] for x in range(len(array))])



    def merge_sort(array,start,end,drawArray,timespeed):
        global switch
        mainWindow.update()
        if(switch == False):
            return
        if start<end:
            mid = int((start+end)/2)
            Algorithms.merge_sort(array,start,mid,drawArray,timespeed)
            Algorithms.merge_sort(array,mid+1,end,drawArray,timespeed)
            Algorithms.merge(array,start,mid,end,drawArray,timespeed)

            mainWindow.after(timespeed,drawArray(array,[color["PURPLE"] if x >=start 
                and x < mid else color['ORANGE'] if x==mid 
                else color['YELLOW'] if x >mid and x<=end 
                else color['BLUE'] for x in range(len(array))]))
        
        drawArray(array,[color["BLUE"] for x in range(len(array))])

    def merge(data, start, mid, end, drawData, timeTick):
        global switch
        mainWindow.update()
        if(switch == False):
            return
        p = start
        q = mid + 1
        tempArray = []

        for i in range(start, end+1):
            mainWindow.update()
            if(switch == False):
                return
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
            mainWindow.update()
            if(switch == False):
                return
            data[start] = tempArray[p]
            start += 1


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
speedMenu.current(1)

generateButton = Button(uiFrame,text='Generate',command=generate,bg=color['WHITE'])
generateButton.grid(row=2,column=0,padx=12,pady=10)
generateButton.config(width=12)

sortButton = Button(uiFrame,text='Sort',command=swithchon,bg=color['WHITE'])
sortButton.grid(row=2,column=1,padx=12,pady=10)
sortButton.config(width=12)

stopButton = Button(uiFrame,text='Stop',command=stop,bg=color['WHITE'])
stopButton.grid(row=2,column=2,padx=12,pady=10)
stopButton.config(width=12)

exitButton = Button(uiFrame,text='Exit',command=exit,bg=color['WHITE'],background=color['RED'],fg=color['WHITE'])
exitButton.grid(row=2,column=3,padx=12,pady=10)
exitButton.config(width=12)

visualCanvas = Canvas(mainWindow,width=800,height=400,bg=color['WHITE'])
visualCanvas.grid(row=3 ,column=0,padx=10,pady=10)

# <--- Print Main Window --->

mainWindow.mainloop()
