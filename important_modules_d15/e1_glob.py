import glob

my_files = glob.glob("files/*.txt")

print (f"{my_files}\n")

for filepath in my_files:
    print(filepath+"\n")
    with open (filepath, 'r') as file:
        print(file.read().upper())
    print("\n")