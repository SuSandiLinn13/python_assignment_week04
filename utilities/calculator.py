def add(num1,num2):
    sum = num1 + num2
    return sum

def subtract(num1,num2):
    difference = num1-num2
    return difference

def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(dividend, divisor):
    quotient = dividend / divisor
    return quotient

if __name__ == "__main__":
    x = 10
    y = 5
    print(add(x, y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))
