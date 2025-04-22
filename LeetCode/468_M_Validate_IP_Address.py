class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def check4(ip):
            groups = ip.split(".")
            if len(groups) != 4: return False
            for xi in groups:
                if not xi.isdigit(): return False
                if len(xi) > 1 and xi[0] == '0': return False
                if not 0 <= int(xi) <= 255: return False
            return True

        def check6(ip):
            hex_digits = "0123456789abcdefABCDEF"
            groups = ip.split(":")
            if len(groups) != 8: return False
            for xi in groups:
                if not (1 <= len(xi) <= 4): return False
                for ch in xi:
                    if ch not in hex_digits: return False
            return True

        if "." in queryIP and check4(queryIP): return "IPv4"
        elif ":" in queryIP and check6(queryIP): return "IPv6"
        else: return "Neither"