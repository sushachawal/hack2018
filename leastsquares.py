def leastsquares(line,data):
    y=[]
    score = 0
    for x in range(0,100):
        y.append(line["m"] * x/10 + line["c"])
    for i in range(0,len(y)-1):
        score += abs(y[i]-data[i])/(len(y)-1)
    return score
