class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0: return str(numerator // denominator)
        negative = (numerator < 0) ^ (denominator < 0)  
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part = str(numerator // denominator)
        remainder = numerator % denominator
        fraction_part = []
        seen_remainders = {} 
        index = 0
        while remainder and remainder not in seen_remainders:
            seen_remainders[remainder] = index
            remainder *= 10
            fraction_part.append(str(remainder // denominator))
            remainder %= denominator
            index += 1
        if remainder in seen_remainders:
            repeat_index = seen_remainders[remainder]
            fraction_part.insert(repeat_index, "(")
            fraction_part.append(")")
        result = integer_part + "." + "".join(fraction_part)
        return "-" + result if negative else result