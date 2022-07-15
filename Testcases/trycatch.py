a=5
b=0


try:
    c = int(input("Enter a number : "))
    print(c)
    print("resource open")
    print(a/b)

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)

except Exception as e:
    print("you cant divide by zero : ",e)

finally:
    print("resource close")