vaild=False
while not vaild:
   try:
       n=int(input("Enter a number:"))
       while n%2==0:
           print("Bye")
           n=int(input("Enter a number:"))
           valid=True
   except ValueError:
       print("Invalid input.Please enter a valid number.")

              