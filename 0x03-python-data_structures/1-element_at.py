def element_at(my_list, idx):
    if idx < 0:
        str = "None"
        return str
    if idx > len(my_list):
        str = "None"
        return str
    else:
        str = my_list[idx]
        return str
