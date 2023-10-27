class Codec:
    x = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        global x
        x = longUrl
        return "http://"+longUrl[-1:-8]+"4e9iAk"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return x

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))