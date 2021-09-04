speedMenu  =  ttk.Combobox(uiFrame, textvariable = speed_name, values = speed_list)
speedMenu.grid(row = 1, column = 2, padx = 12, pady = 10)
speedMenu.current(1)