def calculator(a,b,op):
    if op=="+":
        return a+b
    if op=="-":
        return a-b
    if op=="/":
        return a/b
    if op=="%":
        return a%b
if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, /, %): ")
    result = calculator(a, b, op)
    print(f"Result: {result}")
