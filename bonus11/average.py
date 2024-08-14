def get_average():
    with open ('data.txt', 'r') as file:
        t_value = file.readlines()
    n = 0
    total = 0
    for i in t_value:
        i = i.strip() # for removing leading and trailing white spaces and breakline character
        try:
            total += float(i)
            n += 1
        except ValueError:
            continue
    if n == 0:
        print ("can't divie with zero")
        return 0

    average = total/n

    return average

average_temperature = get_average()
print (f"The average temperature is: {average_temperature}")