# Hash of the favicon

Create a query to find hosts which returns the same [favicon](https://en.wikipedia.org/wiki/Favicon) as `https://en.wikipedia.org/favicon.ico`.

## Hints

- Shodan uses MuarmurHash3 as a hashing function.
- Shodan processes the favicon in the following way.
  - Favicon => Base64 => MurmurHash3.

---

- [Answer](./answer.md)
