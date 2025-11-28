months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}


while True:
    try:
        date = input("Date: ").strip() # User inputs the date as mm/dd/yy
        date2 = date.replace(", ", "/").replace(" ","/")
        m,d,y = date2.split("/")
        if m in months and "/" in date:
            raise ValueError
        #Output should be in yr-mm-dd format
        if m in months and "," in date and 1 <= int(d) <= 31 and 1 <= int(months[m]) <= 12:
            print(f"{y}-{months[m]}-{int(d):02}")
            break
        elif 1 <= int(d) <= 31 and 1 <= int(m) <= 12:
            print(f"{y}-{int(m):02}-{int(d):02}")
            break
    except ValueError:
        pass
