from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def parse_fraction(frac_str):
            num, den = frac_str.split('/')
            return int(num) / int(den)        
        def to_frac(n):
            frac = Fraction(n).limit_denominator()
            return f"{frac.numerator}/{frac.denominator}"

        normalized = expression.replace('-', '+-')
        parts = normalized.split('+')
        num_list = []
        for part in parts:
            if part: num_list.append(parse_fraction(part))
        return to_frac(sum(num_list))
    
from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace('-', '+-')
        parts = expression.split('+')
        total = Fraction(0)
        for part in parts:
            if part: total += Fraction(part)
        return f"{total.numerator}/{total.denominator}"