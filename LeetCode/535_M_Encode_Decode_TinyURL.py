class Codec:
    def __init__(self):
        self.url_map = {}
        self.base_url = "http://tinyurl.com/"
        self.counter = 0
    def encode(self, longUrl: str) -> str:
        short_key = self._generate_short_key()
        self.url_map[short_key] = longUrl
        return self.base_url + short_key
    def decode(self, shortUrl: str) -> str:
        short_key = shortUrl.split(self.base_url)[1]
        return self.url_map.get(short_key, "")
    def _generate_short_key(self) -> str:
        self.counter += 1
        return str(self.counter)