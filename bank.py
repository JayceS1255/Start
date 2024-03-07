def greeting():
    greeting = input('Greeting: ')
    money = money_g(greeting)
    print(money)


def money_g(greet):
        if greet.lower().find('hello') != -1:
             return "$0"
        elif greet.find('h') == 0:
              return "$20"
        else:
             return "$100"
    
greeting()
