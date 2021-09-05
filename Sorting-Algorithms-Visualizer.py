from tkinter import  * 
from tkinter import ttk
import random
from Color import color

# Clearer Ui using ctypes
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# <--- Functions/definations --->

def drawArray (array, colorArray):
    visualCanvas.delete("all")
    canvas_width = 960
    canvas_height = 480
    x_width = canvas_width / (len(array) + 1)
    offset = 4
    spacing = 2
    normalizedArray = [i / max(array) for i in array] 

    for i, height in enumerate(normalizedArray):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 470
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        visualCanvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i]) 
    
    mainWindow.update_idletasks()

def generate():
    array_size = noofitems.get()
    global array
    array = []
    for row in range(0, array_size):
        randomval = random.randint(0, 200)
        array.append(randomval)
    drawArray(array, [color['BLUE'] for x in range(len(array))])


def setspeed():
    speed = speedMenu.get()
    if speed == 'Slowest':
        return 1000
    elif speed == 'Slow':
        return 500
    elif speed == 'Medium':
        return 100
    elif speed == 'Fast':
        return 10
    else:
        return 0

def sort():
    global array
    timespeed = setspeed()
    algo = algoMenu.get()
    if algo == 'Bubble Sort':
        Algorithms.bubble_sort(array, drawArray, timespeed)
    elif algo == 'Merge Sort':
        Algorithms.merge_sort(array, 0, len(array) - 1, drawArray, timespeed)
    elif algo == 'Bogo Sort':
        Algorithms.bogo_sort(array, drawArray, timespeed)
    elif algo == 'Selection Sort':
        Algorithms.selection_sort(array, drawArray, timespeed)
    elif algo == 'Insertion Sort':
        Algorithms.insertion_sort(array, drawArray, timespeed)
    elif algo == 'Quick Sort':
        Algorithms.quick_sort(array, 0, len(array) - 1, drawArray, timespeed)
    elif algo == 'Odd Even Sort':
        Algorithms.odd_even_sort(array, drawArray, timespeed)

def swithchon():
    global switch
    switch = True
    sort() 

def stop():
    global switch
    switch = False

def exit():
    mainWindow.destroy()
    

# <--- Algorithms --->

