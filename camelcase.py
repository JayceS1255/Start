def main():
    camel_case = input("camelCase: ")
    snake = snake_case(camel_case)

    print(snake)

def snake_case(camel_case):
    
    snake_case = ""

    for case in camel_case:
        
        if case.isupper():
            case = case.lower()
            snake_case += "_" + case

        else:
            snake_case += case 
    return snake_case
main()