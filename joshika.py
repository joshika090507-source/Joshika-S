def check_number():
    try:
        num=int(input("Enter a number"))

        if num%2==0:
            print("Even")
        else:
            print("odd")
            
    except ValueError:
          print("Enter a valid number:")
check_number()

   
