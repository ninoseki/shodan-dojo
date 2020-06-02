# Hash of the favicon

Create a query to find hosts which returns the same [favicon](https://en.wikipedia.org/wiki/Favicon) as `https://en.wikipedia.org/favicon.ico`.

## Hints

- Shodan uses MuarmurHash3 as a hashing function.
- You can use `http.html_hash` filter.
  - http.favicon.hash: MuarmurHash3 hash value
  - e.g.
    - `http.favicon.hash:708578229` (https://www.google.com/favicon.ico)
- Shodan processes the favicon in the following way.
  - Favicon => Base64 => MurmurHash3.
- MuarmurHash3 libraries:
  - Go https://github.com/DataDog/mmh3
  - JS: https://www.npmjs.com/package/murmurhash3js
  - Python: https://pypi.org/project/mmh3/
  - Ruby: https://rubygems.org/gems/mmh3/
  - etc.

---

- [Answer](./answer.md)
