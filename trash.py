def open_or_senior(data):
    glist = []
    for number in data:
        if number[0] >= 55 and number[1] >= 7:
            glist.append('Senior')
        else:
            glist.append('Open')
    print(glist)

open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])