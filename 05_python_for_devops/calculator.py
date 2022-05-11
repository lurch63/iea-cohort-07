#!/usr/bin/python3
import operator
import math

operators = {"+": operator.add,
             "-": operator.sub,
             "*": operator.mul,
             "/": operator.truediv}

def calculate(num1, num2, op):
    try:
        return operators[op](num1, num2)
    except ZeroDivisionError:
        print("Not Today Dummy. No Division By ZERO!" )
    except TypeError:
        print("Nope. That Operand is not supported in that operation" )