class Algorithms:
    global switch
    def odd_even_sort(array, drawArray, timespeed):
        isSorted = 0
        while isSorted == 0:
            mainWindow.update()
            if(switch == False):
                return
            isSorted = 1
            temp = 0
            for i in range(1, len(array) - 1, 2):
                mainWindow.update()
                if(switch == False):
                    return
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    isSorted = 0
                    mainWindow.after(timespeed, drawArray(array, [color['ORANGE'] if  x == i else color["YELLOW"] if x == i + 1 
                    else color["BLUE"] for x in range(len(array))]))
                    
            for i in range(0, len(array) - 1, 2):
                mainWindow.update()
                if(switch == False):
                    return
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    isSorted = 0
                    mainWindow.after(timespeed, drawArray(array, [color['ORANGE'] if x == i else color["YELLOW"] if x == i + 1 
                    else color["BLUE"] for x in range(len(array))]))
        drawArray(array, [color['BLUE'] for x in range(len(array))])
            

    def quick_sort(array, start, end, drawarray, timespeed):
        if start < end :
            mainWindow.update()
            if(switch == False):
                return

            pivot = Algorithms.partition(array, start, end, drawArray, timespeed)

            mainWindow.after(timespeed, drawArray(array, [color["PURPLE"] if x >= start 
                                        and x < pivot else color['ORANGE'] if x == pivot 
                                        else color['YELLOW'] if x > pivot and x <= end 
                                        else color['BLUE'] for x in range(len(array))]))

            Algorithms.quick_sort(array, start, pivot - 1, drawArray, timespeed)
            mainWindow.update()
            if(switch == False):
                return
            Algorithms.quick_sort(array, pivot + 1, end, drawArray, timespeed)

            mainWindow.after(timespeed, drawArray(array, [color["PURPLE"] if x >=start 
                                        and x < pivot else color['ORANGE'] if x == pivot
                                        else color['YELLOW'] if x > pivot and x<=end 
                                        else color['BLUE'] for x in range(len(array))]))

        drawArray(array, [color['BLUE'] for x in range(len(array))])

    def partition(array, start, end, drawarray, timespeed):
        mainWindow.update()
        if(switch == False):
            return
        pivot = end
        pi = array[end]
        i = start - 1
        for j in range(start, end):

            mainWindow.update()
            if(switch == False):
                return

            if array[j] < pi:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[pivot] = array[pivot], array[i + 1]
        return i + 1


    def insertion_sort(array, drawarray, timespeed):
        mainWindow.update()

        size = len(array)
        for i in range(1, size):
            key = array[i]
            j = i - 1
            while key < array[j] and j >= 0:
                mainWindow.update()
                if(switch == False):
                    return

                array[j + 1] = array[j]
                j -= 1
                mainWindow.after(timespeed, drawArray(array, [color['ORANGE'] if x == i else color["YELLOW"] if x == j 
                    else color["BLUE"] for x in range(len(array))]))
            array[j + 1] = key
            
        drawArray(array, [color['BLUE'] for x in range(len(array))])


    def bubble_sort(array, drawArray, timespeed):
        mainWindow.update()
        size = len(array)
        for i in range(size - 1):
            for j in range(size - i - 1):
                mainWindow.update()
                if(switch == False):
                    return

                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    mainWindow.after(timespeed, drawArray(array, [color['ORANGE'] if x == j 
                                            else color["YELLOW"] if x == j + 1
                                            else color["BLUE"] for x in range(len(array))]))
        drawArray(array, [color['BLUE'] for x in range(len(array))])



    def bogo_sort(array, drawArray, timespeed):
        size = len(array)
        mainWindow.update()
        while(Algorithms.is_sorted(array, drawArray, timespeed) == False):
            Algorithms.shuffle(array, drawArray, timespeed)
        
    def is_sorted(array, drawArray, timespeed):
        size = len(array)
        for i in range (0, size - 1):
            mainWindow.update()
            if(array[i] > array[i - 1]):
                return False    
        return True

    def shuffle(array, drawArray, timespeed):
        size = len(array)
        for i in range (0, size):
            mainWindow.update()
            if(switch == False):
                return

            r = random.randint(0, size - 1)
            array[i], array[r] = array[r], array[i]
            mainWindow.after(timespeed, 
                drawArray(array, [color["ORANGE"] if  x == r 
                else color['BLUE'] for x in range(len(array))]))
        
        drawArray(array, [color['BLUE'] for x in range(len(array))])



    def selection_sort(L, drawArray, timespeed):
        for i in range(len(L) - 1):
            min_index = i
            for j in range(i + 1,  len(L)):
                mainWindow.update()
                if(switch == False):
                    return

                if L[j] < L[min_index]:
                    min_index = j
                drawArray(array, [color['PURPLE'] if x == j 
                        else color['ORANGE'] if x == i 
                        else color['YELLOW'] if x == min_index 
                        else color['BLUE'] for x in range(len(array))])
            
            drawArray(array, [color['ORANGE'] if  x == i 
                        else color['YELLOW'] if  x == min_index 
                        else color["BLUE"] for x in range(len(array))])

            L[i],  L[min_index] = L[min_index],  L[i]
            
            mainWindow.after(timespeed, drawArray(array, [color['YELLOW'] if  x == i 
                                        else color['ORANGE'] if  x == min_index 
                                        else color["BLUE"] for x in range(len(array))]))

        drawArray(array, [color['BLUE'] for x in range(len(array))])



    def merge_sort(array, start, end, drawArray, timespeed):
        if(switch == False):
            return
        if start<end:
            mid = int((start + end) / 2)

            mainWindow.after(timespeed, drawArray(array, [color["PURPLE"] if x >=start 
                                        and x < mid else color['ORANGE'] if x == mid 
                                        else color['YELLOW'] if x > mid and x <= end 
                                        else color['BLUE'] for x in range(len(array))]))

            Algorithms.merge_sort(array, start, mid, drawArray, timespeed)
            mainWindow.update()
            if(switch == False):
                return
            Algorithms.merge_sort(array, mid + 1, end, drawArray, timespeed)

            mainWindow.after(timespeed, drawArray(array, [color["PURPLE"] if x >=start 
                                        and x < mid else color['ORANGE'] if x == mid 
                                        else color['YELLOW'] if x >mid and x <= end 
                                        else color['BLUE'] for x in range(len(array))]))

            Algorithms.merge(array, start, mid, end, drawArray, timespeed)
        
        drawArray(array, [color["BLUE"] for x in range(len(array))])

    def merge(data,  start,  mid,  end,  drawArray,  timespeed):
        if(switch == False):
            return
        p = start
        q = mid + 1
        tempArray = []
        for i in range(start,  end + 1):
            mainWindow.update()
            if(switch == False):
                return

            if p > mid:
                tempArray.append(data[q])
                q += 1
            elif q > end:
                tempArray.append(data[p])
                p += 1
            elif data[p] < data[q]:
                tempArray.append(data[p])
                p += 1
            else:
                tempArray.append(data[q])
                q += 1

        for p in range(len(tempArray)):
            mainWindow.update()
            if(switch == False):
                return

            data[start] = tempArray[p]
            start += 1


