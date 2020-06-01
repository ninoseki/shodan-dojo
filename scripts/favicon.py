import base64

import mmh3
import requests

res = requests.get("https://en.wikipedia.org/favicon.ico")
b64bytes = base64.encodebytes(res.content)
print(mmh3.hash(b64bytes))
# 857403617
