def main():
    time = input("What time is it? ")
    mtime = convert(time)
    meal_times = [(7, 8, 'breakfast time!'), (12, 13, 'lunch time!'), (18, 19, 'dinner time!')]
    
    for start, end, message in meal_times:
        if start <= mtime <= end:
            print(message)
            return

def convert(time):
    hours, mins = map(int, time.split(':'))
    return hours + (mins / 60)

main()