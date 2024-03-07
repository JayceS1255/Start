name = input('What is your name? ')
#remove whitespace from string and captalize
name = name.strip().title()
#split name
first, last = name.split(" ")
print('hello', first)
