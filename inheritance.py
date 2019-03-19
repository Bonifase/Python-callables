def combiner(my_list):
    num = 0
    s = ""

    for el in my_list:
        if isinstance(el, str):
            s += el
        else:
            num += el

    return s + str(num)