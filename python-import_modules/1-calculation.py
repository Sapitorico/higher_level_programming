#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    a = 10
    b = 5
    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mult(a, b)
    div_result = div(a, b)
    print('{}'.format(add_result))
    print('{}'.format(sub_result))
    print('{}'.format(mul_result))
    print('{}'.format(div_result))
