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

You can use `http.html_hash` filter for filtering results by a hash of the favicon.

Shodan uses [MurmurHash3](https://github.com/aappleby/smhasher/wiki/MurmurHash3) as a hashing function.

- [Pivoting with Property Hashes](https://help.shodan.io/mastery/property-hashes)

In Python, you can use [mmh3](https://pypi.org/project/mmh3/) for calculating MurmurHash3.

```python
import mmh3
mmh3.hash('foo') # 32 bit signed int
# -156908512
```

And for favicon, Shodan also uses base64 before calculating the hash.

```python
import base64
import mmh3
import requests

res = requests.get("https://en.wikipedia.org/favicon.ico")
b64bytes = base64.encodebytes(res.content)
print(mmh3.hash(b64bytes))
# 857403617
```

The answer is [http.favicon.hash:857403617](https://www.shodan.io/search?query=http.favicon.hash%3A857403617).

![](https://i.imgur.com/K5eMU0I.png)

## Misc

Note that you should follow the [RFC 2045](https://tools.ietf.org/html/rfc2045) standard for the base64 encoding.

It doesn't cause any problem if you are using the standard Python library, but it might cause a problem for other languages such as Ruby.

```ruby
# it doens't match with RFC 2045 standard
b64 = Base64.strict_encode64(data)
# inserts a newline character after every 76 characters to follow the RFC 2045
rfc2045_b64 = b64.chars.each_slice(76).map(&:join).join("\n") + "\n"
```
