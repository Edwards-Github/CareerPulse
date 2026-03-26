import hashlib, re
from typing import Dict, Optional, Callable

class URLShortener:
	def __init__(self):
		# Temporary storage (Week 3 we move this to SQLite!)
		self.url_map: Dict[str, str] = {}

	@staticmethod
	def validate_url_decorator(func: Callable) -> bool:
		def wrapper(self, url: str): # Keep 'self' here because generate_code needs it!
			# The "Security Check"
			pattern = re.compile(r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$')
			if not pattern.match(url):
				raise ValueError(f"Invalid URL: {url}")

			# If valid, run the original function
			return func(self, url)
		return wrapper

	@validate_url_decorator
	def generate_code(self, url: str) -> str:
		# Professional way to create a unique ID
		# url.encode() turns string into bytes. Input: str ("https://google.com") Output: Byte str (b"https://google.com")
		# hashlib.md5() generates a deterministic id (meaning if you give it the same URL 1,000 times you will get the same hash 1,000 times) from bytes. Input: raw Bytes Output: A MD5 Hash Object
		# hexdigest turns the unique ID back into human readable string. Input: messy binary data inside the Hash Object. Output: Hexadecimal String (containing only 0-9 and a-f)
		# Why? The raw output of a hash is "non-printable" binary. If you tried to print it, your terminal might show weird symbols or beep. 
		# .hexdigest() translates those bits into a clean string that you can actually save in a database or put in a URL.
		return hashlib.md5(url.encode()).hexdigest()[:6]

	def shorten(self, long_url: str) -> str:
		code = self.generate_code(long_url)
		self.url_map[code] = long_url
		return code

	def resolve(self, code: str) -> Optional[str]:
		return self.url_map.get(code)

# Quick Test
if __name__ == "__main__":
    tracker = URLShortener()
    my_link = "https://www.google.com/search?q=python+jobs+in+tech"
    short = tracker.shorten(my_link)
    print(f"Short Code: {short}")
    print(f"Original: {tracker.resolve(short)}")
    
try:
	# This will work
	print(f"Valid: {tracker.shorten('https://google.com')}")

	# This will trigger the Decorator's ValueError
	print(f"Invalid: {tracker.shorten('not-a-link')}")
except ValueError as e:
	print(f"Caught by Decorator: {e}")