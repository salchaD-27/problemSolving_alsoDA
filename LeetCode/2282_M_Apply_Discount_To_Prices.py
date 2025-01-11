class Solution:
    def acceptable(self, char: str) -> bool:
        return char.isdigit()

    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        result = []
        for word in words:
            if word.startswith('$') and len(word) > 1 and word[1:].isdigit():
                original_price = int(word[1:])
                discounted_price = original_price * (100 - discount) / 100
                discounted_word = f"${discounted_price:.2f}"
                result.append(discounted_word)
            else:
                result.append(word)
        return ' '.join(result)