def main():
    x = float(input("What's X? "))
    print("X squared is", square(x))

def square(n):
      return round(n**2, 1)

main()