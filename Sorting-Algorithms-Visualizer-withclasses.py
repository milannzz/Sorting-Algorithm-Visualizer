import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
from Color import color

# Clearer Ui using ctypes
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

class SAVApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.array  =  []
        self.no_of_items = tk.IntVar()
        self.no_of_items.set(100)
        self.switch = tk.BooleanVar()
        self.switch.set(False)
        self.algo_name = tk.StringVar()
        self.algo_list = ['Quick Sort', 'Merge Sort', "Odd Even Sort", 'Bubble Sort', 'Selection Sort', "Insertion Sort", 'Bogo Sort']
        self.speed_name = tk.StringVar()
        self.speed_list = ["Real-Time", 'Fast', 'Medium', 'Slow', 'Slowest']
        self.timespeed = 10
        

        # configure the root window
        self.title('Sorting Algorithms Visualizer')
        self.geometry('980x710')
        self.resizable(0,0)
        self.config(bg = color["LIGHT_GRAY"])
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        
        self.controller_ui = tk.Frame(self, bg=color["WHITE"])
        self.controller_ui.grid(row=0, column=0, padx = 10, pady = 5)
        self.controller_ui.grid_columnconfigure(0,  weight = 1)

        self.algo_ui  =  tk.Label(self.controller_ui, text = 'Algorithms: ', bg = color['WHITE'])
        self.algo_ui.grid(row=0, column=0, padx=12 , pady=10, sticky = tk.W)

        self.algo_menu  =  ttk.Combobox(self.controller_ui, textvariable = self.algo_name, values = self.algo_list)
        self.algo_menu.grid(row = 0, column = 2, padx = 12, pady = 10)
        self.algo_menu.current(0)

        self.speed_ui  =  tk.Label(self.controller_ui, text = 'Speed:', bg = color['WHITE'])
        self.speed_ui.grid(row = 1, column = 0, padx = 12, pady = 10, sticky = tk.W)

        self.speed_menu  =  ttk.Combobox(self.controller_ui, textvariable = self.speed_name, values = self.speed_list)
        self.speed_menu.grid(row = 1, column = 2, padx = 12, pady = 10)
        self.speed_menu.current(1)

        self.no_of_columns_label  =  tk.Label(self.controller_ui, text = 'Number of Columns:', bg = color['WHITE'])
        self.no_of_columns_label.grid(row = 2, column = 0, padx = 12, pady = 10, sticky = tk.W)

        self.no_of_columns_entry = tk.Entry(self.controller_ui, textvariable = self.no_of_items, bg = color["WHITE"],width = 23)
        self.no_of_columns_entry.grid(row = 2, column = 2, padx = 12, pady = 10, sticky = tk.W)

        self.generate_Button  =  tk.Button(self.controller_ui, text = 'Generate', command = self.generate, bg = color['WHITE'], width = 14)
        self.generate_Button.grid(row = 3, column = 0, padx = 12, pady = 10)

        self.sort_Button  =  tk.Button(self.controller_ui, text = 'Sort', command = self.switch_on, bg = color['WHITE'], width = 14)
        self.sort_Button.grid(row = 3, column = 1, padx = 12, pady = 10)

        self.stop_Button  =  tk.Button(self.controller_ui, text = 'Stop', command = self.stop, bg = color['WHITE'], width = 14)
        self.stop_Button.grid(row = 3, column = 2, padx = 12, pady = 10)

        self.exit_Button  =  tk.Button(self.controller_ui, text = 'Exit', command = exit, bg = color['WHITE'], background = color['RED'], fg = color['WHITE'], width = 14)
        self.exit_Button.grid(row = 3, column = 3, padx = 12, pady = 10)

        self.visual_Canvas  =  tk.Canvas(self, width = 980, height = 480, bg = color['WHITE'])
        self.visual_Canvas.grid(row = 4 , column = 0, padx = 10, pady = (0, 10))

    # <--- Functions/definations --->

    def drawArray (self, colorArray):
        self.update()
        if(self.switch == False):
            return
        self.visual_Canvas.delete("all")
        canvas_width = 960
        canvas_height = 480
        x_width = canvas_width / (len(self.array) + 1)
        offset = 4
        spacing = 2
        normalized_array = [i / max(self.array) for i in self.array] 

        for i, height in enumerate(normalized_array):
            if(self.switch == False):
                return
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height * 470
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height
            self.visual_Canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i]) 
    
        self.update_idletasks()

    def generate(self):
        self.update()
        array_size = self.no_of_items.get()
        self.array = []
        for col in range(0, array_size):
            randomval = random.randint(0, 200)
            self.array.append(randomval)
        self.drawArray([color['BLUE'] for x in range(len(self.array))])
        
    
    def setspeed(self):
        speed = self.speed_menu.get()
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

    def sort(self):
        self.timespeed = self.setspeed()
        algo = self.algo_menu.get()
        if algo == 'Bubble Sort':
            self.bubble_sort()
        elif algo == 'Merge Sort':
            self.merge_sort(0, len(self.array) - 1, )
        elif algo == 'Bogo Sort':
            self.bogo_sort()
        elif algo == 'Selection Sort':
            self.selection_sort()
        elif algo == 'Insertion Sort':
            self.insertion_sort()
        elif algo == 'Quick Sort':
            self.quick_sort(0, len(self.array) - 1, )
        elif algo == 'Odd Even Sort':
            self.odd_even_sort()

    def switch_on(self):
        self.switch = True
        self.sort()

    def stop(self):
        self.switch = False

    def exit(self):
        self.destroy()
    
    def odd_even_sort(self):
        isSorted = 0
        while isSorted == 0:
            isSorted = 1
            for i in range(1, len(self.array) - 1, 2):
                self.update()
                if(self.switch == False):
                    return
                if self.array[i] > self.array[i + 1]:
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                    isSorted = 0
                    self.after(self.timespeed, self.drawArray([color['ORANGE'] if  x == i else color["YELLOW"] if x == i + 1 
                    else color["BLUE"] for x in range(len(self.array))]))
                    
            for i in range(0, len(self.array) - 1, 2):
                self.update()
                if(self.switch == False):
                    return
                if self.array[i] > self.array[i + 1]:
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                    isSorted = 0
                    self.after(self.timespeed, self.drawArray([color['ORANGE'] if x == i else color["YELLOW"] if x == i + 1 
                    else color["BLUE"] for x in range(len(self.array))]))

        self.drawArray([color['BLUE'] for x in range(len(self.array))])
    
    def bubble_sort(self):
        size = len(self.array)
        for i in range(size - 1):
            for j in range(size - i - 1):
                self.update()
                if(self.switch == False):
                    return
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.after(self.timespeed, self.drawArray([color['ORANGE'] if x == j 
                            else color["YELLOW"] if x == j + 1
                            else color["BLUE"] for x in range(len(self.array))]))
        self.drawArray([color['BLUE'] for x in range(len(self.array))])
    
    def bogo_sort(self):
        size = len(self.array)
        self.update()
        while(self.is_sorted() == False):
            self.shuffle()
        
    def is_sorted(self):
        size = len(self.array)
        self.update()
        for i in range (0, size - 1):
            if(self.array[i] > self.array[i - 1]):
                return False    
        return True

    def shuffle(self):
        size = len(self.array)
        self.update()
        for i in range (0, size):
            self.update()
            if(self.switch == False):
                return

            r = random.randint(0, size - 1)
            self.array[i], self.array[r] = self.array[r], self.array[i]
            self.after(self.timespeed, self.drawArray([color["ORANGE"] if  x == r 
                                    else color['BLUE'] for x in range(len(self.array))]))
        
        self.drawArray([color['BLUE'] for x in range(len(self.array))])

    def quick_sort(self, start, end):
        self.update()
        if(self.switch == False):
            return
        if start < end :
            self.update()
            if(self.switch == False):
                return

            pivot = self.partition( start, end)

            self.after(self.timespeed, self.drawArray([color["PURPLE"] if x >= start 
                and x < pivot else color['ORANGE'] if x == pivot 
                else color['YELLOW'] if x > pivot and x <= end 
                else color['BLUE'] for x in range(len(self.array))]))

            self.quick_sort(start, pivot - 1)
            self.update()
            if(self.switch == False):
                return
            self.quick_sort(pivot + 1, end)

            self.after(self.timespeed, self.drawArray([color["PURPLE"] if x >=start 
                and x < pivot else color['ORANGE'] if x == pivot
                else color['YELLOW'] if x > pivot and x<=end 
                else color['BLUE'] for x in range(len(self.array))]))

            self.drawArray([color['BLUE'] for x in range(len(self.array))])

    def partition(self, start, end):
        self.update()
        if(self.switch == False):
            return
        pivot = end
        pi = self.array[end]
        i = start - 1
        for j in range(start, end):

            self.update()
            if(self.switch == False):
                return

            if self.array[j] < pi:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[pivot] = self.array[pivot], self.array[i + 1]
        return i + 1


    def insertion_sort(self):
        self.update()

        size = len(self.array)
        for i in range(1, size):
            key = self.array[i]
            j = i - 1
            while key < self.array[j] and j >= 0:
                self.update()
                if(self.switch == False):
                    return

                self.array[j + 1] = self.array[j]
                j -= 1
                self.after(self.timespeed, self.drawArray([color['ORANGE'] if x == i else color["YELLOW"] if x == j 
                    else color["BLUE"] for x in range(len(self.array))]))
            self.array[j + 1] = key
            
        self.drawArray([color['BLUE'] for x in range(len(self.array))])
    
    def selection_sort(self):
        for i in range(len(self.array) - 1):
            min_index = i
            for j in range(i + 1,  len(self.array)):
                self.update()
                if(self.switch == False):
                    return

                if self.array[j] < self.array[min_index]:
                    min_index = j
                self.drawArray([color['PURPLE'] if x == j 
                    else color['ORANGE'] if x == i 
                    else color['YELLOW'] if x == min_index 
                    else color['BLUE'] for x in range(len(self.array))])
            
            self.drawArray([color['ORANGE'] if  x == i 
                    else color['YELLOW'] if  x == min_index 
                    else color["BLUE"] for x in range(len(self.array))])

            self.array[i],  self.array[min_index] = self.array[min_index],  self.array[i]
            
            self.after(self.timespeed, self.drawArray([color['YELLOW'] if  x == i 
                    else color['ORANGE'] if  x == min_index 
                    else color["BLUE"] for x in range(len(self.array))]))

        self.drawArray([color['BLUE'] for x in range(len(self.array))])



    def merge_sort(self, start, end):
        self.update()
        if(self.switch == False):
            return
        if start<end:
            mid = int((start + end) / 2)

            self.after(self.timespeed, self.drawArray([color["PURPLE"] if x >=start 
                and x < mid else color['ORANGE'] if x == mid 
                else color['YELLOW'] if x > mid and x <= end 
                else color['BLUE'] for x in range(len(self.array))]))

            self.merge_sort(start, mid)
            self.update()
            if(self.switch == False):
                return
            self.merge_sort(mid + 1, end)

            self.after(self.timespeed, self.drawArray([color["PURPLE"] if x >=start 
                and x < mid else color['ORANGE'] if x == mid 
                else color['YELLOW'] if x >mid and x <= end 
                else color['BLUE'] for x in range(len(self.array))]))

            self.merge(start, mid, end)
        
        self.drawArray([color["BLUE"] for x in range(len(self.array))])

    def merge(self, start,  mid,  end,):
        self.update()
        if(self.switch == False):
            return

        p = start
        q = mid + 1
        tempArray = []
        
        for i in range(start,  end + 1):
            self.update()
            if(self.switch == False):
                return

            if p > mid:
                tempArray.append(self.array[q])
                q += 1
            elif q > end:
                tempArray.append(self.array[p])
                p += 1
            elif self.array[p] < self.array[q]:
                tempArray.append(self.array[p])
                p += 1
            else:
                tempArray.append(self.array[q])
                q += 1

        for p in range(len(tempArray)):
            self.update()
            if(self.switch == False):
                return

            self.array[start] = tempArray[p]
            start += 1


if __name__ == "__main__":
    app = SAVApp()
    app.mainloop()