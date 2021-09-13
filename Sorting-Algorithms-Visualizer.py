import tkinter as tk
from tkinter import ttk

import random
from Color import color

# <--- Clearer ui using ctypes --->
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# <--- Functions / definations --->

def draw_array(array, color_array):
    visual_canvas.delete("all")
    canvas_width = 980
    canvas_height = 480
    x_width = canvas_width / (len(array))
    x_offset = 0
    spacing = 2
    normalized_array = [i / max(array) for i in array] 

    for i, height in enumerate(normalized_array):
        x0 = i * x_width + x_offset + spacing
        y0 = canvas_height - height * 478
        x1 = (i + 1) * x_width + x_offset
        y1 = canvas_height
        visual_canvas.create_rectangle(x0, y0, x1, y1, fill = color_array[i]) 
    
    root_window.update_idletasks()

def generate():
    array_size = no_of_items.get()
    global array
    array = []
    for row in range(0, array_size):
        randomval = random.randint(0, 200)
        array.append(randomval)
    draw_array(array, [color['BLUE'] for x in range(len(array))])


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
    if(len(array) == 0):
        return
    timespeed = setspeed()
    algo = algorithms_menu_combobox.get()
    if algo == 'Bubble Sort':
        Algorithms.bubble_sort(array, draw_array, timespeed)
    elif algo == 'Merge Sort':
        Algorithms.merge_sort(array, 0, len(array) - 1, draw_array, timespeed)
    elif algo == 'Bogo Sort':
        Algorithms.bogo_sort(array, draw_array, timespeed)
    elif algo == 'Selection Sort':
        Algorithms.selection_sort(array, draw_array, timespeed)
    elif algo == 'Insertion Sort':
        Algorithms.insertion_sort(array, draw_array, timespeed)
    elif algo == 'Quick Sort':
        Algorithms.quick_sort(array, 0, len(array) - 1, draw_array, timespeed)
    elif algo == 'Odd Even Sort':
        Algorithms.odd_even_sort(array, draw_array, timespeed)

def swithchon():
    global switch
    switch = True
    sort() 

def stop():
    global switch
    switch = False

def exit():
    root_window.destroy()
    

# <--- Algorithms --->

