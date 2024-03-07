def main():
    time = input("What time is it? ")

    mtime = convert(time)


    if 7 <= mtime <= 8:
        print('breakfast time!')
    elif 12 <= mtime <= 13:
        print('lunch time!')
    elif 18 <= mtime <= 19:
        print('dinner time!')
    else:
        print('')


def convert(time):
    
    hours, mins = map(int, time.split(':'))

    rtime = hours + (mins/60)

    return rtime

main()