# <--- UI elements here --->

mainWindow = Tk()
mainWindow.title("Sorting Algorithms Visualizer")
mainWindow.geometry("980x710")
mainWindow.resizable(0,0)
mainWindow.config(bg = color["LIGHT_GRAY"])
mainWindow.grid_columnconfigure(0, weight = 1)
mainWindow.grid_rowconfigure(0, weight = 1)

algo_name = StringVar()
algo_list = ['Quick Sort', 'Merge Sort', "Odd Even Sort", 'Bubble Sort', 'Selection Sort', "Insertion Sort", 'Bogo Sort']

speed_name = StringVar()
speed_list = ["Real-Time", 'Fast', 'Medium', 'Slow', 'Slowest']

# Main Array
array  =  []
noofitems = IntVar()
noofitems.set(100)

uiFrame  =  Frame(mainWindow , bg = color['WHITE'])
uiFrame.grid(row = 0, column = 0, padx = 10, pady = 5)
uiFrame.grid_columnconfigure(0,  weight = 1)

uiAlgos  =  Label(uiFrame, text = 'Algorithms: ', bg = color['WHITE'])
uiAlgos.grid(row = 0, column = 0, padx = 12, pady = 10, sticky = W)

algoMenu  =  ttk.Combobox(uiFrame, textvariable = algo_name, values = algo_list)
algoMenu.grid(row = 0, column = 2, padx = 12, pady = 10)
algoMenu.current(0)

uiSpeed  =  Label(uiFrame, text = 'Speed:', bg = color['WHITE'])
uiSpeed.grid(row = 1, column = 0, padx = 12, pady = 10, sticky = W)

speedMenu  =  ttk.Combobox(uiFrame, textvariable = speed_name, values = speed_list)
speedMenu.grid(row = 1, column = 2, padx = 12, pady = 10)
speedMenu.current(1)

uiNoOfColumns  =  Label(uiFrame, text = 'Number of Columns:', bg = color['WHITE'])
uiNoOfColumns.grid(row = 2, column = 0, padx = 12, pady = 10, sticky = W)

entryNoOfColumns = Entry(uiFrame, textvariable = noofitems, bg = color["WHITE"],width = 23)
entryNoOfColumns.grid(row = 2, column = 2, padx = 12, pady = 10, sticky = W)

generateButton  =  Button(uiFrame, text = 'Generate', command = generate, bg = color['WHITE'], width = 14)
generateButton.grid(row = 3, column = 0, padx = 12, pady = 10)

sortButton  =  Button(uiFrame, text = 'Sort', command = swithchon, bg = color['WHITE'], width = 14)
sortButton.grid(row = 3, column = 1, padx = 12, pady = 10)

stopButton  =  Button(uiFrame, text = 'Stop', command = stop, bg = color['WHITE'], width = 14)
stopButton.grid(row = 3, column = 2, padx = 12, pady = 10)

exitButton  =  Button(uiFrame, text = 'Exit', command = exit, bg = color['WHITE'], background = color['RED'], fg = color['WHITE'], width = 14)
exitButton.grid(row = 3, column = 3, padx = 12, pady = 10)

visualCanvas  =  Canvas(mainWindow, width = 980, height = 480, bg = color['WHITE'])
visualCanvas.grid(row = 4 , column = 0, padx = 10, pady = (0, 10))

# <--- Print Main Window --->

mainWindow.mainloop()
