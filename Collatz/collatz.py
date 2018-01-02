def collatz():
    try:
        number = int(input("Enter the number here: "))
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
                #return number
            else:
                number = 3 * number + 1
                print(number)
                #return number
    except ValueError:
        print("Enter numbers only")
        collatz()


collatz()