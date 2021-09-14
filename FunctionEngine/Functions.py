from FunctionEngine.FunctionEngine import Term, Equation, FormatTypes, Operations, ureg
import numpy as np

def return_term(input) -> Term:
    if issubclass(type(input), Term):
        return input
    else:
        return Term(input)

def sqrt(input : Term) -> Equation:
    input = return_term(input)
    new_val = input.value ** 0.5

    output_formats = Term._build_formatting([input], r'\sqrt{{{}}}', [])

    result = Equation(new_val, output_formats, Operations.POWER)
    return result

def sin(input) -> Equation:
    input = return_term(input)

    new_val = np.sin(input.value.to('radians'))
    output_formats = Term._build_formatting([input], r'\sin{{({})}}', [])

    result = Equation(new_val, output_formats, [])
    return result

def cos(input) -> Equation:
    input = return_term(input)

    new_val = np.cos(input.value.to('radians'))
    output_formats = Term._build_formatting([input], r'\cos{{({})}}', [])

    result = Equation(new_val, output_formats, [])
    return result

def tan(input) -> Equation:
    input = return_term(input)

    new_val = np.tan(input.value)
    output_formats = Term._build_formatting([input], r'\tan{{({})}}', [])

    result = Equation(new_val, output_formats, [])
    return result

def asin(input) -> Equation:
    input = return_term(input)
    new_val = np.arcsin(input.value)
    output_formats = Term._build_formatting([input], r'\sin^{{-1}}{{({})}}', [])

    result = Equation(new_val, output_formats, [])
    result.unit = 'radians'
    return result

def acos(input) -> Equation:
    input = return_term(input)
    new_val = np.arccos(input.value)
    output_formats = Term._build_formatting([input], r'\cos^{{-1}}{{({})}}', [])

    result = Equation(new_val, output_formats, [])
    result.unit = 'radians'
    return result

def atan(input) -> Equation:
    input = return_term(input)
    new_val = np.arctan(input.value)
    output_formats = Term._build_formatting([input], r'\tan^{{-1}}{{({})}}', [])

    result = Equation(new_val, output_formats, [])
    result.unit = 'radians'
    return result