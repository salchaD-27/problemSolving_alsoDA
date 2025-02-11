class Solution:
    def numberToWords(self, num: int) -> str:
        def helper(num):
            below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            if num == 0: return ""
            elif num < 20: return below_20[num]
            elif num < 100: return tens[num // 10] + (" " + helper(num % 10) if num % 10 != 0 else "")
            else: return below_20[num // 100] + " Hundred" + (" " + helper(num % 100) if num % 100 != 0 else "")

        if num == 0: return "Zero"
        scales = ["", "Thousand", "Million", "Billion"]
        result = ""
        scale_idx = 0
        while num > 0:
            group = num % 1000
            if group != 0: result = helper(group) + (" " + scales[scale_idx] if scales[scale_idx] != "" else "") + (" " + result if result != "" else "")
            num //= 1000
            scale_idx += 1
        return result.strip()