class Algorithms:
    global switch
    def odd_even_sort(array, draw_array, timespeed):
        isSorted = 0
        while isSorted == 0:
            root_window.update()
            if(switch == False):
                return
            isSorted = 1
            for i in range(1, len(array) - 1, 2):
                root_window.update()
                if(switch == False):
                    return
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    isSorted = 0
                    root_window.after(timespeed, draw_array(array, [color['ORANGE'] if  x == i else color["YELLOW"] if x == i + 1 
                    else color["BLUE"] for x in range(len(array))]))
                    
            for i in range(0, len(array) - 1, 2):
                root_window.update()
                if(switch == False):
                    return
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    isSorted = 0
                    root_window.after(timespeed, draw_array(array, [color['ORANGE'] if x == i else color["YELLOW"] if x == i + 1 
                    else color["BLUE"] for x in range(len(array))]))
        draw_array(array, [color['BLUE'] for x in range(len(array))])
            

    def quick_sort(array, start, end, draw_array, timespeed):
        if start < end :
            root_window.update()
            if(switch == False):
                return

            pivot = Algorithms.partition(array, start, end, draw_array, timespeed)

            root_window.after(timespeed, draw_array(array, [color["PURPLE"] if x >= start 
                                        and x < pivot else color['ORANGE'] if x == pivot 
                                        else color['YELLOW'] if x > pivot and x <= end 
                                        else color['BLUE'] for x in range(len(array))]))

            Algorithms.quick_sort(array, start, pivot - 1, draw_array, timespeed)
            root_window.update()
            if(switch == False):
                return
            Algorithms.quick_sort(array, pivot + 1, end, draw_array, timespeed)

            root_window.after(timespeed, draw_array(array, [color["PURPLE"] if x >=start 
                                        and x < pivot else color['ORANGE'] if x == pivot
                                        else color['YELLOW'] if x > pivot and x<=end 
                                        else color['BLUE'] for x in range(len(array))]))

        draw_array(array, [color['BLUE'] for x in range(len(array))])

    def partition(array, start, end, draw_array, timespeed):
        root_window.update()
        if(switch == False):
            return
        pivot = end
        pi = array[end]
        i = start - 1
        for j in range(start, end):

            root_window.update()
            if(switch == False):
                return

            if array[j] < pi:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[pivot] = array[pivot], array[i + 1]
        return i + 1


    def insertion_sort(array, draw_array, timespeed):
        root_window.update()

        size = len(array)
        for i in range(1, size):
            key = array[i]
            j = i - 1
            while key < array[j] and j >= 0:
                root_window.update()
                if(switch == False):
                    return

                array[j + 1] = array[j]
                j -= 1
                root_window.after(timespeed, draw_array(array, [color['ORANGE'] if x == i else color["YELLOW"] if x == j 
                    else color["BLUE"] for x in range(len(array))]))
            array[j + 1] = key
            
        draw_array(array, [color['BLUE'] for x in range(len(array))])


    def bubble_sort(array, draw_array, timespeed):
        root_window.update()
        size = len(array)
        for i in range(size - 1):
            for j in range(size - i - 1):
                root_window.update()
                if(switch == False):
                    return

                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    root_window.after(timespeed, draw_array(array, [color['ORANGE'] if x == j 
                                            else color["YELLOW"] if x == j + 1
                                            else color["BLUE"] for x in range(len(array))]))
        draw_array(array, [color['BLUE'] for x in range(len(array))])



    def bogo_sort(array, draw_array, timespeed):
        size = len(array)
        root_window.update()
        while(Algorithms.is_sorted(array, draw_array, timespeed) == False):
            Algorithms.shuffle(array, draw_array, timespeed)
        
    def is_sorted(array, draw_array, timespeed):
        size = len(array)
        for i in range (0, size - 1):
            root_window.update()
            if(array[i] > array[i - 1]):
                return False    
        return True

    def shuffle(array, draw_array, timespeed):
        size = len(array)
        for i in range (0, size):
            root_window.update()
            if(switch == False):
                return

            r = random.randint(0, size - 1)
            array[i], array[r] = array[r], array[i]
            root_window.after(timespeed, 
                draw_array(array, [color["ORANGE"] if  x == r 
                else color['BLUE'] for x in range(len(array))]))
        
        draw_array(array, [color['BLUE'] for x in range(len(array))])



    def selection_sort(L, draw_array, timespeed):
        for i in range(len(L) - 1):
            min_index = i
            for j in range(i + 1,  len(L)):
                root_window.update()
                if(switch == False):
                    return

                if L[j] < L[min_index]:
                    min_index = j
                draw_array(array, [color['PURPLE'] if x == j 
                        else color['ORANGE'] if x == i 
                        else color['YELLOW'] if x == min_index 
                        else color['BLUE'] for x in range(len(array))])
            
            draw_array(array, [color['ORANGE'] if  x == i 
                        else color['YELLOW'] if  x == min_index 
                        else color["BLUE"] for x in range(len(array))])

            L[i],  L[min_index] = L[min_index],  L[i]
            
            root_window.after(timespeed, draw_array(array, [color['YELLOW'] if  x == i 
                                        else color['ORANGE'] if  x == min_index 
                                        else color["BLUE"] for x in range(len(array))]))

        draw_array(array, [color['BLUE'] for x in range(len(array))])



    def merge_sort(array, start, end, draw_array, timespeed):
        if(switch == False):
            return
        if start<end:
            mid = int((start + end) / 2)

            root_window.after(timespeed, draw_array(array, [color["PURPLE"] if x >=start 
                                        and x < mid else color['ORANGE'] if x == mid 
                                        else color['YELLOW'] if x > mid and x <= end 
                                        else color['BLUE'] for x in range(len(array))]))

            Algorithms.merge_sort(array, start, mid, draw_array, timespeed)
            root_window.update()
            if(switch == False):
                return
            Algorithms.merge_sort(array, mid + 1, end, draw_array, timespeed)

            root_window.after(timespeed, draw_array(array, [color["PURPLE"] if x >=start 
                                        and x < mid else color['ORANGE'] if x == mid 
                                        else color['YELLOW'] if x >mid and x <= end 
                                        else color['BLUE'] for x in range(len(array))]))

            Algorithms.merge(array, start, mid, end)
        
        draw_array(array, [color["BLUE"] for x in range(len(array))])

    def merge(data,  start,  mid,  end):
        if(switch == False):
            return
        p = start
        q = mid + 1
        tempArray = []
        for i in range(start,  end + 1):
            root_window.update()
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
            root_window.update()
            if(switch == False):
                return

            data[start] = tempArray[p]
            start += 1


