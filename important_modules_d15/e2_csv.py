import csv
import pandas as pd
with open ("files/city_temperature.csv",'r') as file:
    data_list = list(csv.reader(file))

while True:
    city = input("Temperature of city - Incert the city name or Exit to quit: ")

    for row in data_list[1:]:
        if row[0] == city.capitalize():
            print (f"The Temperature of {city} is {row[1]}")
            continue
    if city.capitalize() == "Exit":
        print("Thanks for using. Application is closing!")
        break

#example showing how to write to a csv file.
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]
# name of csv file
filename = "university_records.csv"
# writing to csv file
with open(f'files/{filename}', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)
#question - why is there a blank row in between each row?

#using panadas to read and print csv file 

#read the csv file in to a DataFrame
df = pd.read_csv('files/city_temperature.csv') 
#display the DataFrame
print(df)