from FunctionEngine.FunctionEngine import Term, Equation, FormatTypes, Operations, ureg
import numpy as np

def return_term(input) -> Term:
    if issubclass(type(input), Term):
        return input
    else:
        return Term(input)

def generic_function(function, args, formatting, bracketting_operations = [], operation = Operations.OTHER) -> Equation:
    args_term = [return_term(arg) for arg in args]
    args_val = [arg.value for arg in args_term]
    result_val = function(*args_val)
    
    output_formats = Term._build_formatting(args_term, formatting, bracketting_operations)

    result = Equation(result_val, output_formats, operation)
    return result

def sqrt(input : Term) -> Equation:
    result = generic_function(pow, [input, 0.5], r'\sqrt{{{0}}}', operation=Operations.POWER)
    return result

def sin(input) -> Equation:
    result = generic_function(np.sin, [input], r'\sin{{({0})}}')
    return result

def cos(input) -> Equation:
    result = generic_function(np.cos, [input], r'\cos{{({0})}}')
    return result

def tan(input) -> Equation:
    result = generic_function(np.tan, [input], r'\tan{{({0})}}')
    return result

def asin(input) -> Equation:
    result = generic_function(np.arcsin, [input], r'\sin^{{-1}}{{({0})}}')
    result.unit = 'radians'
    return result

def acos(input) -> Equation:
    result = generic_function(np.arccos, [input], r'\cos^{{-1}}{{({0})}}')
    result.unit = 'radians'
    return result

def atan(input) -> Equation:
    result = generic_function(np.arctan, [input], r'\tan^{{-1}}{{({0})}}')
    result.unit = 'radians'
    return result