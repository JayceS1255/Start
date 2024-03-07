def main():
    outdated = input("Date: ")
    date = norm_date(outdated)
    if date:
        print(date)
    letter_date = l_date(outdated)
    


def norm_date(out_date):
    parts = out_date.split("/")
    if len(parts) == 3:
        month, day, year = map(int, parts)
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{year}-{month}-{day}"  
        else:
            main()


def l_date(out_date):
    parts = out_date.split(" ")
    if len(parts) == 3:
        month, day, year = parts
        day = day.replace(",", "")
        list_month = [
            "January", "February", "March", "April",
            "May", "June", "July", "August", "September",
            "October", "November", "December"
        ]
        if month in list_month:
            nmonth = list_month.index(month) + 1
            if 1 <= int(day) <= 31:
                print(f"{year}-{nmonth}-{day}")


if __name__ == "__main__":
    main()