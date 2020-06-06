def div():
    try:
        a = int(input("please enter a number"))
        b = int(input("Please enter another number"))
        print(a/b)
    except ZeroDivisionError:
        print("There is zero devided by error ")
    finally:
        print("To test finally")

div()
