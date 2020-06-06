def div():
    try:
        a = int(input("please enter a number"))
        b = int(input("please enter a number"))
        print(a/b)
    except ZeroDivisionError:
        print("There is a zero devide by error, Please enter a valid number")
    finally:
        print("This will run regardless of the error")


div()


