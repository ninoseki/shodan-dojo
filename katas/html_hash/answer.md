# Answer

Shodan has serveral filters for the HTTP protocol.

- http.component
- http.component_category
- http.favicon.hash
- http.html
- http.html_hash
- http.robots_hash
- http.securitytxt
- http.status
- http.title
- http.waf

You can use `http.html_hash` filter for filtering results by a hash of the HTML.

Shodan uses [MurmurHash3](https://github.com/aappleby/smhasher/wiki/MurmurHash3) as a hashing function.

In Python, you can use [mmh3](https://pypi.org/project/mmh3/) for calculating MurmurHash3.

```python
import mmh3
mmh3.hash('foo') # 32 bit signed int
# -156908512
```

Let's take an HTML of `http://example.com` as an input.

```python
import mmh3
import requests

res = requests.get("http://example.com")
html = res.text
print(mmh3.hash(html))
# -2087618365
```

The answer is [http.html_hash:-2087618365](https://www.shodan.io/search?query=http.html_hash%3A-2087618365).

![](https://i.imgur.com/vE8bGZx.png)
