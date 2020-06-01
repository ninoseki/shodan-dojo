import mmh3
import requests

res = requests.get("http://example.com")
html = res.text
print(mmh3.hash(html))