# <--- UI elements here --->

# <-- Variable --->
array  =  []
algorithms_list = ['Quick Sort', 'Merge Sort', "Odd Even Sort", 'Bubble Sort', 'Selection Sort', "Insertion Sort", 'Bogo Sort']
speed_list = ["Real-Time", 'Fast', 'Medium', 'Slow', 'Slowest']
label_font = "hevetica 10"
button_font = "hevetica 10"
canvas_padx = 10
canvas_height = 980

root_window = tk.Tk()
root_window.title("Sorting Algorithms Visualizer")
root_window.minsize(1000, 700)
root_window.grid_columnconfigure(0, weight = 1)
root_window.grid_rowconfigure(0, weight = 1)

algorithms_name = tk.StringVar()
speed_name = tk.StringVar()
no_of_items = tk.IntVar()
no_of_items.set(100)

main_container = tk.Frame(root_window , bg=color['LIGHT_BLUE'])
main_container.grid(row=0, column=0, padx=0, pady=0)

# <--- Controls Container --- >
controls_container = tk.Frame(main_container , bg=color['WHITE'])
controls_container.grid(row=0, column=0, padx=10, pady=10)

algorithms_label = tk.Label(controls_container, text='Algorithms:', bg=color['WHITE'], anchor=tk.W, width=23, font=label_font)
algorithms_label.grid(row=0, column=0, padx=(140, 0), pady=10, sticky=tk.W)

algorithms_menu_combobox = ttk.Combobox(controls_container, textvariable=algorithms_name, values=algorithms_list, font=label_font)
algorithms_menu_combobox.grid(row=0, column=0, padx=(0, 180), sticky=tk.E)
algorithms_menu_combobox.current(0)

speed_label = tk.Label(controls_container, text='Speed:', bg=color['WHITE'], anchor=tk.W,  width=23, font=label_font)
speed_label.grid(row=1, column=0, padx=(140, 0), pady=10, sticky=tk.W)

speedMenu = ttk.Combobox(controls_container, textvariable=speed_name, values=speed_list,  font=label_font)
speedMenu.grid(row=1, column=0, padx=(0, 180), pady=10, sticky=tk.E)
speedMenu.current(1)

no_of_items_label = tk.Label(controls_container, text='Number of Columns:', bg=color['WHITE'], anchor=tk.W, width=23, font=label_font)
no_of_items_label.grid(row=2, column=0, padx=(140, 0), pady=10, sticky=tk.W)

no_of_items_entry = tk.Entry(controls_container, textvariable=no_of_items, bg=color["WHITE"], width=23, font=label_font)
no_of_items_entry.grid(row=2, column=0, padx=(0, 180), pady=10, sticky=tk.E)

# <--- Buttons Container --- >
buttons_container = tk.Frame(controls_container, bg=color['WHITE'])
buttons_container.grid(row=3, column=0)

generate_button = tk.Button(buttons_container, text='Generate', command=generate, bg=color['WHITE'], width=16, font=button_font)
generate_button.grid(row=0, column=0, padx=(64, 40), pady=0, ipady=2)

sort_button = tk.Button(buttons_container, text='Sort', command=swithchon, bg=color['WHITE'], width=16, font=button_font)
sort_button.grid(row=0, column=1, padx=(40, 40), pady=10, ipady=2)

stop_button = tk.Button(buttons_container, text='Stop', command=stop, bg=color['WHITE'], width=16, font=button_font)
stop_button.grid(row=0, column=2, padx=(40, 40), pady=10, ipady=2)

exit_button = tk.Button(buttons_container, text='Exit', command=exit, bg=color['WHITE'], background=color['RED'], fg=color['WHITE'], width=16, font=button_font)
exit_button.grid(row=0, column=3, padx=(40, 64), pady=10, ipady=2)

visual_canvas = tk.Canvas(main_container, width=980, height=480, bg=color['WHITE'])
visual_canvas.grid(row=2 , column=0, padx=canvas_padx, pady=(0, 10))


# <--- Print Main Window --->

root_window.mainloop()
