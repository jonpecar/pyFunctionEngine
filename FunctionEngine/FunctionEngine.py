from logging import Formatter
from pint import UnitRegistry
from enum import Enum

ureg = UnitRegistry()

class Operations(Enum):
    POWER = 0
    MULTIPLY = 1
    DIVIDE = 2
    ADD = 3
    SUBTRACT = 4
    OTHER = 5

class FormatTypes(Enum):
    SYMBOLS = 0
    NO_UNITS = 1
    WITH_UNITS = 2

class Term:
    
    value = None
    symbol = None

    def __init__(self, value, symbol = None, unit = None):
        if unit:
            self.value = value * ureg(unit)
        else:
            self.value = value * ureg('dimensionless')
        
        if symbol:
            self.symbol = symbol
        else:
            try:
                self.symbol = self._formatted_types
            except:
                self.symbol = str(self.value)

    def formatted_value(self, format : FormatTypes):
        if format == FormatTypes.SYMBOLS:
            return self.symbol
        elif format == FormatTypes.WITH_UNITS:
            return self._formatted_types
        elif format == FormatTypes.NO_UNITS:
            return self._formatted_typeless

    def result_value(self, format : FormatTypes):
        return self.symbol + ' = ' + self.formatted_value(format)
        
    @property
    def magnitude(self):
        return self.value.magnitude

    @property
    def _formatted_types(self):
        if not self.unit.dimensionless:
            option1 = '{:~L}'.format(self.value)
            option2 = '{:.2f~L}'.format(self.value)
            if len(option2) < len(option1):
                return option2
            else:
                return option1
        else:
            return self._formatted_typeless

    @property
    def _formatted_typeless(self):
        option1 = '{:}'.format(self.value.magnitude)
        option2 = '{:.2f}'.format(self.value.magnitude)
        if len(option2) < len(option1):
            return option2
        else:
            return option1

    def __rmul__(self, other):
        return Term(other) * self

    def __mul__(self, other: 'Term'):
        try:
            value = self.value * other.value
        except:
            other = Term(other)
            value = self.value * other.value

        output_formats = Term._build_formatting([self, other], r'{{{}}} \times {{{}}}',[Operations.ADD, Operations.SUBTRACT])

        result = Equation(value, output_formats, Operations.MULTIPLY)
        return result

    def __radd__(self, other):
        return Term(other) + self

    def __add__(self, other: 'Term'):
        try:
            value = self.value + other.value
        except:
            other = Term(other)
            value = self.value + other.value

        output_formats = Term._build_formatting([self, other], r'{{{}}} + {{{}}}',[])

        result = Equation(value, output_formats, Operations.ADD)
        return result

    def __rsub__(self, other):
        return Term(other) - self

    def __sub__(self, other: 'Term'):
        try:
            value = self.value - other.value
        except:
            other = Term(other)
            value = self.value - other.value

        output_formats = Term._build_formatting([self, other], r'{{{}}} - {{{}}}',[])

        result = Equation(value, output_formats, Operations.SUBTRACT)
        return result

    def __rtruediv__(self, other):
        return Term(other) / self

    def __truediv__(self, other : 'Term'):
        try:
            value = self.value / other.value
        except:
            other = Term(other)
            value = self.value / other.value

        output_formats = Term._build_formatting([self, other], r'\frac{{{}}}{{{}}}',[])

        result = Equation(value, output_formats, Operations.DIVIDE)
        return result

    def __rpow__(self, other):
        return Term(other) ** self

    def __pow__(self, other : 'Term'):
        try:
            value = self.value ** other.value
        except:
            other = Term(other)
            value = self.value ** other.value

        output_formats = Term._build_formatting([self, other], '{{{}}}^{{{}}}', [Operations.ADD, Operations.DIVIDE, Operations.MULTIPLY, Operations.SUBTRACT])

        result = Equation(value, output_formats, Operations.POWER)
        return result


    def _add_brackets(text):
        return '(' + text + ')'

    def _select_formatting(item : 'Term', operations_to_bracket):
        formats = [None] * len(FormatTypes)
        if type(item) == Term or type(item) == Equation and item.symbol:
            for i in FormatTypes:
                formats[i.value] = item.formatted_value(i)
        elif type(item) == Equation:
            for i in FormatTypes:
                formats[i.value] = item.formatted_formula(i)
            if item.operation in operations_to_bracket:
                for i in len(formats):
                    formats[i] = Term._add_brackets(formats[i])

        return formats
    
    def _build_formatting(terms, formatting, bracketting_operations):
        
        output_formats = [None] * len(FormatTypes)
        formatted_terms = [ [] for _ in range(len(FormatTypes))]

        for term in terms:
            term_formats = Term._select_formatting(term, bracketting_operations)
            for i in range(len(term_formats)):
                formatted_terms[i].append(term_formats[i])
        for i in range(len(output_formats)):
            output_formats[i] = formatting.format(*formatted_terms[i])
        
        return output_formats

    @property
    def unit(self):
        return self.value.units

    @unit.setter
    def unit(self, target_unit):
        self.value.ito(target_unit)
    

class Equation(Term):
    _formulas = [None, None, None]
    operation = None
    def __init__(self, value, formulas, operation):
        self.operation = operation
        self._formulas = formulas
        self.value = value

    def formatted_formula(self, format : FormatTypes):
        return self._formulas[format.value]

    def result_formula(self, format : FormatTypes):
        result = self.symbol + ' = ' + self._formulas[format.value]
        if format != FormatTypes.SYMBOLS:
            result += ' = ' + self.formatted_value(format)
        return result


