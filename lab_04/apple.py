def countApplesAndOranges(s, t, a, b,apples,oranges):
    aoh=0
    ooh=0
    locationapple=[]
    locationorange=[]
    for i in apples:
        locationapple.append(i + a)
    for i in oranges:
        locationorange.append(i + b)
    for i in range(s, t+1):
        if i in locationapple:
            aoh +=1
        elif i in locationorange:
            ooh +=1
    return "apples:", aoh, "orange:", ooh, 
print(countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4]))
