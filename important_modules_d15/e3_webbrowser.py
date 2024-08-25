import webbrowser as wb

search_teram = input("Insert what you want to search for: ").replace(" ","+")

wb.open(f"https://www.google.com/search?q={search_teram}")

