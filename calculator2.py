def calculator(x,y,op):
    if op=="+":
     return x+y
    if op=="-":
       return x-y
    if op=="*":
       return x*y
    if op=="/":
       return x/y
if __name__ == "__main__":
   x=  int(input("enter the number"))
   y=int(input("enter the number"))
   op=input("enter operation ")

   result=calculator(x,y,op)
   print(f"Result: {result}")