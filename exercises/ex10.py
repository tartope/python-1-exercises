def calculator():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    operation_type = input("Enter number (+, *, /, -): ")

    if operation_type == "+":
        sum = num1 + num2
        return sum
    elif operation_type == "*":
        product = num1 * num2
        return product
    elif operation_type == "-":
        difference = num1 - num2
        return difference
    else:
        quotient = num1 / num2
        return quotient