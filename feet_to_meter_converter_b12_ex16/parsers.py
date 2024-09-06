def parse(hight):
    hight.strip()
    hight = hight.split(" ")
    feet = float(hight[0])
    inches = float(hight[1])
    return {"feet": feet, "inches": inches}